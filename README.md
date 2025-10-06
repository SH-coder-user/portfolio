# 🧭 데이터 엔지니어링 로드맵 (Docker & Kubernetes 중심)

> 💡 목표:  
> 데이터 파이프라인을 설계·자동화하고,  
> Docker와 Kubernetes로 **운영 환경 수준의 프로젝트**를 완성한다.
> 계획학습기간과 별개로 실제학습기간은 더 단축 되거나 늘어날 수 있다.

---

## ⚙️ 전체 구조

| 단계 | 주제 | 설명 | 기간 |
|------|------|------|------|
| 0단계 | 환경 준비 | Python + Docker + VSCode 세팅 | 1일 |
| 1단계 | Python 기초 | 데이터 처리 로직의 기반 | 7일 |
| 2단계 | SQL & DB | PostgreSQL로 데이터 저장/조회 | 7일 |
| 3단계 | ETL 파이프라인 | 데이터 수집 → 변환 → 적재 자동화 | 7일 |
| 4단계 | 데이터 모델링 | 스타 스키마 설계, 정규화/비정규화 | 5일 |
| 5단계 | Airflow 오케스트레이션 | ETL 워크플로우 자동화 | 5일 |
| 6단계 | Docker | 모든 환경을 컨테이너로 관리 | 5일 |
| 7단계 | Kubernetes | 컨테이너 자동화·확장 운영 | 10일 |
| 8단계 | 포트폴리오 프로젝트 | 실제 데이터 파이프라인 구축 | 7일 |

총 학습 기간: **약 45~50일 (2개월)**  
→ 완전 초보 → 실무형 데이터 엔지니어로 성장할 수 있는 커리큘럼

---

## 🪜 0단계. 환경 준비

### 🎯 목표
- Python, VSCode, Docker 설치
- 실습용 폴더 구조 세팅

### 📘 핵심 명령어
```bash
python --version
docker --version
mkdir data-engineering-lab && cd data-engineering-lab
```

---

## 🧱 1단계. Python 기초 (7일)
> 데이터 처리 로직의 핵심 언어

| Day | 주제 | 학습 포인트 |
|-----|------|--------------|
| 1 | 환경 & 출력 | print(), f-string |
| 2 | 변수와 자료형 | int, str, list, dict |
| 3 | 조건문·반복문 | if / for / while |
| 4 | 함수 | 코드 재사용, 모듈화 |
| 5 | 파일 입출력 | CSV, JSON |
| 6 | Pandas | 표 형식 데이터 처리 |
| 7 | 미니 ETL 프로젝트 | Extract → Transform → Load |

✅ 결과  
> Python으로 CSV/JSON 데이터를 처리하는 기본 ETL 흐름 완성  

---

## 🧭 2단계. SQL & Database (7일)
> 데이터를 안전하게 저장하고 효율적으로 조회하는 기술

### 📘 실습 환경: Docker 기반 PostgreSQL

```bash
docker run --name pgdb -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```

| Day | 주제 | 실습 포인트 |
|-----|------|--------------|
| 1 | 데이터베이스 개념 | DB, Table, Row, Column |
| 2 | SELECT 기초 | WHERE, ORDER BY |
| 3 | GROUP BY, JOIN | 다중 테이블 관계 |
| 4 | DDL, DML | CREATE, INSERT, UPDATE |
| 5 | Index & Key | PK, FK 이해 |
| 6 | Pandas + SQL 연동 | Python에서 DB 쿼리 |
| 7 | 미니 DB 프로젝트 | 사용자·주문 테이블 설계 |

✅ 결과  
> 로컬 PostgreSQL + Python 연동 성공  
> SQL 쿼리와 ETL 데이터 저장의 기초 완성

---

## 🔄 3단계. ETL 파이프라인 구축 (7일)
> 데이터 흐름 전체를 코드로 자동화

### 📘 구성
- Extract: CSV/JSON or API
- Transform: Pandas로 정제
- Load: PostgreSQL 저장

| Day | 주제 | 예시 |
|-----|------|------|
| 1 | ETL 개념 이해 | Extract→Transform→Load |
| 2 | 데이터 수집 | CSV, API 요청 |
| 3 | 데이터 정제 | 결측치, 중복 제거 |
| 4 | 적재(Load) | DB 저장 자동화 |
| 5 | 스케줄링 | 매일 자동 실행(Cron) |
| 6 | 로깅 | 실행 결과 기록 |
| 7 | 미니 파이프라인 프로젝트 | 전체 흐름 연결 |

✅ 결과  
> Python 스크립트만으로 매일 실행되는 ETL 파이프라인 완성  

---

## 🧩 4단계. 데이터 모델링 (5일)
> 데이터를 분석하기 좋은 구조로 설계

