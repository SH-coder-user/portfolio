# for 반복문 리스트나 범위를 순회 
# 예시 for x in [1,2,3]:
    
# while 반복문 조건이 참인 동안 계속 실행
# 예시  while x < 5:
#     x += 1

# 함수 def 코드 재사용 단위 def 함수이름(매개변수):
#     return 값    

# 1. 반복문 실습

foods = ["오렌지", "사과", "오이"]

for food in foods:
    print(f"오늘의 음식 {food} 입니다.")


# 2. while문 실습
i = 1
while i  <=5 :
    print(f"{i} 번째 반복입니다.")
    i += 1 # i = i + 1 과 동일한 의미로 i를 1씩 증가시킴


# 3. 함수 실습
def greet(name):
    print(f"안녕하세요 {name}님!!")

greet("마누엘")

#4. 실습미션 - "반복문과 함수 활용"
# 요구사항
# 1. 음식 리스트를 하나 만든 후
# 2. 사용자에게 음식명을 입력받아
# 3. 음식 리스트를 하나하나 출력하되 출력형식은 음식순번, 음식명

i = 0
foodlist = []  # 빈 리스트 생성
while i <5: 
    inputfood= input("음식명을 입력하세요 : ")
    foodlist.append(inputfood)
    i += 1

for i, food in enumerate(foodlist):
    print(f"음식 {i+1} 번째는 {food} 입니다.")


# enumerate() 함수는 리스트나 튜플과 같은 순서가 있는 자료형을 순회할 때 인덱스와 값을 동시에 가져올 수 있게 해줍니다.
# 같은 중복 값이 있는 경우에도 인덱스가 다르게 출력된다는 것을 배웠다.

# 만약 for i in foodlist:
#     print(f"음식 {i+1} 번째는 {food} 입니다.") 
# 와 같이 했다면 중복값이 있는 경우 인덱스가 중복되어 출력되었을 것이다.
