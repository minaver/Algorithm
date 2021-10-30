# lesson : 실수 1 dist 마지막에 **0.5를 해줘야하는데 **1/2을 해줬다.. 다음같이 하면 **1) /2 이렇게 된다
# 경우의 수를 명확하게 생각하라! '혹시 이런경우는 없을까'까지 생각하는게 중요


T = int(input())

for t in range(T):
  x1, y1, r1, x2, y2, r2 = map(int,input().split())

  dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
  if x1 == x2 and y1 == y2 and r1 == r2:
    print(-1)
  elif r1 + r2 < dist:
    print(0)
  elif r1 + r2 == dist:
    print(1)
  else:
    if abs(r1 - r2) == dist:
      print(1)
    elif abs(r1 - r2) > dist:
      print(0)
    else:
      print(2)
