# lesson
# 1. 등차로 더해지는 구조 구현시 초기 등차값을 지정하고 차이값을 loop안에서 구현해준다.

x = int(input())
comp_num = 1
line = 2

while True:
  if x <= comp_num :
    break
  comp_num = comp_num + line
  line = line +1

dist = comp_num - x # 3-2 =1

if line%2 != 0:
  a = line - 1 -dist
  b = line - a
else :
  b = line - 1 -dist
  a = line - b

print(f"{a}/{b}")