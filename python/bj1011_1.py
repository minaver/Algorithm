# lesson : O() 시간을 줄이고 싶다며 자체적으로 알고리즘을 만들어야한다 
# 이때 최대한 구체적인 test-case를 제작 -> 규칙성을 찾는다

T = int(input())

while T != 0:
  x,y = map(int,input().split())
  length = y-x
  count = 0
  move = 1
  move_sum = 0

  while move_sum < length:
    count += 1
    move_sum += move
    if count%2 ==0:
      move += 1
  print(count)
  T -= 1