| Day | 주제 | 실습 |
|-----|------|------|
| 1 | 정규화/비정규화 | 테이블 분리와 조인 |
| 2 | 스타 스키마 | Fact/Dimension 구분 |
| 3 | DWH 개념 | 분석용 DB와 운영용 DB 차이 |
| 4 | 성능 최적화 | Index, Partition |
| 5 | ERD 설계 프로젝트 | ERD 다이어그램 만들기 |

✅ 결과  
> PostgreSQL 기반의 데이터 모델 설계 능력 확보  

---

## ⚙️ 5단계. Airflow 오케스트레이션 (5일)
> 여러 ETL 작업을 자동으로 관리하고 시각화하는 도구

### 📘 실습 환경: Docker-compose 기반 Airflow

```yaml
version: '3'
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: airflow
  webserver:
    image: apache/airflow:2.7.0
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
    ports:
      - "8080:8080"
```

| Day | 주제 | 실습 |
|-----|------|------|
| 1 | Airflow 구조 | DAG, Operator, Task |
| 2 | PythonOperator | Python 코드 자동화 |
| 3 | Scheduling | 매일 정해진 시간 실행 |
| 4 | Logging & Retry | 실패 시 재시도 |
| 5 | DAG 프로젝트 | 실전 ETL 파이프라인 구성 |

✅ 결과  
> Docker 기반 Airflow 환경에서 자동화 파이프라인 완성  

---

## 🐳 6단계. Docker 심화 (5일)
> 파이프라인 전체를 컨테이너화하여 일관된 환경 구축

| Day | 주제 | 실습 |
|-----|------|------|
| 1 | Docker 개념 | 이미지 vs 컨테이너 |
| 2 | Dockerfile 작성 | Python, PostgreSQL |
| 3 | Docker Compose | 다중 컨테이너 연결 |
| 4 | 볼륨/네트워크 | 데이터 유지 및 통신 |
| 5 | 프로젝트 컨테이너화 | 전체 ETL 시스템 통합 |

✅ 결과  
> Python + DB + Airflow + Logging 환경을 Docker로 완전 자동화  

---

## ☸️ 7단계. Kubernetes 확장 (10일)
> 컨테이너를 자동으로 배포, 확장, 복구하는 기술

### 📘 실습 환경
- Minikube (로컬 K8s 클러스터)
- kubectl 명령어
- yaml 배포 파일 작성

| Day | 주제 | 실습 |
|-----|------|------|
| 1 | K8s 기본 구조 | Pod, Deployment, Service |
| 2 | Minikube 설치 | 로컬 클러스터 실행 |
| 3 | Pod 배포 | `kubectl apply -f` |
| 4 | Deployment & Replica | 자동 복제 |
| 5 | Service (ClusterIP/NodePort) | 통신 노출 |
| 6 | Persistent Volume | 데이터 유지 |
| 7 | StatefulSet | DB 안정적 운영 |
| 8 | ConfigMap / Secret | 설정값 관리 |
| 9 | Job / CronJob | ETL 자동 실행 |
| 10 | Helm 패키지화 | 배포 자동화 |

✅ 결과  
> ETL 파이프라인을 Kubernetes 클러스터에서 자동 실행 및 확장 가능  

---

## 🚀 8단계. 포트폴리오 프로젝트 (7일)
> 실제 데이터 파이프라인 구축 & 자동화 시스템 완성

### 🎯 목표
- Docker/K8s 기반 데이터 파이프라인 구축
- Airflow로 ETL 자동화
- PostgreSQL 저장 및 로그 관리

### 📘 예시 프로젝트
**“일별 판매 데이터를 수집 → 변환 → DB 적재 → 자동화 스케줄링”**

| 구성요소 | 도구 |
|-----------|------|
| 데이터 수집 | Python + API |
| 데이터 변환 | Pandas |
| 적재 | PostgreSQL |
| 자동화 | Airflow DAG |
| 배포 | Docker + Kubernetes |

✅ 결과  
> 완전 로컬 환경에서 동작하는 **엔드투엔드 데이터 파이프라인** 완성  
> 포트폴리오로 바로 제출 가능 🎯

---

## 🧠 학습 순서 요약

```plaintext
Python → SQL → ETL → Modeling → Airflow → Docker → Kubernetes → Project
```

---

## 💡 학습 비용
💰 **0원 (100% 로컬 실행 가능)**  
AWS, GCP 같은 클라우드 자원은 모두 Docker/Kubernetes로 대체됨.  
필요할 경우 나중에만 AWS로 확장.

---

## 🔖 태그
`#DataEngineering` `#Python` `#SQL` `#ETL`  
`#Docker` `#Kubernetes` `#Airflow` `#PostgreSQL` `#Portfolio`

