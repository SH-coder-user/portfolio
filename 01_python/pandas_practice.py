import pandas as pd

foods = []
ratings = []

for i in range(3):
    food = input("음식 이름을 입력하세요: ")
    rating = int(input("맛은 1~5 중 몇 점인가요? "))
    foods.append(food)
    ratings.append(rating)

# 데이터프레임 생성
# 표 형식 데이터로 변환, 일종의 테이블 형태로 변환
df = pd.DataFrame({
    "음식": foods,
    "별점": ratings
})

# CSV 저장
df.to_csv("foods.csv", index=False, encoding="utf-8-sig")  
# index=False는 인덱스 열을 저장하지 않도록 설정 , utf-8 만 했을 시 엑셀에서 읽으니
# 한글이 깨져서 보임. utf-8-sig로 저장하여 해결

# 저장된 CSV 읽기
read_df = pd.read_csv("foods.csv", encoding="utf-8-sig")
print("=== 저장된 음식 목록 ===")
print(read_df)
