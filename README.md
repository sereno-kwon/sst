# Moulton SST Wide, Korean Edition

sst.moultonbicycles.co.kr 모델 소개 원페이지. 폴스타 4 쿠페 페이지 구성을 참고하고, 서체 톤은 루비워크샵 메인 히어로 위젯(영문 Pretendard, 한글 에스코어 드림 4)을 따릅니다.

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
