#!/usr/bin/env python3
import argparse
import datetime as dt
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen

BASE_URL = "https://vega.github.io/vega-lite/"

CATEGORIES = {
    "intro-and-embed.md": [
        "docs/index.html",
        "tutorials/getting_started.html",
        "usage/embed.html",
        "ecosystem.html",
    ],
    "spec-core.md": [
        "docs/spec.html",
        "docs/data.html",
        "docs/mark.html",
        "docs/config.html",
        "docs/invalid-data.html",
    ],
    "encoding-and-fields.md": [
        "docs/encoding.html",
        "docs/field.html",
        "docs/type.html",
        "docs/types.html",
        "docs/datum.html",
        "docs/value.html",
        "docs/condition.html",
        "docs/sort.html",
        "docs/stack.html",
        "docs/bandposition.html",
        "docs/size.html",
        "docs/datetime.html",
    ],
    "presentation.md": [
        "docs/axis.html",
        "docs/legend.html",
        "docs/scale.html",
        "docs/format.html",
        "docs/gradient.html",
        "docs/header.html",
        "docs/title.html",
        "docs/tooltip.html",
    ],
    "marks.md": [
        "docs/mark.html",
        "docs/area.html",
        "docs/bar.html",
        "docs/line.html",
        "docs/point.html",
        "docs/circle.html",
        "docs/square.html",
        "docs/rect.html",
        "docs/tick.html",
        "docs/rule.html",
        "docs/text.html",
        "docs/trail.html",
        "docs/image.html",
        "docs/arc.html",
        "docs/boxplot.html",
        "docs/errorband.html",
        "docs/errorbar.html",
        "docs/geoshape.html",
    ],
    "transforms.md": [
        "docs/transform.html",
        "docs/calculate.html",
        "docs/filter.html",
        "docs/aggregate.html",
        "docs/joinaggregate.html",
        "docs/window.html",
        "docs/bin.html",
        "docs/timeunit.html",
        "docs/density.html",
        "docs/regression.html",
        "docs/loess.html",
        "docs/quantile.html",
        "docs/sample.html",
        "docs/lookup.html",
        "docs/fold.html",
        "docs/flatten.html",
        "docs/pivot.html",
        "docs/impute.html",
        "docs/extent.html",
    ],
    "composition.md": [
        "docs/composition.html",
        "docs/layer.html",
        "docs/facet.html",
        "docs/concat.html",
        "docs/repeat.html",
        "docs/resolve.html",
    ],
    "interaction-params.md": [
        "docs/parameter.html",
        "docs/param-value.html",
        "docs/selection.html",
        "docs/bind.html",
        "docs/predicate.html",
    ],
    "geo.md": [
        "docs/projection.html",
    ],
}


class MarkdownExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.in_pre = False
        self.inline_code = False
        self.skip_depth = 0
        self.in_table = False
        self.table_rows = []
        self.current_row = None
        self.current_cell = None
        self.link_href = None

    def handle_starttag(self, tag, attrs):
        if self.skip_depth > 0:
            self.skip_depth += 1
            return
        attrs_map = dict(attrs)
        if tag in {"script", "style"}:
            self.skip_depth = 1
            return
        if tag == "span" and "class" in attrs_map:
            if "edit-page" in attrs_map["class"].split():
                self.skip_depth = 1
                return
        if self.in_table and tag not in {"table", "tr", "th", "td"}:
            return
        if tag == "table":
            self.in_table = True
            self.table_rows = []
            return
        if tag == "tr" and self.in_table:
            self.current_row = []
            return
        if tag in {"th", "td"} and self.in_table:
            self.current_cell = []
            return

        if tag == "pre":
            self.in_pre = True
            self.out.append("\n```\n")
        elif tag == "code":
            if not self.in_pre:
                self.inline_code = True
                self.out.append("`")
        elif tag in {"h1", "h2", "h3", "h4"}:
            level = {"h1": 1, "h2": 2, "h3": 3, "h4": 4}[tag]
            self.out.append("\n" + ("#" * level) + " ")
        elif tag == "p":
            self.out.append("\n")
        elif tag == "br":
            self.out.append("\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "a":
            self.link_href = attrs_map.get("href")

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        text = data
        if self.in_table and self.current_cell is not None:
            self.current_cell.append(text)
            return
        if self.in_pre:
            self.out.append(text)
            return
        cleaned = re.sub(r"\s+", " ", text)
        if cleaned:
            self.out.append(cleaned)

    def handle_endtag(self, tag):
        if self.skip_depth > 0:
            self.skip_depth -= 1
            return
        if tag == "table" and self.in_table:
            table_md = self._table_to_markdown()
            if table_md:
                self.out.append("\n" + table_md + "\n")
            self.in_table = False
            self.table_rows = []
            return
        if tag == "tr" and self.in_table:
            if self.current_row is not None:
                self.table_rows.append(self.current_row)
            self.current_row = None
            return
        if tag in {"th", "td"} and self.in_table:
            if self.current_cell is None:
                return
            cell_text = " ".join(self.current_cell)
            cell_text = re.sub(r"\s+", " ", cell_text).strip()
            self.current_row.append(cell_text)
            self.current_cell = None
            return

        if tag == "pre":
            self.in_pre = False
            self.out.append("\n```\n")
        elif tag == "code":
            if self.inline_code:
                self.out.append("`")
                self.inline_code = False
        elif tag == "a":
            if self.link_href:
                self.out.append(f" ({self.link_href})")
            self.link_href = None

    def _table_to_markdown(self):
        if not self.table_rows:
            return ""
        header = self.table_rows[0]
        if not header:
            return ""
        col_count = len(header)
        lines = []
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"] * col_count) + " |")
        for row in self.table_rows[1:]:
            padded = row + [""] * (col_count - len(row))
            lines.append("| " + " | ".join(padded[:col_count]) + " |")
        return "\n".join(lines)

    def get_markdown(self):
        text = "".join(self.out)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


class PageContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.capture = False
        self.capture_depth = 0
        self.chunks = []
        self.found = False

    def handle_starttag(self, tag, attrs):
        attrs_map = dict(attrs)
        classes = attrs_map.get("class", "")
        if not self.capture and "page-content" in classes.split():
            self.capture = True
            self.capture_depth = 1
            self.found = True
            self.chunks.append(self._format_starttag(tag, attrs_map))
            return
        if self.capture:
            self.capture_depth += 1
            self.chunks.append(self._format_starttag(tag, attrs_map))

    def handle_endtag(self, tag):
        if not self.capture:
            return
        self.chunks.append(f"</{tag}>")
        self.capture_depth -= 1
        if self.capture_depth <= 0:
            self.capture = False

    def handle_data(self, data):
        if self.capture:
            self.chunks.append(data)

    def handle_startendtag(self, tag, attrs):
        if self.capture:
            attrs_map = dict(attrs)
            self.chunks.append(self._format_starttag(tag, attrs_map, self_closing=True))

    def _format_starttag(self, tag, attrs, self_closing=False):
        if attrs:
            attr_str = " ".join(
                f'{k}="{str(v).replace(chr(34), "&quot;")}"' for k, v in attrs.items()
            )
            if self_closing:
                return f"<{tag} {attr_str} />"
            return f"<{tag} {attr_str}>"
        if self_closing:
            return f"<{tag} />"
        return f"<{tag}>"

    def get_html(self):
        return "".join(self.chunks)


def fetch_html(url):
    with urlopen(url) as resp:
        return resp.read().decode("utf-8")


def extract_page_markdown(url):
    html = fetch_html(url)
    match = re.search(r'<section class="page-content">(.*?)</section>', html, re.S)
    if match:
        content = match.group(1)
    else:
        extractor = PageContentExtractor()
        extractor.feed(html)
        if not extractor.found:
            raise RuntimeError(f"Could not find page content for {url}")
        content = extractor.get_html()
    content = re.sub(r'<span class="edit-page">.*?</span>', "", content, flags=re.S)
    parser = MarkdownExtractor()
    parser.feed(content)
    md = parser.get_markdown()
    lines = md.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    title = None
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i][2:].strip()
        lines = lines[:i] + lines[i + 1 :]
    md = "\n".join(lines).strip()
    return title or "Untitled", md


def ascii_clean(text):
    text = unicodedata.normalize("NFKD", text)
    return text.encode("ascii", "ignore").decode("ascii")


def write_category(out_dir, filename, paths):
    out_path = out_dir / filename
    parts = []
    parts.append(f"# {filename.replace('-', ' ').replace('.md', '').title()}\n")
    parts.append(f"Generated from {BASE_URL} on {dt.date.today().isoformat()}.\n")
    for path in paths:
        url = urljoin(BASE_URL, path)
        title, md = extract_page_markdown(url)
        parts.append(f"## {title}")
        parts.append(f"Source: {url}\n")
        if md:
            parts.append(md)
        parts.append("")
    content = "\n".join(parts)
    out_path.write_text(ascii_clean(content) + "\n", encoding="utf-8")
    return out_path


def main(argv):
    parser = argparse.ArgumentParser(
        description="Fetch Vega-Lite docs and write grouped markdown references."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory (defaults to ../references relative to this script).",
    )
    args = parser.parse_args(argv)

    if args.out:
        out_dir = Path(args.out).expanduser().resolve()
    else:
        out_dir = Path(__file__).resolve().parent.parent / "references"
    out_dir.mkdir(parents=True, exist_ok=True)

    for filename, paths in CATEGORIES.items():
        write_category(out_dir, filename, paths)
        print(f"Wrote {filename}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
