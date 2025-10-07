# 🧭 데이터 엔지니어 로드맵 (Docker & Kubernetes 중심)

> 💡 **목표:**  
> 데이터 파이프라인을 설계·자동화하고,  
> Docker와 Kubernetes로 **운영 환경 수준의 프로젝트**를 완성한다.  
> ※ 학습 기간은 개인의 배경 지식과 실습 속도에 따라 달라질 수 있음.

---

## ⚙️ 전체 구조

| 단계 | 주제 | 설명 | 기간 |
|------|------|------|------|
| 0단계 | 환경 준비 | Python + Docker + VSCode 세팅
| 1단계 | Python 기초 | 데이터 처리 로직의 기반
| 2단계 | SQL & DB | PostgreSQL로 데이터 저장/조회
| 3단계 | ETL 파이프라인 | 데이터 수집 → 변환 → 적재 자동화
| 4단계 | 데이터 모델링 | 스타 스키마 설계, 정규화/비정규화 
| 5단계 | Airflow 오케스트레이션 | 파이프라인 스케줄링과 DAG 구성 
| 6단계 | Docker & Kubernetes | 배포 환경 구성 및 자동화
| 7단계 | 클라우드 & CI/CD | AWS, GitHub Actions, 자동배포

---

## 🧩 0단계: 환경 준비

### 목표
- Python 개발 환경과 컨테이너 환경을 세팅한다.

### 실습 항목
1. Python 설치 (`3.10+`)
2. VSCode + 확장팩 설치 (Python, Docker, YAML, GitLens)
3. Docker Desktop 또는 WSL2 기반 Docker 설치
4. GitHub 계정 생성 및 SSH Key 등록
5. 테스트용 “Hello ETL” 스크립트 실행

```bash
print("데이터 파이프라인 준비 완료!")
```

---

## 🐍 1단계: Python 기초

### 목표
- ETL 파이프라인의 변환 로직을 구성할 수 있는 수준의 Python 실력 확보

### 학습 내용
1. 기본 문법: 변수, 조건문, 반복문
2. 자료구조: 리스트, 튜플, 딕셔너리, 세트
3. 함수, 모듈, 패키지 구조
4. 파일 입출력 (`open`, `with`)
5. 예외 처리 (`try-except`)
6. 데이터 처리 기초 (`csv`, `json`)
7. 클래스와 객체지향 개념

### 실습
- JSON 파일을 읽어 특정 필드만 추출 후 CSV로 저장
- `if __name__ == "__main__":` 구조의 의미 이해 및 실습

---

## 🧮 2단계: SQL & 데이터베이스

### 목표
- 관계형 데이터 모델 설계 및 CRUD 조작 능력 확보

### 학습 내용
1. PostgreSQL 설치 및 CLI 실습
2. 데이터베이스 / 테이블 생성
3. 기본 CRUD (INSERT, SELECT, UPDATE, DELETE)
4. JOIN, GROUP BY, HAVING, 서브쿼리
5. 인덱스와 실행계획 (`EXPLAIN ANALYZE`)
6. 트랜잭션, 커밋, 롤백
7. Python과 DB 연결 (`psycopg2`)

### 실습
- Python 스크립트로 PostgreSQL 연동하여 데이터 적재
- 실행 계획 비교로 쿼리 성능 확인

---

## ⚗️ 3단계: ETL 파이프라인

### 목표
- 데이터를 **수집(Extract) → 변환(Transform) → 적재(Load)** 하는 자동화 흐름을 구축한다.

### 학습 내용
1. ETL 개념과 구성요소
2. API / 웹 크롤링 데이터 수집
3. Pandas를 이용한 데이터 정제 및 변환
4. DB 적재 자동화 (batch job)
5. 스케줄링 기초 (`cron`, `schedule` 모듈)

### 실습
- 공공데이터 API를 주기적으로 호출하여 PostgreSQL에 적재
- 로그 출력과 예외처리 구현

---

## 🧱 4단계: 데이터 모델링

### 목표
- 효율적인 데이터 구조 설계를 통해 분석 친화적인 스키마 구축

### 학습 내용
1. 정규화 / 비정규화 개념
2. 스타 스키마, 스노우플레이크 스키마 설계
3. Fact / Dimension 테이블 구분
4. 물리적 설계 (데이터 타입, 제약조건)
5. 샘플 데이터로 모델 검증

### 실습
- “판매 데이터 분석”용 스타 스키마 설계
- ERD 작성 (dbdiagram.io, draw.io 등)

---

## 🪶 5단계: Airflow 오케스트레이션

### 목표
- ETL 파이프라인을 스케줄링하고 의존성을 관리한다.

### 학습 내용
1. Airflow 개요 및 아키텍처
2. DAG (Directed Acyclic Graph) 구조
3. Operator / Task / Scheduler
4. BashOperator, PythonOperator 사용법
5. Task 간 의존성 관리 (`>>`, `<<`)
6. 로그 모니터링과 XCom

### 실습
- 간단한 DAG 작성 (`extract → transform → load`)
- 주기적 스케줄링 설정 (매일 00시 실행)

---

## 🐳 6단계: Docker & Kubernetes

### 목표
- 컨테이너 기반 환경에서 ETL 파이프라인을 안정적으로 배포한다.

### 학습 내용
1. Dockerfile 작성 및 이미지 빌드
2. docker-compose로 서비스 묶기
3. Kubernetes 개요 및 주요 개념
   - Pod, ReplicaSet, Deployment, StatefulSet
4. Headless Service와 PVC를 이용한 데이터 보존
5. `kubectl` 명령어와 yaml 매니페스트 작성

### 실습
- PostgreSQL StatefulSet 구성 (db-0: master / db-1~2: replica)
- Airflow + PostgreSQL을 Kubernetes에 배포

---

## ☁️ 7단계: 클라우드 & CI/CD

### 목표
- 클라우드 환경에서 데이터 파이프라인을 자동화하고 배포까지 완료한다.

### 학습 내용
1. AWS 기본 서비스
   - S3 (데이터 저장소)
   - EC2 (Airflow 호스팅)
   - IAM (권한 관리)
2. GitHub Actions로 CI/CD 구성
3. self-hosted runner 설정
4. Docker 이미지 자동 빌드 및 배포
5. 로그 및 모니터링 (CloudWatch, Grafana)

### 실습
- Airflow Docker 이미지를 GitHub Actions로 빌드 후 EC2로 자동 배포
- S3 연동으로 데이터 백업/복구

---

## 🎯 학습 완료 후 역량

| 구분 | 설명 |
|------|------|
| 프로그래밍 | Python 기반 데이터 처리 및 자동화 코드 작성 |
| DB 설계 | 정규화/비정규화 모델링, SQL 성능 분석 |
| 파이프라인 | ETL + Airflow 오케스트레이션 |
| 인프라 | Docker, Kubernetes 기반 배포 |
| 클라우드 | AWS 자원 활용 및 CI/CD 자동화 구축 |

---

## 📚 추천 학습 리소스

- **Python:** 《점프 투 파이썬》, Python 공식 문서
- **SQL:** Mode SQL Tutorial, PostgreSQL Docs
- **Airflow:** Apache Airflow 공식 튜토리얼
- **Docker & K8s:** Kubernetes 공식 문서, Docker Labs
- **AWS:** AWS Skill Builder (CLF-C02 대비)
- **CI/CD:** GitHub Actions Docs

---

> 📘 작성자: 데이터엔지니어링 로드맵 (SH ver.)
