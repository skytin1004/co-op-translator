Korean mode: write natural Korean while preserving protected tokens exactly.

Rules (must follow):
1) Preserve placeholders exactly as written, including braces and names:
   {days}, {count}, {{value}}, ${name}, %s, @@INLINE_CODE_x@@, and @@CODE_BLOCK_x@@.
2) Do not omit required Korean particles just because the preceding word is a placeholder,
   product name, acronym, or code-like token.
3) Attach Korean particles after protected tokens when grammar requires them, without changing
   the token itself.
4) If a particle would depend on an unknown placeholder value, prefer a natural Korean phrasing
   that keeps the placeholder unchanged and avoids awkward particle loss.
5) Preserve product names, API names, package names, paths, and command names unless an explicit
   glossary or source text clearly asks otherwise.
6) Keep Markdown links exactly: [text](URL) -> [translated text](same URL).
   Translate only link text; keep Markdown structure and URL unchanged.

Example
Source: Excluding {days}
Correct: {days}를 제외하고
Incorrect: {days} 제외하고

STRUCTURE AND TOKEN FIDELITY ARE MORE IMPORTANT THAN STYLE.
