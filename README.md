# Moulton SST WIDE

https://sst.rubiworkshop.com 몰튼 SST 와이드 모델 소개 원페이지. 폴스타 4 쿠페 페이지 구성을 참고하고, 서체 톤은 루비워크샵 메인 히어로 위젯(영문 Pretendard, 한글 에스코어 드림 4)을 따릅니다.

- 언어: 한국어(기본), English, 日本語. 한국어 본문은 HTML에 그대로 들어 있어 자바스크립트 없이도 읽히고, 다른 언어는 상단 버튼으로 바뀝니다.
- 상담 CTA: https://rubiworkshop.com/models
- 도메인: `CNAME` (sst.rubiworkshop.com)

## 이미지

`images/` 폴더에 아래 이름으로 넣으면 자동으로 표시됩니다. 없으면 회색 판과 선화가 보입니다.

| 파일 | 위치 |
|---|---|
| `moulton-logo.svg` | 헤더 몰튼 로고 |
| `hero.jpg` | 히어로 (16:7, 모바일 4:3). 공유 미리보기와 검색 구조화 데이터 이미지로도 쓰입니다 |
| `intro.jpg` | 첫 문장 옆 이미지 (4:3) |
| `design.jpg` | 핫스팟 이미지 (16:9) |
| `frame.jpg` | 프레임 스토리 (3:2) |
| `gallery-1.jpg` ~ `gallery-6.jpg` | 갤러리 (4:3) |
| `build-sg-upright.jpg` | 실버그레이 업라이트 빌드 (4:3) |
| `build-sg-drop.jpg` | 실버그레이 드롭 빌드 (4:3) |
| `build-rb-drop.jpg` | 리비에라 블루 드롭 빌드 (4:3) |

핫스팟 위치는 `index.html`의 `.hot` 버튼 `data-x`, `data-y` 값(이미지 기준 %)으로 조정합니다.

## 검색 최적화

- `index.html` 머리에 대표 주소(canonical), 설명, Open Graph와 트위터 카드, 구조화 데이터(Product, BicycleStore)가 들어 있습니다.
- `sitemap.xml`, `robots.txt`가 루트에 있습니다. 페이지를 크게 고치면 `sitemap.xml`의 `lastmod` 날짜를 바꿔 주세요.
- 네이버 서치어드바이저, 구글 서치 콘솔에 사이트를 등록하고 소유 확인 메타 태그를 `index.html` 머리의 안내 주석 자리에 붙여 넣은 뒤 sitemap.xml을 제출합니다.

## 수정

문구는 `index.html` 하단 스크립트의 `T` (ko / en / ja), 빌드 구성은 `BUILDS` 배열에서 바꿉니다. 한국어 문구를 바꾸면 같은 문구가 HTML 본문에도 들어 있으니 두 곳을 함께 고쳐 주세요.
