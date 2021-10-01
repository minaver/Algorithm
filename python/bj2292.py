# lesson 
# 1. 문제에서 말하는 범위를 정확하게 보자 num의 범위가 어디부터 시작인지 어디서 끝나는지!
# 복잡한 문제, 알고리즘이 쉽게 떠오르지 않을떄는 계산 횟수나 비용이 그리 크지 않다면 컴퓨터에게 단순하게 맞겨보자!

num = int(input()) -2 # 시작 input값을 2라고 할때 시작을 0으로 설정 

road = 2      # 걸리는 길의 수
comp_num = 6  # 비교 기준 숫자 
i = 2         # 이후 comp_num가 누적 등차로 증가할 때 사용할 변수 

if num == -1: # 입력 변수가 1일 경우 처리 
  road = 1
else :
  while True:
    if num < comp_num:  # comp_num이 "comp_num = comp_num + 6*i" 로 증가하여 num을 초과할 때까지 loop
      break   # 초과하면 break
    else:
      comp_num = comp_num + 6*i # i를 사용한 comp_num의 누적 등차 증가 6 -> 6+12 -> 6+12+18 -> 6+12+18+24 -> ...
      road = road +1    # 한 계층씩 블럭이 쌓여갈수록 길의 수 증가 
      i = i +1

print(road)
