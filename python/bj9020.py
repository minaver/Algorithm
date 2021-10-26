# lesson : 에라토스테네스의 체 함수를 공부하였다. 처음에 생짜로 시도해보았는데 계속 O(n**3) 시간 복잡도가 도출되어 시간초과 발생하였다.
# 해당 방법으로 미리 소수인지 아닌지를 알고있는 리스트를 제작후 비교하면 O(n**2)의 시간 복잡도로 수행 가능하다. 


def eratos(n):  # 에라토스테네스의 체 함수 제작
  sosu = [1 for s in range(n+1)]  # 먼저 원하는 범위의 수(n+1)를 크기로 갖는 리스트를 제작 모두 1로 초기화
  for i in range(2,int(n**0.5)+1):  # 각 sosu 리스트의 요소를 n의 최대 약수까지 비교연산
    if sosu[i] == 1:  # 만약 해당 요소가 소수일 경우
      for j in range(i*2,n,i):  # 해당 요소의 배수들은 모두 소수가 아니다
        sosu[j] = 0

  return sosu

sosu = eratos(10000)  # 에라토스테네스의 체 함수 호출

T = int(input())  
for t in range(T):  
  n = int(input())
  for c in range(int(n/2),n): # 차이가 가장 작은 두 소수를 우선하여 출력하므로 n의 1/2값 부터 소수인지 확인한다(이때가 차이가 최소)
    if sosu[c] == 1 and sosu[n-c] == 1: # 두 비교 값(c,n-c)이 모두 소수일 경우 
      print(n-c,c)  # 위 조건문 참일시 바로 '최소 차이 소수'에 해당하므로 해당 값 그냥 출력해버린다.
      break