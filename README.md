# Moulton SST WIDE

sst.rubiworkshop.com 모델 소개 원페이지. 폴스타 4 쿠페 페이지 구성을 참고하고, 서체 톤은 루비워크샵 메인 히어로 위젯(영문 Pretendard, 한글 에스코어 드림 4)을 따릅니다.

- 언어: 한국어, 영어, 일본어 (상단 KO / EN / JA 전환)
- 상담 CTA: https://rubiworkshop.com/models

## 이미지

`images/` 폴더에 아래 이름으로 넣으면 자동으로 표시됩니다. 없으면 회색 판과 선화가 보입니다.

| 파일 | 위치 |
|---|---|
| `moulton-logo.svg` | 헤더 몰튼 로고 |
| `hero.jpg` | 히어로 (16:7, 모바일 4:3) |
| `intro.jpg` | 첫 문장 옆 이미지 (4:3) |
| `design.jpg` | 핫스팟 이미지 (16:9) |
| `frame.jpg` | 프레임 스토리 (3:2) |
| `gallery-1.jpg` ~ `gallery-6.jpg` | 갤러리 (4:3) |
| `build-sg-upright.jpg` | 실버그레이 업라이트 빌드 (4:3) |
| `build-sg-drop.jpg` | 실버그레이 드롭 빌드 (4:3) |
| `build-rb-drop.jpg` | 리비에라 블루 드롭 빌드 (4:3) |

핫스팟 위치는 `index.html`의 `.hot` 버튼 `data-x`, `data-y` 값(이미지 기준 %)으로 조정합니다.

## 수정

문구는 `index.html` 하단 스크립트의 `T` (ko / en / ja), 빌드 구성은 `BUILDS` 배열에서 바꿉니다.

## 검색 최적화

- 문구는 스크립트가 언어별로 넣지만, 검색 로봇용으로 한국어 기본 문구를 HTML에 미리 채워 둡니다. `T.ko` 문구를 고친 뒤 `python3 tools/prerender.py` 를 실행해 주세요.
- `robots.txt`, `sitemap.xml`, 대표 주소(canonical), 구조화 데이터(Product, 프레임 판매가 포함)가 들어 있습니다. 가격을 바꾸면 `<head>`의 JSON-LD `price` 값도 함께 고칩니다.
