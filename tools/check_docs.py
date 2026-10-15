"""Fail if a page lacks its other-language twin, or a relative Markdown link is broken."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
errors = []


def twin_of(path: Path):
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if parts[:2] == ("docs", "en"):
        prefix = path.name.split("-")[0]
        match = sorted((ROOT / "docs" / "fr").glob(f"{prefix}-*.md"))
        return match[0] if match else None
    if parts[:2] == ("docs", "fr"):
        prefix = path.name.split("-")[0]
        match = sorted((ROOT / "docs" / "en").glob(f"{prefix}-*.md"))
        return match[0] if match else None
    if path.name.endswith(".fr.md"):
        return path.with_name(path.name[: -len(".fr.md")] + ".md")
    return path.with_name(path.name[: -len(".md")] + ".fr.md")


def is_tracked_doc(path: Path) -> bool:
    return ".github" not in path.parts and "LICENSE" not in path.name


docs = [p for p in ROOT.rglob("*.md") if is_tracked_doc(p)]
for page in docs:
    twin = twin_of(page)
    if twin is None or not twin.exists():
        errors.append(f"{page.relative_to(ROOT)}: no other-language twin")
    text = page.read_text(encoding="utf-8")
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        file_part = target.split("#")[0]
        if file_part and not (page.parent / file_part).resolve().exists():
            errors.append(f"{page.relative_to(ROOT)}: broken link {target}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(docs)} pages, every page has a twin and all relative links resolve")
