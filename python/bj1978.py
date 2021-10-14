
N = int(input())
number = list(map(int,input().split()))

count = 0
for i in range(N):
  if int(number[i])<4:
    if int(number[i]) == 1:
      continue
    count += 1
    continue
  else:
    for num in range(2,int(number[i])):
      if int(number[i])%num == 0:
        break
      if num == int(number[i])-1: # 마지막까지 number보다 작은 어떤 값으로도 나눠지지 않는다면 count 1 상승
        count += 1

print(count)