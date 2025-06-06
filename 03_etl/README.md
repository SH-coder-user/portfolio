# 🧪 ETL 실습 모음

## ✅ 목표
- Open API에서 데이터를 가져와 전처리하고, DB에 저장하는 ETL 파이프라인 구성

## 📁 파일 설명

| 파일명 | 설명 |
|--------|------|
| weather_etl.py | 기상청 날씨 API → Pandas로 정제 → SQLite 저장 |
| transform_movie_data.py | 영화 랭킹 데이터 정제 및 컬럼 변환 예제 |

## 🔄 흐름
1. `requests`로 API 호출
2. `Pandas`로 데이터 프레임 생성
3. 불필요한 컬럼 제거 및 변환
4. SQLite에 저장
