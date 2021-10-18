# lesson : O(n^2)로 시간초과
M,N = map(int,input().split())

for num in range(M,N+1):
  if num == 1:
    continue
  elif num == 2:
    print(2)
  else:
    for i in range(2,num):
      if num%i == 0:
        break
      if i == num-1:
        print(num)


