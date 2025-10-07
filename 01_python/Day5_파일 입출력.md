# 🧱 Day 5 — 파일 입출력 (CSV, JSON)

---

## 🎯 오늘의 목표
- 외부 파일을 읽고(`read`) 쓰는(`write`) 방법을 익힌다.  
- CSV / JSON 파일 형식을 이해하고 다룬다.  
- 데이터를 파일로 저장하고 다시 불러오는 과정으로 **ETL의 기초**를 익힌다.  

---

## 🧠 1. 파일 열기와 닫기 (open / close)

> Python은 `open()` 함수로 파일을 열고,  
> `read()` 또는 `write()` 로 내용을 다루며,  
> 마지막엔 `close()` 로 닫습니다.

```python
f = open("hello.txt", "w")  # (파일명, 모드)
f.write("Hello, Data Engineer!\n")
f.close()
```

✅ 실행 결과:  
프로젝트 폴더에 `hello.txt` 파일이 생성되고,  
내용은 이렇게 들어있습니다👇  
```
Hello, Data Engineer!
```

---

## 💡 파일 열기 모드

| 모드 | 설명 |
|------|------|
| `"r"` | 읽기(Read) |
| `"w"` | 쓰기(Write, 기존 내용 덮어씀) |
| `"a"` | 이어쓰기(Append, 기존 내용 뒤에 추가) |

---

## 🧩 2. with문 사용 (파일 자동 닫기)

> `with open()` 구문을 쓰면 파일을 자동으로 닫아줘요.  
> 데이터 엔지니어링에서는 대부분 이렇게 사용합니다.

```python
with open("log.txt", "a") as f:
    f.write("데이터 처리 완료!\n")
```

💡 `"a"` 모드를 쓰면 여러 번 실행해도 내용이 계속 추가됩니다.

---

## 🧪 실습 1 — 텍스트 파일 읽기

```python
with open("hello.txt", "r") as f:
    content = f.read()

print("파일 내용:")
print(content)
```

✅ 출력:
```
파일 내용:
Hello, Data Engineer!
```

---

## 🧠 3. CSV 파일 다루기

> CSV (Comma-Separated Values) 파일은 엑셀처럼 행(Row)과 열(Column)로 구성된 텍스트 형식입니다.

예시 (`data.csv`)
```
name,score
A,85
B,90
C,78
```

---

### 🧪 실습 2 — CSV 쓰기

```python
import csv

data = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 90},
    {"name": "C", "score": 78}
]

with open("data.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(data)
```

✅ 결과:  
`data.csv` 파일 생성

---

### 🧩 CSV 읽기

```python
import csv

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

✅ 출력:
```
{'name': 'A', 'score': '85'}
{'name': 'B', 'score': '90'}
{'name': 'C', 'score': '78'}
```

💡 CSV 파일을 읽으면 각 행이 **딕셔너리(dict)** 형태로 변환됩니다.  
→ ETL의 Transform 단계에서 바로 활용 가능.

---

## 🧠 4. JSON 파일 다루기

> JSON (JavaScript Object Notation)은  
> 웹 API나 클라우드 데이터 전송에 가장 많이 쓰이는 형식입니다.  
> Python의 **딕셔너리(dict)** 와 구조가 거의 같아요.

예시 JSON:
```json
[
  {"name": "A", "score": 85},
  {"name": "B", "score": 90}
]
```

---

### 🧪 실습 3 — JSON 쓰기

```python
import json

data = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 90}
]

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

✅ 결과:  
`data.json` 파일 생성 (예쁘게 들여쓰기된 JSON 형식)

---

### 🧩 JSON 읽기

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
```

✅ 출력:
```
[{'name': 'A', 'score': 85}, {'name': 'B', 'score': 90}]
```

💡 JSON은 웹에서 데이터를 받을 때 필수적으로 쓰이므로  
이 구조에 익숙해지는 게 매우 중요합니다.

---

## 🧪 실습 4 — CSV → JSON 변환기 만들기

> 데이터 엔지니어가 자주 하는 작업 중 하나입니다.

```python
import csv, json

# 1️⃣ CSV 읽기
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# 2️⃣ JSON으로 저장
with open("converted.json", "w") as f:
    json.dump(rows, f, indent=2)

print("✅ CSV → JSON 변환 완료!")
```

✅ 결과:  
`converted.json` 파일 생성  
→ 이제 파일 포맷 변환 자동화 가능 🎉

---

## 🧠 5. 예외 처리 (파일이 없을 때)

> 데이터 파일이 없는 경우에도 프로그램이 멈추지 않게 예외처리를 추가합니다.

```python
try:
    with open("unknown.csv", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("⚠️ 파일을 찾을 수 없습니다.")
```

✅ 출력:
```
⚠️ 파일을 찾을 수 없습니다.
```

💡 ETL 파이프라인에서 “파일 유무 체크” 시 아주 중요합니다.

---

## 🧪 실전 프로젝트 — 파일 기반 점수 요약기

```python
# day5_project.py
import csv, json

students = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 92},
    {"name": "C", "score": 78}
]

# 1️⃣ CSV로 저장
with open("students.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)

# 2️⃣ CSV 읽어서 평균 계산
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    scores = [int(row["score"]) for row in reader]
    avg = sum(scores) / len(scores)

# 3️⃣ 결과를 JSON으로 저장
result = {"average_score": avg}
with open("result.json", "w") as f:
    json.dump(result, f, indent=2)

print("✅ 평균 점수 계산 완료! result.json 파일 확인하세요.")
```

✅ 실행 결과:
```
✅ 평균 점수 계산 완료! result.json 파일 확인하세요.
```

💡 `result.json` 내용:
```json
{
  "average_score": 85.0
}
```

---

## 🐳 6. Docker 확장 (선택)

```dockerfile
FROM python:3.10
COPY day5_project.py .
CMD ["python", "day5_project.py"]
```

```bash
docker build -t python-day5 .
docker run python-day5
```

✅ 결과:
```
✅ 평균 점수 계산 완료! result.json 파일 확인하세요.
```

---

## ✅ 오늘의 체크리스트

| 항목 | 완료 여부 |
|------|------------|
| open / close 이해 | ☐ |
| with문 사용 | ☐ |
| CSV 파일 쓰기/읽기 | ☐ |
| JSON 파일 쓰기/읽기 | ☐ |
| CSV → JSON 변환기 실행 | ☐ |
| 예외 처리(FileNotFoundError) 이해 | ☐ |
| Docker 실행 테스트 | ☐ |

---

## 🧭 다음 단계 (Day 6 예고)

> 내일은 **Pandas**를 사용해서  
> CSV/JSON 데이터를 더 쉽게 다루는 법을 배웁니다.  
>  
> 이제 단순히 “파일을 읽는” 수준이 아니라  
> **데이터를 표 형태로 가공하고 분석하는 능력**을 키울 거예요.

예고 예시 👇  
```python
import pandas as pd
df = pd.read_csv("students.csv")
print(df.describe())
```

---

✅ **오늘의 미션**
1. `students.csv`를 직접 만들어 저장해보기  
2. CSV → JSON 변환기를 수정해 평균점수 외에 최고점/최저점도 포함시키기  
3. (선택) Docker 컨테이너 안에서 실행 테스트  


