# lesson : bj1978 과 다른 점은 n = int(number[i])이다 
# 매번 int()로 타입변환 연산을 수행하는 것이 더 느릴 것 같아. 시간을 비교해보았는데 역시나 더 느렸다.
# 매번 int() 연산을 수행한 코드의 경우 76ms의 시간이 걸린 반면 처음에 저장해준 코드는 68ms로 약 10.5%의 시간이 감소하였다.

N = int(input())
number = list(map(int,input().split()))

count = 0
for i in range(N):
  n = int(number[i])
  if n<4:
    if n == 1:
      continue
    count += 1
    continue
  else:
    for num in range(2,n):
      if n%num == 0:
        break
      if num == n-1: # 마지막까지 number보다 작은 어떤 값으로도 나눠지지 않는다면 count 1 상승
        count += 1

print(count)