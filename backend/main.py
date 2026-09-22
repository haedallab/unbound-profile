from datetime import datetime, timezone

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Unbound Profile API",
    description="Hailey의 개인 소개 페이지와 연동되는 FastAPI 백엔드 (KAIST 클라우드 컴퓨팅 실습)",
    version="1.0.0",
)

# Vercel 프론트엔드에서 호출할 수 있도록 CORS 허용 (실습용: 전체 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PROFILE = {
    "name": "Hailey",
    "title": "Unbound — 정의되지 않은 존재",
    "summary": "여행과 음악을 사랑하는 금융 전문가. 자유롭고 유연한 사고를 즐기며, "
               "AI 툴로 재미난 것들을 시도해 보는 시간을 즐긴다.",
    "keywords": ["Finance", "Travel", "Music", "AI Tools", "Free Thinking"],
}


@app.get("/", tags=["Health"])
def root():
    """서버 상태 확인"""
    return {"status": "ok", "message": "Unbound Profile API is running", "docs": "/docs"}


@app.get("/api/profile", tags=["Profile"])
def get_profile():
    """개인 소개 정보 반환"""
    return PROFILE


@app.get("/api/hello", tags=["Demo"])
def hello(name: str = Query("Guest", description="인사할 이름")):
    """이름을 받아 인사 메시지와 서버 시간을 반환"""
    return {
        "message": f"안녕하세요, {name}님! Unbound 백엔드에서 인사드립니다 👋",
        "server_time_utc": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/compound", tags=["Finance"])
def compound_interest(
    principal: float = Query(10_000_000, gt=0, description="원금 (원)"),
    rate: float = Query(5.0, ge=0, le=100, description="연 수익률 (%)"),
    years: int = Query(10, ge=1, le=50, description="투자 기간 (년)"),
):
    """연복리 계산: 원금 × (1 + r)^n"""
    r = rate / 100
    yearly = [
        {"year": y, "value": round(principal * (1 + r) ** y)}
        for y in range(0, years + 1)
    ]
    final = yearly[-1]["value"]
    return {
        "principal": principal,
        "rate_pct": rate,
        "years": years,
        "final_value": final,
        "total_return_pct": round((final / principal - 1) * 100, 2),
        "yearly": yearly,
    }
