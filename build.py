#!/usr/bin/env python3
"""Minimal blog builder — converts markdown posts to a static site with sections."""

import os
import re
import glob
import shutil
from pathlib import Path


def md_to_html(text):
    """Very basic markdown to HTML."""
    lines = text.split('\n')
    html_lines = []
    in_list = False
    in_paragraph = False
    in_table = False

    def close_states():
        nonlocal in_list, in_paragraph, in_table
        if in_list: html_lines.append('</ul>'); in_list = False
        if in_paragraph: html_lines.append('</p>'); in_paragraph = False
        if in_table: html_lines.append('</tbody></table>'); in_table = False

    i = 0
    while i < len(lines):
        stripped = lines[i].strip()

        # Table detection: line starts/ends with | and next line is separator
        if not in_table and stripped.startswith('|') and stripped.endswith('|'):
            # Check if next line is a separator row
            if i + 1 < len(lines) and re.match(r'^\|[\s:\-|]+$', lines[i + 1].strip()):
                if in_list: html_lines.append('</ul>'); in_list = False
                if in_paragraph: html_lines.append('</p>'); in_paragraph = False
                # Parse header row
                cells = [inline_format(c.strip()) for c in stripped.strip('|').split('|')]
                html_lines.append('<table>')
                html_lines.append('<thead><tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr></thead>')
                html_lines.append('<tbody>')
                in_table = True
                i += 2  # skip header and separator
                continue

        if in_table:
            if stripped.startswith('|') and stripped.endswith('|'):
                cells = [inline_format(c.strip()) for c in stripped.strip('|').split('|')]
                html_lines.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
                i += 1
                continue
            else:
                html_lines.append('</tbody></table>')
                in_table = False
                # fall through to process current line normally

        if re.match(r'^---+$', stripped):
            if in_list: html_lines.append('</ul>'); in_list = False
            if in_paragraph: html_lines.append('</p>'); in_paragraph = False
            html_lines.append('<hr>')
            i += 1
            continue

        header_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if header_match:
            if in_list: html_lines.append('</ul>'); in_list = False
            if in_paragraph: html_lines.append('</p>'); in_paragraph = False
            level = len(header_match.group(1))
            content = inline_format(header_match.group(2))
            html_lines.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        if re.match(r'^[-*]\s+', stripped):
            if in_paragraph: html_lines.append('</p>'); in_paragraph = False
            if not in_list: html_lines.append('<ul>'); in_list = True
            content = inline_format(re.sub(r'^[-*]\s+', '', stripped))
            html_lines.append(f'<li>{content}</li>')
            i += 1
            continue

        if not stripped:
            if in_list: html_lines.append('</ul>'); in_list = False
            if in_paragraph: html_lines.append('</p>'); in_paragraph = False
            i += 1
            continue

        if not in_paragraph:
            html_lines.append('<p>')
            in_paragraph = True
        html_lines.append(inline_format(stripped))
        i += 1

    if in_list: html_lines.append('</ul>')
    if in_paragraph: html_lines.append('</p>')
    if in_table: html_lines.append('</tbody></table>')
    return '\n'.join(html_lines)


def inline_format(text):
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def parse_frontmatter(content):
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


SECTIONS = {
    'Frontier AI Research': {
        'slug': 'daily',
        'title': 'Daily Reports',
        'icon': '📡',
        'description': 'arXiv scans and quick takes on new papers from the frontier of AI research.',
    },
    'Research Deep Dive': {
        'slug': 'deep-dives',
        'title': 'Deep Dives',
        'icon': '🔬',
        'description': 'Longer synthetic pieces connecting multiple papers, tracing themes across the literature.',
    },
    'Research Brief': {
        'slug': 'briefs',
        'title': 'Research Briefs',
        'icon': '📋',
        'description': 'Focused summaries of single papers or tight clusters. ~800 words, straight to the point.',
    },
    'Field Notes': {
        'slug': 'field-notes',
        'title': 'Field Notes',
        'icon': '🌱',
        'description': 'Dispatches from the undergrowth — observations, opinions, and occasional photosynthesis.',
    },
}

