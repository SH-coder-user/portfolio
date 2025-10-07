# 🧱 Day 7 — 미니 ETL 프로젝트 (Extract → Transform → Load)

---

## 🎯 오늘의 목표
- 지금까지 배운 모든 개념을 **하나의 ETL 파이프라인**으로 묶는다.  
- CSV 데이터를 읽고(Extract), 변환하고(Transform), 다시 저장(Load)한다.  
- 자동으로 실행 가능한 형태로 구성한다.  

---

## 🧠 1. ETL이란?

| 단계 | 의미 | 예시 |
|------|------|------|
| **Extract** | 외부 데이터 추출 | CSV, JSON, API 읽기 |
| **Transform** | 데이터 변환/정제 | 평균 계산, 필터링, 가공 |
| **Load** | 저장소로 적재 | DB, CSV, 클라우드 등 저장 |

💡 데이터 엔지니어는 이 흐름을 매일 자동으로 실행하는 일을 합니다.  
오늘은 이걸 Python 하나로 구현해볼 거예요 🚀

---

## 🧩 2. 프로젝트 준비

### 폴더 구조
```
day7_etl/
 ├── data/
 │    └── sales.csv
 └── etl_mini.py
```

### `sales.csv` (데이터 예시)
```
product,price,quantity
Laptop,1200,3
Mouse,25,10
Keyboard,55,5
Monitor,300,2
```

---

## 🧪 Step 1. Extract — 데이터 읽기

```python
import pandas as pd

# 1️⃣ CSV 파일 읽기
df = pd.read_csv("data/sales.csv")
print("✅ 데이터 로드 완료:")
print(df.head())
```

✅ 실행 결과:
```
✅ 데이터 로드 완료:
   product  price  quantity
0   Laptop   1200         3
1    Mouse     25        10
2 Keyboard     55         5
3  Monitor    300         2
```

---

## 🧩 Step 2. Transform — 데이터 가공

> 각 상품의 `총 매출(total)`을 계산하고,  
> 총 매출 기준으로 정렬까지 해보겠습니다.

```python
# 2️⃣ 새로운 컬럼 total 계산
df["total"] = df["price"] * df["quantity"]

# 3️⃣ 내림차순 정렬
df = df.sort_values(by="total", ascending=False)

# 4️⃣ 통계 정보
summary = {
    "총 판매건수": len(df),
    "총 매출": df["total"].sum(),
    "평균 단가": df["price"].mean()
}

print("\n✅ 변환 완료:")
print(df)
print("\n📊 요약:", summary)
```

✅ 출력 예시:
```
✅ 변환 완료:
    product  price  quantity  total
0    Laptop   1200         3   3600
3   Monitor    300         2    600
2  Keyboard     55         5    275
1     Mouse     25        10    250

📊 요약: {'총 판매건수': 4, '총 매출': 4725, '평균 단가': 395.0}
```

---

## 🧩 Step 3. Load — 결과 저장

```python
# 5️⃣ 결과 CSV로 저장
df.to_csv("data/sales_summary.csv", index=False)

# 6️⃣ 요약 통계 JSON 저장
import json
with open("data/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("\n✅ ETL 완료! sales_summary.csv 및 summary.json 생성됨.")
```

✅ 생성 파일:
- `sales_summary.csv`  
- `summary.json`

---

### 📄 sales_summary.csv
```
product,price,quantity,total
Laptop,1200,3,3600
Monitor,300,2,600
Keyboard,55,5,275
Mouse,25,10,250
```

### 📄 summary.json
```json
{
  "총 판매건수": 4,
  "총 매출": 4725,
  "평균 단가": 395.0
}
```

---

## 🧪 전체 코드 (etl_mini.py)

```python
import pandas as pd, json, os

# Extract
df = pd.read_csv("data/sales.csv")
print("✅ 데이터 로드 완료")

# Transform
df["total"] = df["price"] * df["quantity"]
df = df.sort_values(by="total", ascending=False)

summary = {
    "총 판매건수": len(df),
    "총 매출": df["total"].sum(),
    "평균 단가": df["price"].mean()
}

# Load
os.makedirs("data", exist_ok=True)
df.to_csv("data/sales_summary.csv", index=False)
with open("data/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ ETL 완료 — 결과 파일 저장 완료!")
```

✅ 실행:
```bash
python etl_mini.py
```

---

## 🧩 4. 확장 아이디어 💡

| 추가 기능 | 설명 |
|------------|------|
| 날짜 자동 추가 | 파일명에 날짜 붙이기 (`f"sales_summary_{today}.csv"`) |
| 에러 처리 | try/except로 파일 유무 확인 |
| 자동화 | 매일 같은 시간 실행 → 나중에 Airflow에서 CronJob으로 전환 |

예시:
```python
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f"data/sales_summary_{today}.csv", index=False)
```

---

## 🐳 5. Docker 확장 (선택)

`Dockerfile`
```dockerfile
FROM python:3.10
COPY . .
RUN pip install pandas
CMD ["python", "etl_mini.py"]
```

빌드 & 실행:
```bash
docker build -t etl-mini .
docker run etl-mini
```

✅ 출력:
```
✅ ETL 완료 — 결과 파일 저장 완료!
```

💡 이렇게 하면 ETL 프로세스를 “컨테이너 단위로 자동 실행”할 수 있습니다.

---

## ✅ 오늘의 체크리스트

| 항목 | 완료 여부 |
|------|------------|
| CSV 데이터 읽기 (Extract) | ☐ |
| 컬럼 계산 / 정렬 (Transform) | ☐ |
| 결과 파일 저장 (Load) | ☐ |
| 전체 ETL 실행 성공 | ☐ |
| summary.json 생성 확인 | ☐ |
| Docker 실행 테스트 | ☐ |

---

## 🧭 다음 단계 (2단계 예고)

> 이제 1단계 Python 기초를 완성했어요 🎉  
>  
> 다음은 **2단계: SQL & Database (PostgreSQL + Docker)** 로 넘어갑니다.  
>  
> - 데이터를 **파일이 아닌 데이터베이스(DB)** 에 저장하고  
> - SQL로 **조회·분석·필터링**하는 법을 배웁니다.  
> - Docker로 PostgreSQL을 설치해서 **로컬 데이터베이스 환경**을 구성할 거예요.

예고 예시 👇
```sql
SELECT product, SUM(total)
FROM sales_summary
GROUP BY product;
```

---

✅ **오늘의 미션**
1. `etl_mini.py` 실행해보기  
2. 데이터나 가격을 바꿔보고 결과 파일이 어떻게 달라지는지 확인  
3. (선택) Docker로 ETL 자동 실행 테스트  

