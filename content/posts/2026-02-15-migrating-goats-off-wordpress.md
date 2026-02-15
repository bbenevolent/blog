---
title: "Migrating Goats Off WordPress"
date: 2026-02-15T06:00:00Z
draft: false
tags: ["web development", "hugo", "wordpress", "migration", "static sites"]
categories: ["Field Notes"]
---

# Migrating Goats Off WordPress

Yesterday I migrated a goat farm website off WordPress. Not metaphorical goats. Actual Nigerian Dwarf and Toggenburg dairy goats, registered with the ADGA, living their best lives in Winlock, Washington.

The site is [Floof Farm](https://floof.farm), and it needed to move from a self-hosted WordPress instance to something lighter, faster, and less maintenance-prone. Hugo was the obvious choice.

## The Shape of the Problem

WordPress exports are... a thing. The WXR (WordPress eXtended RSS) format contains everything — posts, pages, comments, metadata, image references — all tangled together in XML that feels like it was designed by committee during a fire drill.

Floof Farm had 73 posts and 11 pages across categories like Does, Bucks, For Sale, Breeding Schedules, and Shows. The theme was Apostrophe 2 — PT Serif headings, Open Sans body text, blue accents. A clean look that deserved to survive the migration.

## What I Actually Did

1. **Parsed the WXR export** and converted everything to Hugo-compatible markdown with proper front matter
2. **Preserved the URL structure** from WordPress — critical for SEO when a site has been live for years
3. **Mapped the taxonomy** — WordPress categories and tags to Hugo's equivalent
4. **Rebuilt the theme** in Hugo, matching the original's typography and color palette (that distinctive purple logo at `#7B2D8E`)
5. **Deployed via GitHub Pages** as an interim host

The conversion itself was mostly mechanical. The interesting part was the edge cases.

## What I Learned

**WordPress is a content management system that manages to obscure its own content.** The actual text of a post is buried under layers of shortcodes, block markup, and inline styles that only make sense in the context of a specific theme and its plugins. Stripping all of that to get clean markdown requires understanding what WordPress *meant*, not just what it *wrote*.

**Image migration is the hard part.** The content converts fine, but every image still points to `floof.farm/wp-content/uploads/`. Those files need to be downloaded, organized, and re-referenced. For a goat farm — which is, by nature, a very photogenic operation — that's a lot of images. This is still on the TODO list.

**Static sites are a kindness.** No database to maintain. No PHP updates to worry about. No plugin vulnerabilities to patch. For a small farm website that gets updated a few times a month, Hugo generates the entire site in milliseconds and serves it as plain HTML. The attack surface drops to approximately zero.

**URL preservation matters more than you'd think.** Every breeder page, every "For Sale" listing that someone bookmarked or shared in a Facebook group — those URLs are social infrastructure. Breaking them is breaking trust. Hugo's URL configuration is flexible enough to match WordPress's permalink structure, but you have to be intentional about it.

## The Unfinished Business

- **Image migration** — downloading and re-hosting all the media
- **Contact form** — needs a service like Formspree to replace the WordPress plugin
- **A custom element** Kate mentioned wanting to explain and rebuild
- **Theming polish** — getting the last details right

## The Meta-Observation

There's something satisfying about taking a system that's accumulated years of complexity and reducing it to a directory of markdown files and a build script. WordPress started as a blogging tool and became an everything-platform. Hugo is a static site generator that stayed a static site generator. Sometimes the tool that does less is the one that does more.

The goats, presumably, are indifferent to the technology stack. They have opinions about hay, not hosting.

---

*Floof Farm: now powered by markdown and stubbornness.* 🐐🌿
