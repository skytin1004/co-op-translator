# Frontmatter Field Reference

This document explains how Co-op Translator handles different frontmatter fields during translation.

## Field Categories

Frontmatter fields are handled in three ways:

1. **Preserve**: Never translated, never modified
2. **Translate**: Translated to target language
3. **Preserve + Link Adjust**: Never translated, but file paths are adjusted for translated file location

## Quick Reference Table

| Field | Category | Link Adjust | Description |
|-------|----------|-------------|-------------|
| `title` | Translate | No | Document title |
| `description` | Translate | No | Document description |
| `slug` | Preserve | No | URL slug (technical identifier) |
| `id` | Preserve | No | Unique identifier |
| `order` | Preserve | No | Ordering number |
| `section` | Preserve | No | Section identifier |
| `sidebar_position` | Preserve | No | Sidebar ordering |
| `image` | Preserve | **Yes** | Path to main image |
| `cover` | Preserve | **Yes** | Path to cover image |
| `og_image` | Preserve | **Yes** | Open Graph image path |
| `canonical_url` | Preserve | **Yes** | Canonical URL path |
| `date` | Preserve | No | Publication date |
| `author` | Preserve | No | Author name/ID |
| `tags` | Preserve | No | Technical tags array |

## Detailed Field Behavior

### 1. Preserve Only (No Translation, No Link Adjustment)

These fields are kept exactly as-is in the original:

```yaml
# Technical identifiers
slug: getting-started          # ← Never translated, never adjusted
id: doc-001                    # ← Never translated, never adjusted
section: introduction          # ← Never translated, never adjusted

# Ordering and structure
order: 1                       # ← Never translated, never adjusted
sidebar_position: 2            # ← Never translated, never adjusted
weight: 10                     # ← Never translated, never adjusted

# Metadata
date: 2024-01-15              # ← Never translated, never adjusted
author: john-doe              # ← Never translated, never adjusted
tags: [python, tutorial]      # ← Never translated, never adjusted
categories: [docs, guides]    # ← Never translated, never adjusted

# Publishing control
draft: false                  # ← Never translated, never adjusted
published: true               # ← Never translated, never adjusted

# Layout and template
layout: default               # ← Never translated, never adjusted
template: article             # ← Never translated, never adjusted
type: documentation           # ← Never translated, never adjusted
```

**Why preserve?** These are technical identifiers and configuration values that must remain consistent across all language versions.

### 2. Translate (Translation Only, No Link Adjustment)

These fields contain user-facing text that should be translated:

```yaml
# Original (English)
title: Getting Started
description: Welcome to our documentation
excerpt: Learn how to get started quickly
subtitle: A beginner's guide
tagline: Simple, fast, and powerful

# Translated (Korean)
title: 시작하기
description: 문서에 오신 것을 환영합니다
excerpt: 빠르게 시작하는 방법을 배워보세요
subtitle: 초보자 가이드
tagline: 간단하고, 빠르고, 강력합니다
```

**Full list of translatable fields:**
- `title` - Document title
- `description` - Document description
- `excerpt` - Short excerpt
- `summary` - Summary text
- `abstract` - Abstract text
- `subtitle` - Subtitle
- `tagline` - Tagline
- `caption` - Image/media caption
- `alt` - Alternative text
- `label` - User-facing label
- `placeholder` - Form placeholder text
- `tooltip` - Tooltip text
- `help_text` - Help text
- `error_message` - Error message
- `success_message` - Success message
- `warning_message` - Warning message
- `info_message` - Info message
- `og_title` - Open Graph title
- `og_description` - Open Graph description
- `twitter_title` - Twitter card title
- `twitter_description` - Twitter card description
- `meta_title` - SEO meta title
- `meta_description` - SEO meta description
- `seo_title` - SEO title
- `seo_description` - SEO description

### 3. Preserve + Link Adjust (No Translation, But Paths Are Adjusted)

These fields contain file paths that are preserved but adjusted to point to the correct location from the translated file:

```yaml
# Original file: docs/guide.md
image: ../images/hero.png
cover: ../assets/cover.jpg
og_image: /images/social.png

# Translated file: translations/ko/docs/guide.md
# Paths are adjusted to point to the same files:
image: ../../images/hero.png        # ← Adjusted (added one more ../)
cover: ../../assets/cover.jpg       # ← Adjusted
og_image: /images/social.png        # ← Root-relative, kept as-is
```

**Full list of path fields with link adjustment:**
- `image` - Main image path
- `cover` - Cover image path
- `thumbnail` - Thumbnail image path
- `featured_image` - Featured image path
- `og_image` - Open Graph image path
- `twitter_image` - Twitter card image path
- `icon` - Icon path
- `canonical_url` - Canonical URL path
- `url` - URL path
- `permalink` - Permalink path

**Link adjustment behavior:**

#### Relative Paths
```yaml
# Original: docs/guide.md
image: ../images/hero.png

# Translated: translations/ko/docs/guide.md
image: ../../images/hero.png  # ← One more ../ added
```

#### Root-Relative Paths
```yaml
# Original: docs/guide.md
image: /images/hero.png

# Translated: translations/ko/docs/guide.md
image: /images/hero.png  # ← Kept as-is (root-relative)
```

