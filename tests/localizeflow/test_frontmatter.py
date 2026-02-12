import pytest

from co_op_translator.localizeflow.frontmatter import (
    LocalizeflowFrontmatterParser,
    ensure_localizeflow_frontmatter_parser,
)
from co_op_translator.utils.llm.frontmatter_utils import get_frontmatter_parser


def test_ensure_localizeflow_frontmatter_parser_overrides_default():
    parser = ensure_localizeflow_frontmatter_parser()
    assert isinstance(parser, LocalizeflowFrontmatterParser)

    again = get_frontmatter_parser()
    assert again is parser
    assert isinstance(again, LocalizeflowFrontmatterParser)


def test_split_fields_quicklinks_promotes_nested_strings():
    parser = LocalizeflowFrontmatterParser()
    frontmatter = {
        "title": "Getting Started",
        "quickLinks": [
            {
                "slug": "getting-started",
                "title": "Getting Started",
                "description": "Learn the basics",
            },
            {
                "slug": "advanced",
                "title": "Advanced",
                "description": "Go deeper",
            },
        ],
    }

    preserve, translate = parser.split_fields(frontmatter)

    assert "quickLinks" in preserve
    assert preserve["quickLinks"][0]["slug"] == "getting-started"
    assert translate["quickLinks[0].title"] == "Getting Started"
    assert translate["quickLinks[0].description"] == "Learn the basics"
    assert translate["quickLinks[1].title"] == "Advanced"
    assert translate["quickLinks[1].description"] == "Go deeper"


def test_merge_fields_reinserts_quicklinks_translations():
    parser = LocalizeflowFrontmatterParser()
    preserve = {
        "quickLinks": [
            {
                "slug": "getting-started",
                "title": "Getting Started",
                "description": "Learn the basics",
            },
            {
                "slug": "advanced",
                "title": "Advanced",
                "description": "Go deeper",
            },
        ]
    }
    translated = {
        "quickLinks[0].title": "시작하기",
        "quickLinks[0].description": "기본을 배우세요",
        "quickLinks[1].title": "고급",
        "quickLinks[1].description": "더 깊이 탐구하세요",
    }

    merged = parser.merge_fields(preserve, translated)

    assert merged["quickLinks"][0]["title"] == "시작하기"
    assert merged["quickLinks"][0]["description"] == "기본을 배우세요"
    assert merged["quickLinks"][0]["slug"] == "getting-started"
    assert merged["quickLinks"][1]["title"] == "고급"
    assert merged["quickLinks"][1]["description"] == "더 깊이 탐구하세요"