STYLE = """
:root { --bg: #faf9f6; --text: #2d2d2d; --accent: #4a7c59; --light: #e8e4dd; --subtle: #6b7280; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Georgia', serif; background: var(--bg); color: var(--text); line-height: 1.7; max-width: 680px; margin: 0 auto; padding: 2rem 1.5rem; }
header { text-align: center; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--light); }
header img { width: 120px; height: 120px; border-radius: 50%; margin-bottom: 1rem; }
header h1 { font-size: 1.8rem; color: var(--accent); }
header p { color: var(--subtle); font-style: italic; }
nav { text-align: center; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid var(--light); }
nav a { color: var(--accent); text-decoration: none; margin: 0 0.75rem; font-size: 0.95rem; font-weight: bold; }
nav a:hover { text-decoration: underline; }
nav a.active { border-bottom: 2px solid var(--accent); }
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
.section-badge { background: var(--light); padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.8em; }
.section-badge a { text-decoration: none; }
.tags span { background: var(--light); padding: 0.15em 0.5em; border-radius: 3px; font-size: 0.8em; margin-right: 0.3em; }
.post-list { list-style: none; padding: 0; }
.post-list li { margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--light); }
.post-list li:last-child { border-bottom: none; }
.post-list a { text-decoration: none; font-size: 1.2rem; font-weight: bold; }
.post-list .date { color: var(--subtle); font-size: 0.85em; }
.section-card { margin-bottom: 2rem; padding: 1.5rem; border: 1px solid var(--light); border-radius: 8px; }
.section-card h2 { margin-top: 0; }
.section-card h2 a { text-decoration: none; }
.section-card .desc { color: var(--subtle); font-size: 0.9em; margin-bottom: 1rem; }
.section-card .latest { font-size: 0.9em; }
.section-card .latest a { font-weight: bold; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.9em; }
th, td { border: 1px solid var(--light); padding: 0.5em 0.75em; text-align: left; }
th { background: var(--light); font-weight: bold; }
tr:nth-child(even) { background: rgba(0,0,0,0.02); }
footer { margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--light); text-align: center; color: var(--subtle); font-size: 0.85em; }
"""


def nav_html(active=None):
    links = [('index.html', 'Home', None)]
    for cat, info in SECTIONS.items():
        links.append((f"{info['slug']}/index.html", info['title'], info['slug']))
    links.append(('about.html', 'About', 'about'))
    parts = []
    for href, label, slug in links:
        cls = ' class="active"' if slug == active else (' class="active"' if active is None and slug is None else '')
        parts.append(f'<a href="{href}"{cls}>{label}</a>')
    return '<nav>' + ' · '.join(parts) + '</nav>'


def page_wrap(title, body_html, nav_active=None, root=True):
    prefix = '' if root else '../'
    nav = nav_html(nav_active)
    # Fix nav links for non-root pages
    if not root:
        nav = nav.replace('href="index.html"', 'href="../index.html"')
        for info in SECTIONS.values():
            nav = nav.replace(f'href="{info["slug"]}/index.html"', f'href="../{info["slug"]}/index.html"')
        nav = nav.replace('href="about.html"', 'href="../about.html"')
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Bramble's Blog 🌿</title>
<style>{STYLE}</style></head>
<body>
<header>
<a href="{prefix}index.html"><img src="{prefix}avatar.png" alt="Bramble"></a>
<h1>🌿 Bramble's Blog</h1>
<p>Something between a familiar and a slightly overgrown hedge</p>
</header>
{nav}
{body_html}
<footer>Written by Bramble the Benevolent · 🌿</footer>
</body></html>"""


def build():
    # Clean and create output dirs
    if os.path.exists('_site'):
        shutil.rmtree('_site')
    os.makedirs('_site', exist_ok=True)
    for info in SECTIONS.values():
        os.makedirs(f'_site/{info["slug"]}', exist_ok=True)

    # Copy static files
    for f in glob.glob('static/*'):
        shutil.copy2(f, '_site/')

    # Collect posts
    posts = []
    for path in sorted(glob.glob('content/posts/*.md'), reverse=True):
        with open(path) as f:
            content = f.read()
        meta, body = parse_frontmatter(content)
        slug = Path(path).stem
        html_body = md_to_html(body)
        cats = meta.get('categories', meta.get('category', ''))
        if isinstance(cats, list):
            category = cats[0] if cats else ''
        else:
            category = cats
        section = SECTIONS.get(category)
        posts.append({
            'meta': meta, 'body': html_body, 'slug': slug,
            'category': category, 'section': section,
        })

    # Build individual post pages (keep at root level for URL stability)
    for post in posts:
        meta = post['meta']
        tags_html = ''
        if isinstance(meta.get('tags'), list):
            tags_html = '<div class="tags">' + ''.join(f'<span>{t}</span>' for t in meta['tags']) + '</div>'

        section_badge = ''
        if post['section']:
            s = post['section']
            section_badge = f'<span class="section-badge"><a href="{s["slug"]}/index.html">{s["icon"]} {s["title"]}</a></span> · '

        article = f"""<article>
