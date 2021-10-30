# lesson : hypot == 빗변 이다. 
# a,b,c 중 어느 선이 빗변일지 모르니 max() 함수로 빗변을 찾은 후 해당 값에 따라 직각삼각형 찾기를 진행해준다.
# O(n)을 유지하기 위해 if문을 길게 가져갔다. if문 안에는 어자피 한 조건만(if,elif,else 중 하나만) 들어가므로 시간 효율이 더 좋다.

while True:
  a,b,c = map(int,input().split())
  if a == 0 and b == 0 and c == 0:
    break

  hypot = max(a,b,c)
  
  if hypot == a:
    if a**2 == b**2 + c**2:
      print("right")
    else:
      print("wrong")
  elif hypot == b:
    if b**2 == a**2 + c**2:
      print("right")
    else:
      print("wrong")
  else:
    if c**2 == a**2 + b**2:
      print("right")
    else:
      print("wrong")
  