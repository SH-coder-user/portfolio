# 파일쓰기 (write) 텍스트를 파일에 저장
# 예시 f.write("여기에 저장할 내용")

# 파일 읽기 (read) 텍스트를 파일에서 읽기
# 예시 f.read()

# with open() 안전하게 파일 다루기(자동 닫힘)
# 예시 with open("파일명", "모드") as f:


# 1. 텍스트 파일에 쓰기

foods = ["오렌지", "캬라멜", "밥"]

with open("foods.txt","w", encoding="utf-8") as f:
    for food in foods:
        f.write(f"{food}\n")  # 각 음식명을 새 줄에 저장

# "w" 쓰기 모드(기존 파일 덮어쓰기)
# encoding="utf-8"은 한글 인코딩을 위해 사용

# 2. 텍스트 파일 읽기

with open("foods.txt", "r", encoding="utf-8") as f:
    lines =f.readlines()  # 파일의 모든 줄을 읽어 리스트로 반환

    for i, line in enumerate(lines):
        print(f"{i+1}. {line.strip()}")

# readlines()는 파일의 모든 줄을 읽어 리스트로 반환합니다.
# strip()은 각 줄의 앞뒤 공백을 제거합니다.


# 3. 실습미션 - "음식 저장 프로그램"

# 요구사항
# 1. 사용자에게 음식명을 3개 입력받고
# 2. 입력받은 음식명을 텍스트 파일에 저장한다.
# 3. 저장된 음식명을 다시 읽어와서 출력한다.

food_list = []

for i in range(3):
    food =input(f"{i+1} 번째 음식명을 입력하세요: ")
    food_list.append(food)

# 파일 저장하기
with open("foods_list.txt","w", encoding="utf-8") as f:
    for food in food_list:
        f.write(f"{food}\n")

# 파일 읽기
with open("foods_list.txt","r", encoding="utf-8") as f:
    lines = f.readlines()
    print("저장된 음식 목록: ")
    for i, line in enumerate(lines):
        print(f"{i + 1}. {line.strip()}")

# for 문에서 i와 line 두개를 선언하는 이유는 enumerate() 함수를 사용하여 인덱스와 값을 동시에 가져오기 때문이다.
# 콤마로 구분되어 i는 인덱스, line은 해당 줄의 내용(문자열 데이터)을 나타낸다.
        