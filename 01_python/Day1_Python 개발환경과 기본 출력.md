# 🧱 1단계 Day 1 — Python 개발환경과 기본 출력

---

## 🎯 오늘의 목표

- 파이썬이 무엇인지 이해한다.  
- 파이썬 실행 환경을 설치하고 직접 코드를 실행해본다.  
- `print()` 함수와 문자열 포맷(f-string)을 자유롭게 사용할 수 있다.  

---

## 🧠 1. 파이썬이란?

> **데이터 엔지니어가 데이터 흐름을 자동으로 다루기 위한 기본 언어**

- 사람이 읽기 쉬운 문법  
- 다양한 데이터 라이브러리 (pandas, numpy, airflow 등)  
- 데이터 수집(Extract), 변환(Transform), 저장(Load)을 모두 처리 가능  

### 💬 비유로 설명하자면:
> Python은 데이터를 “옮기고 가공하는 컨베이어벨트의 두뇌” 같은 존재예요.

---

## ⚙️ 2. 환경 준비하기

### ✅ ① Python 설치 확인
먼저 현재 시스템에 Python이 설치되어 있는지 확인해보세요.

```bash
python --version
```

혹은 (운영체제에 따라 다를 수 있음)
```bash
python3 --version
```

✅ 결과 예시:
```
Python 3.10.12
```

만약 버전이 안 뜬다면 👉 [https://www.python.org/downloads/](https://www.python.org/downloads/) 에서 **3.10 이상 버전** 설치 후 재확인하세요.

---

### ✅ ② 폴더 구조 만들기

```bash
mkdir python_day1
cd python_day1
```

이 폴더 안에서 오늘의 실습을 진행합니다.

---

## 🧩 3. 첫 파이썬 코드 작성하기

이제 가장 기본적인 **출력 코드**를 작성해봅시다.

1️⃣ VSCode 또는 메모장에서 새 파일을 만듭니다.  
이름은 `hello.py` 로 저장하세요.

2️⃣ 아래 코드를 입력합니다.

```python
# hello.py
print("Hello, Data Engineering!")
```

3️⃣ 실행하기:

```bash
python hello.py
```

✅ 결과:
```
Hello, Data Engineering!
```

---

## 🧠 4. 문자열 포맷(f-string)

데이터를 출력할 때 변수를 포함시킬 수 있어야 해요.  
이때 사용하는 것이 **f-string** 입니다.

```python
name = "SungHyeon"
print(f"Welcome, {name}!")
```

✅ 실행결과:
```
Welcome, SungHyeon!
```

💡 **설명:**  
f-string에서 중괄호 `{}` 안에 변수를 넣으면, 자동으로 문자열에 삽입됩니다.

---

## 🧩 5. 간단한 데이터 출력 연습

데이터 엔지니어링에서는 데이터를 로그처럼 출력하는 일이 많습니다.  
다음 예시를 실행해보세요 👇

```python
print("데이터 수집 중...")
source = "API"
records = 350
print(f"{source}에서 {records}개의 데이터를 불러왔습니다.")
```

✅ 실행 결과:
```
데이터 수집 중...
API에서 350개의 데이터를 불러왔습니다.
```

💡 이런 출력문은 ETL 과정 중에 **데이터 상태를 확인하는 로그**로 사용됩니다.

---

## 🧩 6. 주석(Comment) 사용법

코드 위에 설명을 달 때는 `#`을 사용합니다.  
주석은 실행되지 않고, 코드 가독성을 높여줍니다.

```python
# 데이터 엔지니어링 실습 1일차
print("Hello Data Engineer!")
```

---

## 🧠 7. print() 활용 심화 — 여러 줄 출력

파이썬에서는 `\n`을 이용해 여러 줄을 출력할 수 있습니다.

```python
print("데이터 추출 시작...\n변환 중...\n적재 완료 ✅")
```

✅ 결과:
```
데이터 추출 시작...
변환 중...
적재 완료 ✅
```

---

## 🧪 8. 실습 체크리스트

| 항목 | 확인 |
|------|------|
| Python 3.10 이상 설치 완료 | ☐ |
| hello.py 실행 성공 | ☐ |
| f-string 사용 성공 | ☐ |
| 주석(`#!`)으로 설명 추가 | ☐ |
| 여러 줄 출력 실습 완료 | ☐ |

---

## 🐳 9. Docker 확장 (선택)

데이터 엔지니어는 종종 파이썬 코드를 Docker 컨테이너 안에서 실행합니다.  
로컬이 아닌 **격리된 환경**에서 같은 코드가 동일하게 동작하는지 확인하기 위해서죠.

### Dockerfile 생성

`Dockerfile` 파일을 만들고 아래 내용을 작성하세요.

```dockerfile
# python_day1/Dockerfile
FROM python:3.10
COPY hello.py .
CMD ["python", "hello.py"]
```

### 빌드 & 실행
```bash
docker build -t python-hello .
docker run python-hello
```

✅ 결과:
```
Hello, Data Engineering!
```

이제 로컬이 아닌 Docker 환경에서도 동일하게 동작함을 확인했습니다.

---

## 🧭 오늘의 핵심 요약

| 개념 | 설명 |
|------|------|
| Python | 데이터를 자동화하는 언어 |
| print() | 콘솔에 메시지 출력 |
| f-string | 변수 포함 문자열 |
| 주석(#) | 실행되지 않는 설명문 |
| Dockerfile | 실행 환경 자동화 도구 |

---

## 🧩 다음 단계 (Day 2 예고)

> 내일은 “변수와 자료형”을 다루며  
> 데이터를 메모리에 저장하고, 숫자/문자/리스트 등 다양한 형태로 관리하는 법을 배웁니다.  
>  
> 📂 다음 학습 파일: `day2_variables.py`

---

✅ **오늘의 미션**
1. `hello.py` 코드를 직접 실행해본다.  
2. 본인 이름으로 f-string을 테스트한다.  
3. Dockerfile을 만들어 동일한 결과를 컨테이너에서 확인한다.


