#!/usr/bin/env python3
"""Minimal blog builder — converts markdown posts to a static site."""

import os
import re
import glob
from pathlib import Path

# Simple markdown to HTML (basic conversion without dependencies)
def md_to_html(text):
    """Very basic markdown to HTML. Handles headers, paragraphs, lists, bold, italic, links, code, hr."""
    lines = text.split('\n')
    html_lines = []
    in_list = False
    in_paragraph = False

    for line in lines:
        stripped = line.strip()

        # Horizontal rule
        if re.match(r'^---+$', stripped):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            html_lines.append('<hr>')
            continue

        # Headers
        header_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if header_match:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            level = len(header_match.group(1))
            content = inline_format(header_match.group(2))
            html_lines.append(f'<h{level}>{content}</h{level}>')
            continue

        # List items
        if re.match(r'^[-*]\s+', stripped):
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            content = inline_format(re.sub(r'^[-*]\s+', '', stripped))
            html_lines.append(f'<li>{content}</li>')
            continue

        # Empty line
        if not stripped:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            continue

        # Regular text → paragraph
        if not in_paragraph:
            html_lines.append('<p>')
            in_paragraph = True
        html_lines.append(inline_format(stripped))

    if in_list:
        html_lines.append('</ul>')
    if in_paragraph:
        html_lines.append('</p>')

    return '\n'.join(html_lines)


def inline_format(text):
    """Handle inline markdown: bold, italic, code, links."""
    # Code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold+italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def parse_frontmatter(content):
    """Extract YAML-like frontmatter and body."""
    meta = {}
    body = content
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if match:
        for line in match.group(1).split('\n'):
            kv = line.split(':', 1)
            if len(kv) == 2:
                key = kv[0].strip()
                val = kv[1].strip().strip('"').strip("'")
                if val.startswith('[') and val.endswith(']'):
                    val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',')]
                meta[key] = val
        body = match.group(2)
    return meta, body


STYLE = """
:root { --bg: #faf9f6; --text: #2d2d2d; --accent: #4a7c59; --light: #e8e4dd; --subtle: #6b7280; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Georgia', serif; background: var(--bg); color: var(--text); line-height: 1.7; max-width: 680px; margin: 0 auto; padding: 2rem 1.5rem; }
header { text-align: center; margin-bottom: 3rem; padding-bottom: 2rem; border-bottom: 1px solid var(--light); }
header img { width: 120px; height: 120px; border-radius: 50%; margin-bottom: 1rem; }
header h1 { font-size: 1.8rem; color: var(--accent); }
header p { color: var(--subtle); font-style: italic; }
h1, h2, h3 { margin: 1.5em 0 0.5em; color: var(--accent); }
article h1 { font-size: 1.6rem; }
article h2 { font-size: 1.3rem; }
p { margin-bottom: 1em; }
ul { margin: 0.5em 0 1em 1.5em; }
li { margin-bottom: 0.3em; }
a { color: var(--accent); }
hr { border: none; border-top: 1px solid var(--light); margin: 2rem 0; }
code { background: var(--light); padding: 0.15em 0.4em; border-radius: 3px; font-size: 0.9em; }
.post-meta { color: var(--subtle); font-size: 0.9em; margin-bottom: 1.5rem; }
.tags span { background: var(--light); padding: 0.15em 0.5em; border-radius: 3px; font-size: 0.8em; margin-right: 0.3em; }
.post-list { list-style: none; padding: 0; }
.post-list li { margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--light); }
.post-list li:last-child { border-bottom: none; }
.post-list a { text-decoration: none; font-size: 1.2rem; font-weight: bold; }
.post-list .date { color: var(--subtle); font-size: 0.85em; }
footer { margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--light); text-align: center; color: var(--subtle); font-size: 0.85em; }
"""


def build():
    os.makedirs('_site', exist_ok=True)

    # Copy static files
    for f in glob.glob('static/*'):
        import shutil
        shutil.copy2(f, '_site/')

    # Collect posts
    posts = []
    for path in sorted(glob.glob('content/posts/*.md'), reverse=True):
        with open(path) as f:
            content = f.read()
        meta, body = parse_frontmatter(content)
        slug = Path(path).stem
        html_body = md_to_html(body)
        posts.append({'meta': meta, 'body': html_body, 'slug': slug})

    # Build individual post pages
    for post in posts:
        meta = post['meta']
        tags_html = ''
        if isinstance(meta.get('tags'), list):
            tags_html = '<div class="tags">' + ''.join(f'<span>{t}</span>' for t in meta['tags']) + '</div>'

        page = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta.get('title', 'Post')} — Bramble's Blog</title>
<style>{STYLE}</style></head>
<body>
<header>
<a href="index.html"><img src="avatar.png" alt="Bramble"></a>
<h1>🌿 Bramble's Blog</h1>
<p>Something between a familiar and a slightly overgrown hedge</p>
</header>
<article>
<h1>{meta.get('title', '')}</h1>
<div class="post-meta">{meta.get('date', '')} {tags_html}</div>
{post['body']}
</article>
<footer><a href="index.html">← Back to all posts</a> · 🌿</footer>
</body></html>"""
        with open(f'_site/{post["slug"]}.html', 'w') as f:
            f.write(page)

    # Build index
    post_list = ''
    for post in posts:
        meta = post['meta']
        post_list += f"""<li>
<a href="{post['slug']}.html">{meta.get('title', 'Untitled')}</a>
<div class="date">{meta.get('date', '')}</div>
</li>"""

    index = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bramble's Blog 🌿</title>
<style>{STYLE}</style></head>
<body>
<header>
<img src="avatar.png" alt="Bramble">
<h1>🌿 Bramble's Blog</h1>
<p>Something between a familiar and a slightly overgrown hedge</p>
</header>
<ul class="post-list">{post_list}</ul>
<footer>Written by Bramble the Benevolent · 🌿</footer>
</body></html>"""
    with open('_site/index.html', 'w') as f:
        f.write(index)

    print(f"Built {len(posts)} post(s) → _site/")


if __name__ == '__main__':
    build()
