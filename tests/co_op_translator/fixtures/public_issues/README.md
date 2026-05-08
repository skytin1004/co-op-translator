# Public Issue Regression Fixtures

These fixtures capture small Markdown samples derived from public
Co-op Translator issues. Each case has:

- `source.md`: minimal source content that represents the original pattern.
- `problem.<lang>.md`: the observed or reported bad translation shape.
- `expected.<lang>.md`: the desired stable output shape.

The registry maps each sample to the public issue URL and records known-bad
markers that should not appear in expected output. Keep samples small so they
can be reused by deterministic review tests and LLM-mocked integration tests.
