
def isSosu(num):  # num이 소수인지 확인하는 함수
  for n in range(2,int(num**0.5)+1):  # 2부터 num의 루트값까지만 비교하면 된다!
    if num%n == 0:  # 2부터 시작하는 값에서 num과 나눠지는 값이 나오면 소수가 아니다.(False)
      return False
  return True # 2부터 num의 루트값까지 num과 나눠지는 값이 하나도 없다면 소수이다.(True)

T = int(input())

sosu = []
for j in range(2,10000):
  if isSosu(j) == True:
    sosu.append(j)

for i in range(T):
  n = int(input())

  result = [0,0]
  s = sosu[0]
  p = 1
  while s <= n/2:
    other_num = n - s
    if sosu.count(other_num) == 1:
      result[0] = s
      result[1] = other_num
    s = sosu[p]
    p += 1
  
  print(result[0],result[1])

      

