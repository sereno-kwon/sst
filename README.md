# Moulton SST WIDE

https://sst.rubiworkshop.com 몰튼 SST 와이드 모델 소개 원페이지. 폴스타 4 쿠페 페이지 구성을 참고하고, 서체 톤은 루비워크샵 메인 히어로 위젯(영문 Pretendard, 한글 에스코어 드림 4)을 따릅니다.

- 언어: 한국어(기본), English, 日本語. 한국어 본문은 HTML에 그대로 들어 있어 자바스크립트 없이도 읽히고, 다른 언어는 상단 버튼으로 바뀝니다.
- 상담 CTA: https://rubiworkshop.com/models
- 도메인: `CNAME` (sst.rubiworkshop.com)

## 이미지

현재 사진은 루비워크샵 룩북 "몰튼 SST 와이드 실버 그레이" 게시물의 이미지를 imweb CDN(`cdn.imweb.me`) 주소로 바로 불러옵니다.

| 위치 | 사진 | 비율 |
|---|---|---|
| 히어로 | 실버그레이 측면 (`55099274198ec`) | 16:9, 모바일 4:3 |
| 첫 문장 옆 | 뒷바퀴, 빌리 봉커 타이어 (`34434da640781`) | 4:5 |
| 핫스팟 | 실버그레이 측면 (`866dd8be3205c`) | 16:10 |
| 프레임 스토리 | 뒤쪽 사선 (`9c36b3e39626f`) | 4:5 |
| 갤러리 1~6 | 스템, 레버와 벨, 그립, 안장, 페달, 림과 타이어 | 3:4 |
| 빌드: 실버그레이 업라이트 | 실버그레이 측면 (`55099274198ec`) | 4:3 |

실버그레이 드롭, 리비에라 블루 드롭 빌드 사진과 헤더 몰튼 로고(`images/moulton-logo.svg`)는 아직 없습니다. 빌드 사진은 `images/build-sg-drop.jpg`, `images/build-rb-drop.jpg`로 넣거나 스크립트 `BUILDS`의 해당 빌드에 `img` 주소를 적으면 됩니다.

사진을 바꾸면 `index.html`의 `<img src>`와 `alt`를 함께 고칩니다. 잘리는 위치는 `style="object-position:..."`으로, 핫스팟 위치는 `.hot` 버튼의 `data-x`, `data-y`(이미지 칸 기준 %)로 조정합니다.

## 검색 최적화

- `index.html` 머리에 대표 주소(canonical), 설명, Open Graph와 트위터 카드, 구조화 데이터(Product, BicycleStore)가 들어 있습니다.
- `sitemap.xml`, `robots.txt`가 루트에 있습니다. 페이지를 크게 고치면 `sitemap.xml`의 `lastmod` 날짜를 바꿔 주세요.
- 네이버 서치어드바이저, 구글 서치 콘솔에 사이트를 등록하고 소유 확인 메타 태그를 `index.html` 머리의 안내 주석 자리에 붙여 넣은 뒤 sitemap.xml을 제출합니다.

## 수정

문구는 `index.html` 하단 스크립트의 `T` (ko / en / ja), 빌드 구성은 `BUILDS` 배열에서 바꿉니다. 한국어 문구를 바꾸면 같은 문구가 HTML 본문에도 들어 있으니 두 곳을 함께 고쳐 주세요.
