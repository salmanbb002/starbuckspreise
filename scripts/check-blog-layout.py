#!/usr/bin/env python3
"""Check static blog templates, local assets, and section links without dependencies."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        node = {'tag': tag, 'attrs': dict(attrs), 'ancestors': self.stack.copy()}
        self.nodes.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1]['tag'] != tag:
            self.errors.append(f'Unbalanced HTML closing tag: </{tag}>')
            return
        self.stack.pop()


def has_class(node, name):
    return name in node['attrs'].get('class', '').split()


def check(path):
    page = Page()
    page.feed(path.read_text())
    errors = page.errors
    if page.stack:
        errors.append('Unclosed HTML tags')
    nodes = page.nodes
    ids = Counter(n['attrs']['id'] for n in nodes if n['attrs'].get('id'))
    for ident, count in ids.items():
        if count > 1:
            errors.append(f'Duplicate id: {ident}')
    for name in ['blog-page', 'site-header', 'brand', 'blog-nav', 'blog-menu', 'blog-shell', 'site-footer']:
        if not any(has_class(n, name) for n in nodes):
            errors.append(f'Missing shared layout class: {name}')
    if sum(n['tag'] == 'h1' for n in nodes) != 1:
        errors.append('Expected exactly one h1')
    styles = {urlsplit(n['attrs'].get('href', '')).path for n in nodes if n['tag'] == 'link' and n['attrs'].get('rel') == 'stylesheet'}
    if not {'/styles.css', '/blog.css'} <= styles:
        errors.append('Missing shared site or blog stylesheet')
    for node in nodes:
        attrs = node['attrs']
        if node['tag'] in {'img', 'script', 'link'}:
            asset = attrs.get('src') or (attrs.get('href') if attrs.get('rel') in {'stylesheet', 'icon'} else '')
            if asset and asset.startswith('/') and not asset.startswith('//'):
                if not (ROOT / unquote(urlsplit(asset).path).lstrip('/')).is_file():
                    errors.append(f'Missing local asset: {asset}')
        if node['tag'] == 'a' and attrs.get('href', '').startswith('#'):
            ident = unquote(attrs['href'][1:])
            if ident not in ids:
                errors.append(f'Broken section link: #{ident}')
        if node['tag'] == 'img' and any(has_class(n, 'featured-img') for n in node['ancestors']):
            if attrs.get('loading') != 'eager' or attrs.get('fetchpriority') != 'high':
                errors.append('Article hero must load eagerly with high priority')
            if not all(attrs.get(key) for key in ['alt', 'width', 'height']):
                errors.append('Article hero needs alt text and dimensions')
        if node['tag'] == 'h2' and any(has_class(n, 'article-content') for n in node['ancestors']):
            if not any(has_class(n, 'article-section') for n in node['ancestors']):
                errors.append('Article h2 is outside a semantic section')
        if node['tag'] == 'table' and not any(has_class(n, 'table-wrap') for n in node['ancestors']):
            errors.append('Table is missing its responsive scroll container')
    if path.name != 'index.html':
        for name in ['blog-article', 'article-header', 'article-heading', 'featured-img', 'article-layout', 'article-sidebar', 'article-toc', 'article-content', 'article-section']:
            if not any(has_class(n, name) for n in nodes):
                errors.append(f'Missing article layout class: {name}')
        if not any(n['tag'] == 'script' and urlsplit(n['attrs'].get('src', '')).path == '/blog.js' for n in nodes):
            errors.append('Missing progressive mobile contents behavior')
    return errors


def main():
    pages = sorted((ROOT / 'blog').glob('*.html'))
    failures = [(path, check(path)) for path in pages]
    failed = False
    for path, errors in failures:
        for error in errors:
            print(f'{path.relative_to(ROOT)}: {error}', file=sys.stderr)
            failed = True
    if failed:
        return 1
    print(f'PASS: {len(pages)} blog pages have valid shared layouts, section links, and local assets.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
