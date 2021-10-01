import sys

num = int(input())
count = 0 # group word가 아닌 word 수를 count

for i in range(num):
  word = sys.stdin.readline().rstrip() # 문자들 입력 받는다.
  for index in range(len(word)): # 
    # boolcount = 0 : 같은 값만 계속 나온 경우 
    # boolcount = 1 : 같은 값이 나오다 다른 값이 나오고 다시 같은 값이 안나온 경우
    # boolcount = 2 : 같은 값이 나오다 다른 값 나오고 또 과거와 같은 값이 나오는 경우
    boolcount = 0;  # 시작은 0에서 시작하여 ++된다.
    mov_index = index +1; # while 안에서 1씩 증가하면서 target index 와 비교할 index

    while mov_index < len(word): # 마지막 index까지 반복 
      if word[index] != word[mov_index]: # target index의 값과 같은 값이 나올경우 처음나오던 두번째로 나오던 순서나 횟수가 중요한게 아니라 '나온 사실' 자체가 중요하다.
        boolcount = 1

      if boolcount == 1 and word[index] == word[mov_index]: # boolcount가 이미 1인 상태에서 target index와 같은 값이 나올 경우
        boolcount = 2
        break

      mov_index = mov_index +1 # mov_index 마지막 index까지 조금씩 이동
    
    if boolcount == 2: # out while loop if boolcount == 2 이면 not group word 라는 뜻 
      count = count +1
      break

print(num-count) # group word 수 출력