# 🧱 Day 3 — 조건문과 반복문 (Conditionals & Loops)

---

## 🎯 오늘의 목표
- `if` 문으로 조건에 따라 다른 결과를 출력할 수 있다.  
- `for`, `while` 문으로 반복적인 데이터 처리를 자동화할 수 있다.  

---

## 🧠 1. 조건문 (if statement)

> 조건을 검사해서, 맞으면 실행하고 아니면 다른 걸 실행하는 문장입니다.

```python
score = 85

if score >= 80:
    print("합격 🎉")
else:
    print("불합격 ❌")
```

✅ 실행 결과:
```
합격 🎉
```

💡 **조건문의 구조**
```python
if 조건:
    실행코드
elif 다른조건:
    실행코드
else:
    실행코드
```

---

## 🧪 실습 1: 조건문 확장

```python
score = 73

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
else:
    print("F학점")
```

✅ 출력 예시:
```
C학점
```

💡 Tip:  
조건은 위에서 아래로 검사되며, **처음으로 맞는 조건**만 실행됩니다.

---

## 🧩 2. 논리 연산자

조건을 2개 이상 조합할 수 있습니다.

| 연산자 | 의미 | 예시 |
|--------|------|------|
| `and` | 둘 다 참 | `score >= 80 and score <= 90` |
| `or` | 둘 중 하나라도 참 | `score < 60 or score > 90` |
| `not` | 반대 | `not is_active` |

---

## 🧠 3. 반복문 (for, while)

> “같은 일을 여러 번 반복해서 처리”할 때 사용합니다.  

데이터 엔지니어는 반복문으로 **데이터 여러 행(row)**을 순회합니다.

---

### 🧩 for 문 기본형

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("과일:", fruit)
```

✅ 출력:
```
과일: apple
과일: banana
과일: cherry
```

💡 리스트(`[]`)의 요소를 하나씩 꺼내서 `fruit`에 넣고 출력합니다.

---

### 🧪 실습 2: 점수 데이터 순회

```python
scores = [75, 88, 92, 67, 95]

for s in scores:
    print(f"점수 {s} →", end=" ")
    if s >= 80:
        print("합격 🎉")
    else:
        print("불합격 ❌")
```

✅ 출력:
```
점수 75 → 불합격 ❌
점수 88 → 합격 🎉
점수 92 → 합격 🎉
점수 67 → 불합격 ❌
점수 95 → 합격 🎉
```

💡 `end=" "` 는 줄바꿈 대신 같은 줄에 출력하도록 설정한 옵션입니다.

---

## 🧩 4. while 문

> 조건이 **참인 동안 계속 실행**됩니다.

```python
n = 1
while n <= 5:
    print("현재 값:", n)
    n += 1
```

✅ 출력:
```
현재 값: 1
현재 값: 2
현재 값: 3
현재 값: 4
현재 값: 5
```

💡 `while`문은 반복 횟수가 명확하지 않을 때 유용합니다.  
예: 데이터 수집 API를 실패할 때까지 반복 요청

---

## 🧪 실습 3: 누적 합 구하기

```python
total = 0
for i in range(1, 6):
    total += i
print("합계:", total)
```

✅ 결과:
```
합계: 15
```

💡 `range(1,6)` → 1부터 5까지 숫자 생성  
`+=`는 누적 덧셈 (total = total + i)

---

## 🧠 5. 반복 제어 문

| 키워드 | 설명 | 예시 |
|---------|------|------|
| `break` | 반복 종료 | 특정 조건에서 멈춤 |
| `continue` | 다음 반복으로 건너뜀 | 조건에 따라 일부만 건너뜀 |

```python
for num in range(1, 10):
    if num == 5:
        break
    print(num)
```
✅ 출력:  
```
1
2
3
4
```

---

## 🧩 6. 중첩 반복문 (Nested loop)

> 반복문 안에 또 반복문을 넣을 수

