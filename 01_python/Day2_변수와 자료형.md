# 🧱 Day 2 — 변수와 자료형 (Variables & Data Types)

---

## 🎯 오늘의 목표
- 데이터를 저장하는 **변수(Variable)** 개념 이해  
- Python의 **기본 자료형(Data Type)** 익히기  
- 숫자, 문자열, 리스트, 딕셔너리 다루기  

---

## 🧠 1. 변수란?

> 변수가 바로 “데이터를 담는 상자”예요 🎁

- 한 번 정의하면 이름으로 불러 쓸 수 있음  
- 데이터를 재사용하거나 가공할 때 필수  

```python
name = "SungHyeon"
age = 28
```

➡️ “이름(name)”과 “나이(age)”라는 **라벨(Label)**을 붙여 값을 저장한 것  

---

## 🧩 2. 기본 자료형 4가지

| 자료형 | 예시 | 설명 | 자주 쓰는 예 |
|---------|------|------|---------------|
| `int` | 10 | 정수 (integer) | 개수, ID 등 |
| `float` | 3.14 | 실수 (소수점 포함) | 평균, 온도 등 |
| `str` | "hello" | 문자열 (string) | 이름, 메시지 등 |
| `bool` | True / False | 논리값 | 조건 판별 |

---

## 🧪 실습 1: 기본 자료형 출력하기

```python
# day2_basic.py

# 변수 정의
name = "SungHyeon"
age = 28
height = 176.5
is_student = True

# 출력
print("이름:", name)
print("나이:", age)
print("키:", height)
print("학생 여부:", is_student)
```

✅ 실행 결과
```
이름: SungHyeon
나이: 28
키: 176.5
학생 여부: True
```

💡 **포인트**
- Python은 자동으로 자료형을 인식한다.  
- `type()` 함수로 확인할 수 있음 👇  

```python
print(type(name))  # <class 'str'>
```

---

## 🧩 3. 문자열(String) 조합하기

문자열은 단순한 글자가 아니라 **데이터 로깅이나 메시지 구성**에 자주 쓰입니다.

```python
project = "ETL Pipeline"
print("현재 프로젝트:", project)

# 문자열 결합
msg = "Hello " + name + "! Let's start " + project
print(msg)
```

✅ 실행 결과
```
현재 프로젝트: ETL Pipeline
Hello SungHyeon! Let's start ETL Pipeline
```

💡 더 깔끔하게는 f-string 사용:
```python
print(f"Hello {name}! Let's start {project}")
```

---

## 🧩 4. 숫자 계산하기 (int, float)

데이터 엔지니어는 수치 계산을 자주 하게 됩니다.  

```python
# 점수 계산 예시
score_math = 85
score_eng = 92
average = (score_math + score_eng) / 2

print(f"평균 점수: {average}")
```

✅ 출력:
```
평균 점수: 88.5
```

💡 `/`는 **나누기 연산자**, 결과는 항상 `float`형으로 나옵니다.

---

## 🧩 5. 리스트(List)

> 여러 데이터를 한꺼번에 저장할 때 사용 (데이터 행 모음처럼)

```python
scores = [85, 90, 78, 92]
print(scores)
print("첫 번째 점수:", scores[0])
print("평균:", sum(scores) / len(scores))
```

✅ 출력:
```
[85, 90, 78, 92]
첫 번째 점수: 85
평균: 86.25
```

💡 리스트는 데이터의 "한 줄" 또는 "여러 행"을 저장할 때 자주 쓰임.  
→ 나중에 Pandas `DataFrame`의 기반 구조가 됩니다.

---

## 🧩 6. 딕셔너리(Dictionary)

> “키(key) - 값(value)” 쌍으로 데이터 저장

```python
student = {
    "name": "SungHyeon",
    "age": 28,
    "scores": [85, 90, 78]
}

print(student["name"])
print("평균:", sum(student["scores"]) / len(student["scores"]))
```

✅ 출력:
```
SungHyeon
평균: 84.33
```

💡 딕셔너리는 **JSON 구조**와 동일한 형태  
→ 나중에 ETL에서 API 응답(JSON)을 다룰 때 핵심적으로 사용됨.

---

## 🧠 7. 자료형 변환(Type Casting)

```python
x = "10"
y = int(x)  # 문자열 → 정수
print(y + 5)
```

✅ 출력:
```
15
```

💡 변환 함수
| 변환 함수 | 설명 |
|------------|------|
| `int()` | 정수로 변환 |
| `float()` | 실수로 변환 |
| `str()` | 문자열로 변환 |
| `bool()` | 논리값으로 변환 |

---

## 🧩 8. 실습 프로젝트 — 데이터 통계 출력기

하나의 미니 예제로 마무리해볼게요 👇  

```python
# day2_project.py

user = {
    "name": "SungHyeon",
    "scores": [75, 88, 92, 67, 95]
}

avg = sum(user["scores"]) / len(user["scores"])
max_score = max(user["scores"])
min_score = min(user["scores"])

print(f"사용자: {user['name']}")
print(f"평균 점수: {avg:.2f}")
print(f"최고 점수: {max_score}, 최저 점수: {min_score}")
```

✅ 결과:
```
사용자: SungHyeon
평균 점수: 83.40
최고 점수: 95, 최저 점수: 67
```

💡 `{avg:.2f}` 는 소수점 둘째 자리까지 출력하는 형식 지정자입니다.

---

## 🐳 9. Docker 확장 (선택)

이제 Day 2까지의 코드를 Docker 컨테이너에

