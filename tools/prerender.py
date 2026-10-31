# -*- coding: utf-8 -*-
"""검색엔진용 한국어 기본 문구 채우기.

index.html의 문구는 스크립트(T.ko / T.en / T.ja)가 언어에 맞춰 넣기 때문에,
자바스크립트를 실행하지 않는 검색 로봇(네이버 Yeti 등)에는 빈 칸으로 보입니다.
이 스크립트는 T.ko 값을 data-i 요소와 사양표(#spec)에 미리 채워 둡니다.
브라우저에서는 기존처럼 스크립트가 언어에 맞게 다시 덮어씁니다.

T.ko 문구를 고친 뒤:  python3 tools/prerender.py
"""
import re, json, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
p = ROOT / 'index.html'
s = p.read_text(encoding='utf-8')

ko_block = re.search(r'\nko:\{\n(.*?)\n\},\nen:\{', s, re.S).group(1)
ko = {k: json.loads('"' + v + '"') for k, v in re.findall(r'(\w+):"((?:[^"\\]|\\.)*)"', ko_block)}
sp = json.loads(re.search(r'\bsp:(\[\[.*?\]\])', ko_block, re.S).group(1))

n = 0
def fill(m):
    global n
    tag, attrs, key = m.group(1), m.group(2), m.group(3)
    if key not in ko:
        return m.group(0)
    n += 1
    return f'<{tag}{attrs}>{html.escape(ko[key], quote=False)}</{tag}>'

# 자식 태그가 없는 data-i 요소만 대상 (스크립트도 textContent로 통째로 바꿈)
s = re.sub(r'<(\w+)([^>]*\bdata-i="(\w+)"[^>]*)>[^<]*</\1>', fill, s)

spec_html = ''.join(f'<div><dt>{html.escape(a, quote=False)}</dt><dd>{html.escape(b, quote=False)}</dd></div>' for a, b in sp)
s = re.sub(r'(<dl class="spec" id="spec">).*?(</dl>)', lambda m: m.group(1) + spec_html + m.group(2), s, count=1, flags=re.S)

p.write_text(s, encoding='utf-8')
print(f'filled {n} data-i elements, {len(sp)} spec rows')
