# groupby() 특정 기준으로 묶어서 합계/평균 계산
# 예시 df.groupby("컬럼명").mean()

# matploltlib 데이터를 시각화하는 라이브러리
# 예시 plt.bar(), plt.plot() 등

# 꺾은선 / 막대 그래프 분포나 비교를 표현
# 예시 음식점 별점 등

import pandas as pd
import matplotlib.pyplot as plt

# 1. 음식 데이터를 음식명으로 groupby() 하기

df = pd.read_csv("foods1.csv", encoding="utf-8-sig")
grouped = df .groupby("음식")["별점"].mean()
print(grouped)

# 2. 음식 별점의 평균을 막대 그래프로 시각화 
# CTRL + ` 입력해 터미널 연 뒤 pip install matplotlib 로 matplotlib 설치

# 데이터를 음식 기준으로 묶는다 df.groupby("음식")
# ["별점"].mean() 음식 별점 열만 선택하여 평균을 계산한다
# grouped = df.groupby("음식")["별점"].mean() 
# plt.figure(figsize=(10, 6))  # 그래프 크기 설정
# grouped.plot(kind="bar", color="skyblue")

# plt.title("음식 별점 평균")  # 그래프 제목
# plt.xlabel("음식")
# plt.ylabel("평균 별점")
# plt. ylim(0,10) # y축 범위 설정
# plt.grid(axis='y', linestyle='--', alpha =0.5)  # y축 눈금선 추가

# plt.tight_layout()  # 레이아웃 조정
# plt.show()  # 그래프 출력

#실습 미션 - "음식 데이터 시각화"
# 요구사항
# 1. foods1.csv 파일을 불러오기
# 2. 음식 별점의 평균을 막대 그래프로 시각화하기

df = pd.read_csv("foods1.csv", encoding="utf-8-sig")
grouped_food =df.groupby("음식")["별점"].mean()

plt.figure(figsize=(6, 5))  # 그래프 크기 설정
grouped_food.plot(kind="bar", color="lightgreen")

plt.title("음식 별점 평균2")
plt.xlabel("음식")
plt.ylabel("평균 별점")
plt.ylim(0, 6)  # y축 범위 설정
plt.grid(axis='y', linestyle='--', alpha=0.5)  # y축 눈금선 추가

plt.tight_layout()  # 그래프에서 제목이나 축 레이블이 잘리지 않도록 조정
plt.show()  # 그래프 출력