# 조건 필터링 - 특정 조건의 행만 뽑기 df[df["컬럼명"] >= 4]
# 정렬 - 특정 컬럼 기준으로 정렬 df.sort_values("컬럼명")
# 요약 통계 - 평균, 합계 등 df["컬럼명"].mean(), df["컬럼명"].sum()
# 열 선택 - 특정 열만 선택 df[["컬럼1", "컬럼2"]]

import pandas as pd

# csv 파일 불러오기

df = pd.read_csv("foods.csv", encoding="utf-8-sig")
print(df)

# 조건 필터링 - 별점이 2 이상인 음식만 선택
high_rating = df[df["별점"] >= 2] 
print(f"\n === 별점이 2 이상인 음식 === {high_rating}")

# 정렬 - 별점 기준으로 내림차순 정렬
sorted_df = df.sort_values("별점", ascending=False)
print(f"\n === 별점 기준으로 내림차순 정렬된 음식 === {sorted_df}")

# 요약 통계 - 별점의 평균과 합계

print(f"평균 별점 : {round(df["별점"].mean(), 1)}") # 소수점 첫째자리까지 반올림
print(f"최고 별점 : {df["별점"].max()}")
print(f"별점 합계: {df["별점"].sum()}")
print(f"음식 개수: {df.shape[0]}") #행 개수


# 실습 미션 - "음식 데이터 분석"
# 요구사항
# 1. foods1.csv 파일을 생성해서 음식 이름과 별점을 5개 입력받아 저장한다.
# 2. 별점이 2 이상인 음식만 오름차순으로 필터링하여 출력한다
# 3. 별점의 최고, 합계를 출력한다

foods = []
ratings = []
for i in range(5):
    food = input(f"{i+1} 번째 음식을 입력해주세요. : ")
    rating = int(input(f"{food} 음식 별점 입력해주세요 : "))
    foods.append(food)
    ratings.append(rating)

# 데이터프레임 생성
df =pd.DataFrame({"음식": foods, "별점": ratings})

# CSV 저장
df.to_csv("foods1.csv", index=False, encoding="utf-8-sig")

# 2.저장된 CSV 읽기
df = pd.read_csv("foods1.csv", encoding="utf-8-sig")
high_rating = df[df["별점"]>= 2] 
sorting = high_rating.sort_values("별점", ascending=True)
# inplace=True는 원본 데이터프레임을 수정한다는 의미, 리턴값이 none이 되므로 변수에 저장하면 안됌.
# 하려면 함수로 따로 정의해야 함
# ascending=True는 오름차순 정렬을 의미

# 3. 별점의 최고, 합계 출력  
print(f"\n=== 별점이 최고인 음식 ===\n{df["별점"].max()}")
print(f"\n=== 별점의 합계 ===\n{df["별점"].sum()}")
