
def isSosu(num):  # num이 소수인지 확인하는 함수
  for n in range(2,int(num**0.5)+1):  # 2부터 num의 루트값까지만 비교하면 된다!
    if num%n == 0:  # 2부터 시작하는 값에서 num과 나눠지는 값이 나오면 소수가 아니다.(False)
      return False
  return True # 2부터 num의 루트값까지 num과 나눠지는 값이 하나도 없다면 소수이다.(True)

T = int(input())

for i in range(T):
  n = int(input())

  sosu = []
  for num in range(2,n):
    if isSosu(num) == True:
      sosu.append(num)

  for ss in sosu:
    other_ss = n - ss
    if sosu.index(other_ss) != 0:
      
