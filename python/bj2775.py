# lesson
# 역시 O(n^3)은 런타임에 무리가 있다.
T = int(input())

for t in range(T):
  k = int(input())
  n = int(input())
  room = [0 for _ in range(n)]
  room_low = [i for i in range(1,n+1)]

  if k == 1:
    ans = sum(room_low)
  else: 
    for i in range((k-1)*n):
      for j in range(i+1):
        room[j] += room_low[j]
      if (i+1)%n == 0:
        room_low = room 
    ans = sum(room)

  print(ans)
    
