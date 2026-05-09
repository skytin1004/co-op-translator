from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class NotebookMarkdownCell:
    ordinal: int
    cell_index: int
    content: str


def read_notebook(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def cell_source_to_text(source: object) -> str:
    if isinstance(source, list):
        return "".join(str(line) for line in source)
    if source is None:
        return ""
    return str(source)


def notebook_markdown_cells(notebook: dict[str, Any]) -> list[NotebookMarkdownCell]:
    cells: list[NotebookMarkdownCell] = []
    for cell_index, cell in enumerate(notebook.get("cells", []), start=1):
        if not isinstance(cell, dict) or cell.get("cell_type") != "markdown":
            continue
        cells.append(
            NotebookMarkdownCell(
                ordinal=len(cells) + 1,
                cell_index=cell_index,
                content=cell_source_to_text(cell.get("source")),
            )
        )
    return cells
