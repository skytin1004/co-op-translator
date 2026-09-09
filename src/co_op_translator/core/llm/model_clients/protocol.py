from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, TypeVar, runtime_checkable

from pydantic import BaseModel

StructuredResponseT = TypeVar("StructuredResponseT", bound=BaseModel)


@dataclass(frozen=True)
class ModelResponse:
    """Framework-neutral response returned by a translation model client."""

    content: str
    finish_reason: str | None = None
    raw_response: Any = field(default=None, repr=False, compare=False)


@runtime_checkable
class TranslationModelClient(Protocol):
    """Minimal completion boundary used by translation and evaluation flows."""

    async def complete(
        self,
        system_prompt: str,
        user_content: str,
        *,
        temperature: float | None = None,
    ) -> ModelResponse:
        """Complete one system/user prompt pair."""


@runtime_checkable
class StructuredTranslationModelClient(TranslationModelClient, Protocol):
    """Model client that can validate responses against a Pydantic schema."""

    async def complete_structured(
        self,
        system_prompt: str,
        user_content: str,
        response_format: type[StructuredResponseT],
        *,
        temperature: float | None = None,
    ) -> StructuredResponseT:
        """Complete a prompt and return a validated structured response."""
