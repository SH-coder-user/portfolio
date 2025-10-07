# 🧱 Day 6 — Pandas로 데이터 분석 기초

---

## 🎯 오늘의 목표
- Pandas의 기본 개념과 `DataFrame` 구조를 이해한다.  
- CSV/JSON 파일을 Pandas로 읽고 가공한다.  
- 필터링, 정렬, 컬럼 계산 등 기본 데이터 처리 연습을 한다.  

---

## 🧠 1. Pandas란?

> Pandas는 Python에서 데이터를 **표(행·열)** 형태로 다루는 라이브러리입니다.  
> 데이터 분석과 ETL(데이터 변환)의 “핵심 도구”예요.

설치 (처음 한 번만)
```bash
pip install pandas
```

---

## 🧩 2. DataFrame 기본 구조

```python
import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "score": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)
```

✅ 결과:
```
  name  score
0    A     85
1    B     90
2    C     78
```

💡 각 행(Row)은 하나의 데이터,  
각 열(Column)은 속성(필드)입니다.

---

## 🧩 3. CSV 파일 읽기 & 쓰기

### 📘 CSV 읽기
```python
df = pd.read_csv("students.csv")
print(df)
```

### 📘 CSV 저장하기
```python
df.to_csv("students_copy.csv", index=False)
```

💡 `index=False` 는 행 번호(0,1,2...)를 저장하지 않겠다는 의미입니다.

---

## 🧩 4. 기본 통계 확인 (`describe()`)

> 데이터의 기본적인 통계 요약을 한눈에 확인할 수 있습니다.

```python
print(df.describe())
```

✅ 출력:
```
          score
count   3.000000
mean   84.333333
std     6.110100
min    78.000000
max    90.000000
```

💡 count(갯수), mean(평균), min/max(최솟값·최댓값) 등 자동 계산됩니다.  
→ 데이터 품질 점검에 매우 유용합니다.

---

## 🧪 실습 1 — 새로운 컬럼 추가

```python
df["grade"] = ["B", "A", "C"]
print(df)
```

✅ 출력:
```
  name  score grade
0    A     85     B
1    B     90     A
2    C     78     C
```

💡 컬럼을 추가하면 자동으로 DataFrame에 새로운 열이 생깁니다.

---

## 🧠 5. 조건 필터링

> 조건에 맞는 행만 선택할 수 있습니다.

```python
passed = df[df["score"] >= 80]
print(passed)
```

✅ 결과:
```
  name  score grade
0    A     85     B
1    B     90     A
```

💡 Pandas에서는 **SQL의 WHERE절**처럼 데이터를 필터링할 수 있습니다.

---

## 🧪 실습 2 — 평균 점수보다 높은 학생만 추출

```python
avg = df["score"].mean()
print("평균:", avg)

above_avg = df[df["score"] > avg]
print("평균 이상 학생:")
print(above_avg)
```

✅ 출력:
```
평균: 84.33
평균 이상 학생:
  name  score grade
0    A     85     B
1    B     90     A
```

---

## 🧠 6. 정렬(Sort)

```python
sorted_df = df.sort_values(by="score", ascending=False)
print(sorted_df)
```

✅ 출력:
```
  name  score grade
1    B     90     A
0    A     85     B
2    C     78     C
```

💡 `ascending=False` → 내림차순  
`True` 로 바꾸면 오름차순 정렬

---

## 🧩 7. apply()로 데이터 변환하기

> 각 행이나 열에 함수를 적용할 수 있는 기능  
> ETL의 “Transform” 단계에서 아주 자주 사용됩니다.

```python
def grade_by_score(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    else:
        return "C"

df["grade"] = df["score"].apply(grade_by_score)
print(df)
```

✅ 출력:
```
  name  score grade
0    A     85     B
1    B     90     A
2    C     78     C
```

💡 `apply()`는 데이터 한 행(row)을 반복문 없이 처리하게 해줍니다.  
→ 실제 대규모 데이터에도 매우 빠르게 동작합니다.

---

## 🧪 실습 3 — CSV 파일로 저장

```python
df.to_csv("students_result.csv", index=False)
print("✅ students_result.csv 저장 완료!")
```

---

## 🧠 8. JSON 데이터 읽기

```python
df_json = pd.read_json("data.json")
print(df_json)
```

✅ 출력 (예시):
```
  name  score
0    A     85
1    B     90
```

💡 CSV, JSON, Excel 등 거의 모든 형식을 Pandas로 처리할 수 있습니다.  
→ 이후 AWS S3, API 데이터까지 동일한 원리로 확장됩니다.

---

## 🧪 실습 4 — 요약 리포트 자동 생성

```python
import pandas as pd

df = pd.read_csv("students.csv")
avg = df["score"].mean()
max_score = df["score"].max()
min_score = df["score"].min()

summary = {
    "average": avg,
    "max": max_score,
    "min": min_score
}

report = pd.DataFrame([summary])
report.to_csv("summary_report.csv", index=False)
print("✅ 요약 리포트 생성 완료!")
```

✅ 결과:
```
✅ 요약 리포트 생성 완료!
```

💡 `summary_report.csv` 파일 예시:
```
average,max,min
84.33,90,78
```

---

## 🐳 9. Docker 확장 (선택)

```dockerfile
FROM python:3.10
COPY day6_project.py .
RUN pip install pandas
CMD ["python", "day6_project.py"]
```

```bash
docker build -t python-day6 .
docker run python-day6
```

✅ 결과:
```
✅ 요약 리포트 생성 완료!
```

---

## ✅ 오늘의 체크리스트

| 항목 | 완료 여부 |
|------|------------|
| Pandas 설치 및 실행 | ☐ |
| DataFrame 생성 | ☐ |
| CSV 읽기/쓰기 | ☐ |
| 조건 필터링 | ☐ |
| 정렬 / apply() 실습 | ☐ |
| 요약 리포트 프로젝트 실행 | ☐ |
| Docker 실행 테스트 | ☐ |

---

## 🧭 다음 단계 (Day 7 예고)

> 내일은 **미니 ETL 프로젝트**로  
> 지금까지 배운 모든 개념을 연결해볼 거예요.  
>  
> **Extract (CSV 읽기) → Transform (Pandas로 계산) → Load (CSV 저장)**  
> 이 과정을 자동으로 처리하는 **실전 파이프라인 코드**를 만들어볼 겁니다.  

예고 예시 👇
```python
import pandas as pd

df = pd.read_csv("sales.csv")
df["total"] = df["price"] * df["quantity"]
df.to_csv("sales_summary.csv", index=False)
```

---

✅ **오늘의 미션**
1. `students.csv` 파일을 만들어 Pandas로 불러오기  
2. 평균/최고/최저 점수 계산 후 CSV로 저장하기  
3. `apply()` 함수를 활용해 성적 등급 자동 계산해보기  

