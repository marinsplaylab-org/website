#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "index.html"
DATA_PATH = ROOT / "data" / "gallery.json"

START = "<!-- GALLERY:START -->"
END = "<!-- GALLERY:END -->"


def indent(text, spaces):
  pad = " " * spaces
  return "\n".join(f"{pad}{line}" if line else line for line in text.split("\n"))


def render_project(item):
  title = item["title"]
  description = item["description"]
  link = item["link"]
  static_img = item["imageStatic"]
  motion_img = item.get("imageMotion")
  aria_label = item.get("ariaLabel", title)
  source_url = item.get("sourceUrl")
  source_text = item.get("sourceText", source_url)

  lines = [
    f'<div class="gallery-item is-link" data-link="{link}" role="link" aria-label="{aria_label}" tabindex="0">',
    f'  <img',
    f'    class="gallery-media is-static"',
    f'    src="{static_img}"',
    f'    alt="{title} still frame"',
    f'    loading="lazy"',
    f'    decoding="async">'
  ]

  if motion_img:
    lines.extend([
      f'  <img',
      f'    class="gallery-media is-motion"',
      f'    src="{motion_img}"',
      f'    alt=""',
      f'    aria-hidden="true"',
      f'    loading="lazy"',
      f'    decoding="async">'
    ])

  lines.extend([
    f'  <div class="gallery-overlay">',
    f'    <h2 class="gallery-title">{title}</h2>',
    f'    <p class="gallery-desc">{description}</p>'
  ])

  if source_url:
    lines.extend([
      f'    <p class="gallery-desc">',
      f'      <a class="gallery-source" href="{source_url}" target="_blank" rel="noopener noreferrer">',
      f'        {source_text}',
      f'      </a>',
      f'    </p>'
    ])

  lines.extend([
    f'  </div>',
    f'</div>'
  ])

  return "\n".join(lines)


def render_upcoming(item):
  title = item.get("title", "Upcoming Project")
  description = item.get("description", "More updates are on the way.")
  aria_label = item.get("ariaLabel", "Upcoming project")

  return "\n".join([
    f'<div class="gallery-item is-upcoming" role="status" aria-label="{aria_label}">',
    f'  <div class="gallery-overlay">',
    f'    <h2 class="gallery-title">{title}</h2>',
    f'    <p class="gallery-desc">{description}</p>',
    f'  </div>',
    f'</div>'
  ])


def render_empty(item):
  return "\n".join([
    f'<div class="gallery-item is-empty" aria-hidden="true"></div>'
  ])


def render_ghost(item):
  return "\n".join([
    f'<div class="gallery-item is-ghost" aria-hidden="true"></div>'
  ])


def render_items(data):
  rendered = []
  for item in data.get("items", []):
    item_type = item.get("type", "project")
    if item_type == "project":
      rendered.append(render_project(item))
    elif item_type == "upcoming":
      rendered.append(render_upcoming(item))
    elif item_type == "empty":
      rendered.append(render_empty(item))
    elif item_type == "ghost":
      rendered.append(render_ghost(item))
    else:
      raise ValueError(f"Unknown gallery item type: {item_type}")

  return "\n\n".join(rendered)


def main():
  if not DATA_PATH.exists():
    raise SystemExit(f"Missing {DATA_PATH}")

  data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
  html = INDEX_PATH.read_text(encoding="utf-8")

  if START not in html or END not in html:
    raise SystemExit("Gallery markers not found in index.html")

  before, rest = html.split(START, 1)
  _, after = rest.split(END, 1)

  items_html = render_items(data)
  items_html = indent(items_html, 8)

  new_html = f"{before}{START}\n{items_html}\n        {END}{after}"
  INDEX_PATH.write_text(new_html, encoding="utf-8")


if __name__ == "__main__":
  main()
