# 🧱 Day 4 — 함수(Function)와 모듈화

---

## 🎯 오늘의 목표
- 함수를 정의하고 호출할 수 있다.  
- 입력값(매개변수)과 출력값(반환값)의 개념을 이해한다.  
- 여러 기능을 모듈화해서 코드 구조를 효율적으로 만든다.  

---

## 🧠 1. 함수란?

> 함수(Function)는 “특정 작업을 수행하는 코드 묶음”이에요.  
> 같은 로직을 여러 번 쓸 때 효율적으로 관리하게 해줍니다.

💡 예를 들어 “점수에 따라 합격/불합격을 판단”하는 로직을  
여러 번 작성할 필요 없이, 함수로 정의해두면 언제든 불러서 사용할 수 있습니다.

---

## 🧩 2. 함수 기본 구조

```python
def 함수이름(매개변수):
    실행할 코드
    return 결과값
```

예시 👇
```python
def greet(name):
    return f"Hello, {name}!"
```

호출:
```python
msg = greet("SungHyeon")
print(msg)
```

✅ 출력:
```
Hello, SungHyeon!
```

---

## 🧪 실습 1 — 평균 계산 함수 만들기

```python
def get_average(scores):
    total = sum(scores)
    avg = total / len(scores)
    return avg

numbers = [80, 90, 70]
print("평균 점수:", get_average(numbers))
```

✅ 결과:
```
평균 점수: 80.0
```

💡 **return**은 함수의 결과를 돌려주는 키워드입니다.  
return이 없으면 결과가 저장되지 않고 단순히 실행만 됩니다.

---

## 🧠 3. 매개변수(Parameters)와 인자(Arguments)

| 용어 | 설명 | 예시 |
|------|------|------|
| 매개변수(parameter) | 함수를 정의할 때의 입력값 이름 | `def add(x, y):` |
| 인자(argument) | 함수를 호출할 때 실제 전달하는 값 | `add(3, 5)` |

예시 👇
```python
def add(x, y):
    return x + y

print(add(3, 5))  # 8 출력
```

---

## 🧩 4. 함수의 다양한 형태

### ✅ 매개변수 없는 함수
```python
def hello():
    print("Hello, Data Engineer!")
```

### ✅ 반환값 없는 함수
```python
def show_message(msg):
    print(f"[INFO] {msg}")
```

### ✅ 여러 반환값
```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([5, 9, 3, 7])
print(f"최솟값={low}, 최댓값={high}")
```

✅ 출력:
```
최솟값=3, 최댓값=9
```

---

## 🧪 실습 2 — 합격/불합격 판단 함수

```python
def check_pass(score):
    if score >= 80:
        return "PASS"
    else:
        return "FAIL"

print(check_pass(85))
print(check_pass(72))
```

✅ 결과:
```
PASS
FAIL
```

💡 이런 식의 단일 기능 함수는  
데이터 필터링이나 전처리 로직에서 매우 자주 등장합니다.  
(예: “매출 1000 이상인 행만 남기기” 같은 조건)

---

## 🧩 5. 함수 응용 — 반복문과 함께 쓰기

```python
def check_pass(score):
    return "PASS" if score >= 80 else "FAIL"

scores = [75, 88, 92, 67, 95]
results = []

for s in scores:
    results.append(check_pass(s))

print(results)
```

✅ 결과:
```
['FAIL', 'PASS', 'PASS', 'FAIL', 'PASS']
```

💡 이렇게 하면 반복되는 조건문 로직을 한 줄로 정리할 수 있습니다.

---

## 🧩 6. 모듈화 (파일 분리)

> 코드가 많아지면, 관련된 기능끼리 나눠두는 게 좋습니다.

예시 구조 👇
```
project/
 ├── main.py
 └── utils.py
```

**utils.py**
```python
def check_pass(score):
    return "PASS" if score >= 80 else "FAIL"
```

**main.py**
```python
from utils import check_pass

print(check_pass(85))
```

✅ 실행:
```bash
python main.py
```
결과:
```
PASS
```

💡 이렇게 모듈화를 하면 ETL 단계별 파일(Extract.py / Transform.py / Load.py)을 따로 관리할 수 있게 됩니다.

---

## 🧪 7. 실전 미니 프로젝트 — 학점 자동 평가기

```python
# day4_project.py

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

students = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 72},
    {"name": "C", "score": 93}
]

for s in students:
    grade = get_grade(s["score"])
    print(f"{s['name']}의 학점: {grade}")
```

✅ 실행 결과:
```
A의 학점: B
B의 학점: C
C의 학점: A
```

💡 이 로직은 나중에 ETL Transform 단계에서  
“데이터 변환” 로직으로 그대로 활용됩니다.

---

## 🐳 8. Docker 확장 (선택)

`Dockerfile`
```dockerfile
FROM python:3.10
COPY day4_project.py .
CMD ["python", "day4_project.py"]
```

```bash
docker build -t python-day4 .
docker run python-day4
```

✅ 출력:
```
A의 학점: B
B의 학점: C
C의 학점: A
```

---

## ✅ 오늘의 체크리스트

| 항목 | 완료 여부 |
|------|------------|
| 함수 정의 / 호출 이해 | ☐ |
| 매개변수 & 반환값 구분 | ☐ |
| 함수 + 반복문 결합 실습 | ☐ |
| 모듈 분리(`import`) 성공 | ☐ |
| 학점 평가기 프로젝트 실행 | ☐ |
| Docker 실행 테스트 | ☐ |

---

## 🧭 다음 단계 (Day 5 예고)

> 내일은 “**파일 입출력(File I/O)**”을 배워요.  
>  
> 데이터를 코드 밖(파일)에서 읽고 쓰는 방법을 배우면,  
> **실제 CSV·JSON 파일을 자동으로 다루는 ETL의 첫 단계**가 완성됩니다.  

예고 예시 👇  
```python
with open("data.txt", "w") as f:
    f.write("Hello Data Engineer!")
```

---

✅ **오늘의 미션**
1. `get_grade()` 함수를 직접 만들어보고 학점 기준을 바꿔보기  
2. `utils.py`를 분리해서 모듈화 테스트하기  
3. (선택) Docker로 실행 확인하기  


