# lesson : 처음 bj1929_3에서 시도한대로 비교값의 루트값 전까지 비교하는 알고리즘을 작성했지만 시간 초과 발생
# 문제는 isSosu가 while문 내에서 돌아가면 O(n**3)이 되버리는 것이다. 
# 
# 해결책 : isSosu를 while문 밖으로 빼서 알고리즘 생성
# -> 비교할 수의 범위가 123,456까지이므로 미리 해당 범위내(물론 123,456*2 범위내) 소수 값들을 while 밖에서 찾은 후 while문 안에서는 그 소수 값들 중에서
# 우리가 찾는 범위 내의 소수값이 무엇인지만 비교! 
# so O(n**2)의 복잡도를 만들 수 있다.
 
def isSosu(num):  # num이 소수인지 확인하는 함수
  for n in range(2,int(num**0.5)+1):  # 2부터 num의 루트값까지만 비교하면 된다!
    if num%n == 0:  # 2부터 시작하는 값에서 num과 나눠지는 값이 나오면 소수가 아니다.(False)
      return False
  return True # 2부터 num의 루트값까지 num과 나눠지는 값이 하나도 없다면 소수이다.(True)

Sosu = [] # 미리 소수 값을 넣어줄 리스트

for num in range(2,2*123456+1): # n이 123456까지이므로 2n 범위인 123456*2까지 안에 있는 소수 값들 미리 찾는다.
  if isSosu(num) == True:
    Sosu.append(num)

while True:
  n = int(input())
  count = 0
  if n == 0:
    break
  for i in Sosu:  # 여기서는 찾아놓은 소수값들중 원하는 범위에 소수가 몇개 있는지 파악한다.
    if n < i and i <= 2*n:
      count += 1
  print(count)