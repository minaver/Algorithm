# lesson : 
# 1. 만약 알고리즘 작성시 변수 범위가 바뀌거나 변수 의미가 바뀌면 해당 변수에 대해 모든 부분에서 재고해 주어야한다.
# 2. 명심! 항상 초기값, 마지막 값은 특수한 경우일 수 있으므로 test해준다! 이번에는 i == 2일 때(line 14에서 range가 돌아가지 않을 때)를 고려하지 못해 한번에 맞추지 못했다.

M = int(input())
N = int(input())

sosu = []
for i in range(M,N+1):
  if i == 1: 
    continue
  if i == 2:
    sosu.append(i)
  for less_num in range(2,i):
    if i%less_num == 0:
      break
    if less_num == i-1:
      sosu.append(i)

if len(sosu) == 0:
  print(-1)
else:
  print(sum(sosu))
  print(min(sosu))
