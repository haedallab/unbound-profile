# ∞ Unbound Profile — Hailey

> 나는 여행과 음악을 사랑하는 금융 전문가. unbound(정의되지 않은 존재)로 자유롭고 유연한 사고를 즐기는 사람.
> AI 툴을 이용하여 각종 재미난 것들을 시도해 보는 시간을 즐긴다. — Hailey

KAIST 디지털금융MBA **클라우드 컴퓨팅 실습** 개인 과제입니다.
개인 소개 페이지(HTML)를 **Vercel**에, FastAPI 백엔드를 **Render**에 배포하고, 프론트엔드에서 백엔드 API를 호출해 결과를 보여줍니다.

## 🔗 배포 주소

| 구분 | 주소 |
|---|---|
| 프론트엔드 (Vercel) | https://unbound-profile.vercel.app |
| 백엔드 API (Render) | https://unbound-profile-backend.onrender.com |
| Swagger UI | https://unbound-profile-backend.onrender.com/docs |
| GitHub | https://github.com/haedallab/unbound-profile |

## 🧱 주요 구성

```
unbound-profile/
├── frontend/
│   └── index.html        # 개인 소개 + 연동 실습 (한 페이지 구성)
├── backend/
│   ├── main.py           # FastAPI 앱
│   └── requirements.txt
└── README.md
```

- **Frontend** — 순수 HTML/CSS/JavaScript. `fetch()`로 백엔드 API 호출, 결과를 JSON과 화면에 표시
- **Backend** — FastAPI + Uvicorn, CORS 허용

### API 목록

| Method | Endpoint | 설명 |
|---|---|---|
| GET | `/` | 서버 상태 확인 |
| GET | `/api/profile` | 개인 소개 정보 |
| GET | `/api/hello?name=` | 인사 메시지 + 서버 시간 |
| GET | `/api/compound?principal=&rate=&years=` | 연복리 계산 (연도별 평가금액) |

## 🚀 배포 방법

**Render (백엔드)** — New → Web Service → 이 저장소 연결
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Instance Type: Free

**Vercel (프론트엔드)** — Add New → Project → 이 저장소 Import
- Root Directory: `frontend`, Framework Preset: Other

## 💻 로컬 실행

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# http://127.0.0.1:8000/docs
```

## 📝 참고
- Render 무료 플랜은 일정 시간 미사용 시 슬립 상태가 되어 첫 호출에 30~60초가 걸릴 수 있습니다.
- 개인 소개 페이지는 AI(Claude)의 도움을 받아 작성했습니다.