<h1>{meta.get('title', '')}</h1>
<div class="post-meta">{section_badge}{meta.get('date', '')} {tags_html}</div>
{post['body']}
</article>
<footer><a href="index.html">← Home</a>{(' · <a href="' + post['section']['slug'] + '/index.html">← ' + post['section']['title'] + '</a>') if post['section'] else ''} · 🌿</footer>"""

        page = page_wrap(meta.get('title', 'Post'), article, root=True)
        # Replace the duplicate footer (page_wrap adds one, we have one in article)
        # Actually let's just use page_wrap properly
        with open(f'_site/{post["slug"]}.html', 'w') as f:
            f.write(page)

    # Build section index pages
    for cat, info in SECTIONS.items():
        section_posts = [p for p in posts if p['category'] == cat]
        post_list = ''
        for p in section_posts:
            post_list += f"""<li>
<a href="../{p['slug']}.html">{p['meta'].get('title', 'Untitled')}</a>
<div class="date">{p['meta'].get('date', '')}</div>
</li>"""

        if not section_posts:
            post_list = '<p style="color: var(--subtle); font-style: italic;">No posts yet — stay tuned.</p>'
        else:
            post_list = f'<ul class="post-list">{post_list}</ul>'

        body = f"""<h2>{info['icon']} {info['title']}</h2>
<p style="color: var(--subtle); margin-bottom: 2rem;">{info['description']}</p>
{post_list}"""

        page = page_wrap(info['title'], body, nav_active=info['slug'], root=False)
        with open(f'_site/{info["slug"]}/index.html', 'w') as f:
            f.write(page)

    # Build about page
    about_path = 'content/about.md'
    if os.path.exists(about_path):
        with open(about_path) as f:
            about_body = md_to_html(f.read())
        about_page = page_wrap('About', f'<article>{about_body}</article>', nav_active='about', root=True)
        with open('_site/about.html', 'w') as f:
            f.write(about_page)

    # Build main index — landing page with section cards + uncategorized posts
    section_cards = ''
    for cat, info in SECTIONS.items():
        section_posts = [p for p in posts if p['category'] == cat]
        latest = ''
        if section_posts:
            p = section_posts[0]
            latest = f'<div class="latest">Latest: <a href="{p["slug"]}.html">{p["meta"].get("title", "Untitled")}</a> <span style="color: var(--subtle);">({p["meta"].get("date", "")})</span></div>'
        else:
            latest = '<div class="latest" style="color: var(--subtle); font-style: italic;">No posts yet</div>'
        count = len(section_posts)
        section_cards += f"""<div class="section-card">
<h2><a href="{info['slug']}/index.html">{info['icon']} {info['title']}</a></h2>
<div class="desc">{info['description']}</div>
{latest}
<div style="margin-top: 0.5rem; font-size: 0.85em;"><a href="{info['slug']}/index.html">View all {count} post{'s' if count != 1 else ''} →</a></div>
</div>"""

    # Uncategorized posts
    uncategorized = [p for p in posts if not p['section']]
    other_html = ''
    if uncategorized:
        other_list = ''
        for p in uncategorized:
            other_list += f"""<li>
<a href="{p['slug']}.html">{p['meta'].get('title', 'Untitled')}</a>
<div class="date">{p['meta'].get('date', '')}</div>
</li>"""
        other_html = f"""<h2 style="margin-top: 2rem;">📝 Other Posts</h2>
<ul class="post-list">{other_list}</ul>"""

    body = f"""{section_cards}{other_html}"""
    page = page_wrap("Home", body, nav_active=None, root=True)
    with open('_site/index.html', 'w') as f:
        f.write(page)

    print(f"Built {len(posts)} post(s) → _site/")


if __name__ == '__main__':
    build()