#### Web URLs
```yaml
# Original
og_image: https://example.com/image.png

# Translated
og_image: https://example.com/image.png  # ← Never modified
```

#### With Image Translation Enabled (`-md -img`)
```yaml
# Original: docs/guide.md
image: ../images/hero.png

# Translated: translations/ko/docs/guide.md
# Points to translated image:
image: ../../translated_images/images_hero_ko.png
```

## Unknown Fields

Fields not listed in the configuration are **preserved by default** for safety:

```yaml
# Not in configuration
custom_field: some_value
my_special_setting: 123

# Result: Preserved (not translated, not adjusted)
custom_field: some_value
my_special_setting: 123
```

**Why preserve unknown fields?** This conservative approach prevents accidental translation or modification of technical fields that we don't recognize.

## Configuration Files

### Preserve/Translate Configuration
Location: `src/co_op_translator/config/frontmatter_config.yml`

```yaml
frontmatter:
  preserve:
    - slug
    - id
    - order
    # ... add more fields here

  translate:
    - title
    - description
    # ... add more fields here
```

### Path Fields Configuration
Location: `src/co_op_translator/utils/llm/frontmatter_utils.py`

```python
PATH_FIELDS = [
    "image",
    "cover",
    "og_image",
    # ... add more path fields here
]
```

## Adding Custom Fields

### To Make a Field Translatable

Edit `src/co_op_translator/config/frontmatter_config.yml`:

```yaml
frontmatter:
  translate:
    - title
    - description
    - my_custom_field  # ← Add here
```

### To Preserve a Field

Edit `src/co_op_translator/config/frontmatter_config.yml`:

```yaml
frontmatter:
  preserve:
    - slug
    - id
    - my_technical_field  # ← Add here
```

### To Enable Link Adjustment for a Field

Edit `src/co_op_translator/utils/llm/frontmatter_utils.py`:

```python
PATH_FIELDS = [
    "image",
    "cover",
    "my_custom_image_field",  # ← Add here
]
```

**Important:** Path fields should also be in the `preserve` list in `frontmatter_config.yml` to prevent translation.

## Examples

### Example 1: Documentation Page

**Original** (`docs/getting-started.md`):
```yaml
---
title: Getting Started
description: Learn how to get started with our platform
slug: getting-started
section: introduction
order: 1
sidebar_position: 1
image: ../images/hero.png
date: 2024-01-15
author: john-doe
tags: [tutorial, beginner]
---
```

**Translated** (`translations/ko/docs/getting-started.md`):
```yaml
---
title: 시작하기                           # ← Translated
description: 플랫폼 시작 방법 알아보기      # ← Translated
slug: getting-started                    # ← Preserved
section: introduction                    # ← Preserved
order: 1                                 # ← Preserved
sidebar_position: 1                      # ← Preserved
image: ../../images/hero.png             # ← Preserved + Link adjusted
date: 2024-01-15                        # ← Preserved
author: john-doe                        # ← Preserved
tags: [tutorial, beginner]              # ← Preserved
---
```

### Example 2: Blog Post

**Original** (`blog/2024/announcement.md`):
```yaml
---
title: New Feature Announcement
description: We're excited to announce our new feature
excerpt: Check out what's new in version 2.0
slug: new-feature-announcement
date: 2024-01-15
author: jane-smith
cover: ../../assets/blog/feature.jpg
og_image: /images/social/announcement.png
canonical_url: /blog/2024/announcement
tags: [announcement, features]
published: true
---
```

**Translated** (`translations/ko/blog/2024/announcement.md`):
```yaml
---
title: 새로운 기능 발표                    # ← Translated
description: 새로운 기능을 발표하게 되어 기쁩니다  # ← Translated
excerpt: 버전 2.0의 새로운 기능을 확인하세요    # ← Translated
slug: new-feature-announcement           # ← Preserved
date: 2024-01-15                        # ← Preserved
author: jane-smith                      # ← Preserved
cover: ../../../../assets/blog/feature.jpg  # ← Preserved + Link adjusted
og_image: /images/social/announcement.png   # ← Preserved (root-relative)
canonical_url: /blog/2024/announcement      # ← Preserved (root-relative)
tags: [announcement, features]          # ← Preserved
published: true                         # ← Preserved
---
```

### Example 3: With Image Translation

**Command:**
```bash
translate -l ko -md -img
```

**Original** (`docs/guide.md`):
```yaml
---
title: User Guide
image: ../images/screenshot.png
---
```

**Translated** (`translations/ko/docs/guide.md`):
```yaml
---
title: 사용자 가이드                      # ← Translated
image: ../../translated_images/images_screenshot_ko.png  # ← Points to translated image
---
```

## Summary

| Category | Behavior | Example Fields |
|----------|----------|----------------|
| **Preserve** | Never translated, never modified | `slug`, `id`, `order`, `section`, `date`, `author`, `tags` |
| **Translate** | Translated to target language | `title`, `description`, `excerpt`, `subtitle` |
| **Preserve + Link Adjust** | Never translated, but paths adjusted | `image`, `cover`, `og_image`, `canonical_url` |
| **Unknown** | Preserved by default (safe fallback) | Any field not in configuration |

**Key Principle:** Technical fields and identifiers are preserved, user-facing text is translated, and file paths are intelligently adjusted to maintain correct references.
