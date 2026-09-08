"""Provider selection and configuration tests; no model requests are made."""

import os
import unittest
from unittest.mock import MagicMock, patch

from co_op_translator.config.llm_config.anthropic import AnthropicConfig
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider


class AnthropicConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.env = patch.dict(
            os.environ,
            {
                "ANTHROPIC_API_KEY": "test-key",
                "ANTHROPIC_CHAT_MODEL_ID": "claude-test",
            },
            clear=True,
        )
        self.env.start()
        self.addCleanup(self.env.stop)

    def test_anthropic_only_auto_detection(self):
        self.assertEqual(LLMConfig.get_available_provider(), LLMProvider.ANTHROPIC)

    def test_explicit_selection_overrides_openai(self):
        os.environ.update(
            CO_OP_TRANSLATOR_PROVIDER="anthropic",
            OPENAI_API_KEY="other-key",
            OPENAI_CHAT_MODEL_ID="other-model",
        )
        self.assertEqual(LLMConfig.get_available_provider(), LLMProvider.ANTHROPIC)

    def test_default_openai_priority_unchanged(self):
        os.environ.update(
            OPENAI_API_KEY="other-key", OPENAI_CHAT_MODEL_ID="other-model"
        )
        self.assertEqual(LLMConfig.get_available_provider(), LLMProvider.OPENAI)

    def test_explicit_incomplete_selection_never_falls_back(self):
        os.environ.update(
            CO_OP_TRANSLATOR_PROVIDER="anthropic",
            OPENAI_API_KEY="other",
            OPENAI_CHAT_MODEL_ID="other",
        )
        del os.environ["ANTHROPIC_API_KEY"]
        with self.assertRaisesRegex(ValueError, "ANTHROPIC_API_KEY"):
            LLMConfig.get_available_provider()

    def test_missing_model_is_actionable(self):
        del os.environ["ANTHROPIC_CHAT_MODEL_ID"]
        with self.assertRaisesRegex(ValueError, "ANTHROPIC_CHAT_MODEL_ID"):
            LLMConfig.get_available_provider()

    def test_explicit_unconfigured_provider(self):
        with patch.dict(
            os.environ, {"CO_OP_TRANSLATOR_PROVIDER": "anthropic"}, clear=True
        ):
            with self.assertRaisesRegex(
                ValueError, "ANTHROPIC_API_KEY and ANTHROPIC_CHAT_MODEL_ID"
            ):
                LLMConfig.get_available_provider()

    def test_whitespace_values_are_missing(self):
        os.environ["ANTHROPIC_API_KEY"] = "  "
        with self.assertRaisesRegex(ValueError, "ANTHROPIC_API_KEY"):
            LLMConfig.get_available_provider()

    def test_invalid_provider_is_actionable(self):
        os.environ["CO_OP_TRANSLATOR_PROVIDER"] = "typo"
        with self.assertRaisesRegex(ValueError, "Invalid CO_OP_TRANSLATOR_PROVIDER"):
            LLMConfig.get_available_provider()

    def test_output_budget_is_positive(self):
        self.assertEqual(AnthropicConfig.get_max_tokens(), 8192)
        for value in ["0", "-1", "abc", "1.5", ""]:
            with self.subTest(value=value):
                os.environ["ANTHROPIC_MAX_TOKENS"] = value
                with self.assertRaisesRegex(ValueError, "positive integer"):
                    LLMConfig.get_available_provider()

    def test_explicit_sk_backend_is_rejected(self):
        os.environ["CO_OP_TRANSLATOR_MODEL_CLIENT"] = "semantic-kernel"
        with self.assertRaisesRegex(ValueError, "requires Agent Framework"):
            LLMConfig.get_available_provider()

    def test_image_support_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "images=False"):
            LLMConfig.validate_image_support()

    def test_healthcheck_uses_selected_model_and_closes_client(self):
        with patch.dict(
            "sys.modules",
            {"anthropic": MagicMock(), "agent_framework_anthropic": MagicMock()},
        ):
            from anthropic import Anthropic

            self.assertTrue(LLMConfig.validate_connectivity())
            Anthropic.assert_called_once_with(
                api_key="test-key", timeout=10.0, max_retries=0
            )
            client = Anthropic.return_value.__enter__.return_value
            client.messages.create.assert_called_once_with(
                model="claude-test",
                max_tokens=1,
                messages=[{"role": "user", "content": "Hi"}],
            )
            Anthropic.return_value.__exit__.assert_called_once()

    def test_healthcheck_does_not_leak_error_body(self):
        with patch.dict(
            "sys.modules",
            {"anthropic": MagicMock(), "agent_framework_anthropic": MagicMock()},
        ):
            from anthropic import Anthropic

            client = Anthropic.return_value.__enter__.return_value
            client.messages.create.side_effect = RuntimeError("private-provider-body")
            with self.assertRaisesRegex(
                ValueError, "Anthropic connectivity check failed"
            ) as cm:
                LLMConfig.validate_connectivity()
            self.assertNotIn("private-provider-body", str(cm.exception))

    def test_missing_optional_dependency_has_install_command(self):
        with patch.dict(
            "sys.modules",
            {"agent_framework_anthropic": None, "anthropic": MagicMock()},
        ):
            with self.assertRaisesRegex(ValueError, r"co-op-translator\[anthropic\]"):
                LLMConfig.validate_connectivity()
