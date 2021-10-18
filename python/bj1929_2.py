# lesson : 처음 시도에서 소수 탐색시 해당 수보다 작은 범위에서 loop를 돌렸다면 이번에는 소수인 숫자 범위에서만 loop을 돌렸다.
# 그래도 동일하게 O(n^2)의 복잡도를 갖어 시간 초과 발생한다.
M,N = map(int,input().split())

sosu = [2]  # 소수값 누적 

for num in range(2,N+1):  # 2부터 N까지
  mode = True # 소수인지 확인할 boolean
  for s in sosu:  # num을 sosu list안 요소들과 비교하여 나눠 떨어지는지 확인
    if num%s == 0 and num != s: # 소수로 나눠지는 경우 즉 소수가 아닌 경우 (이때 같은 값으로 나눠지는 것은 예외이다)
      mode = False  # 나눠진다면 소수가 아니므로 mode 를 false로 변환
      break
  if mode == True:  # 만약 위 for loop을 모두 돌고도 mode가 True로 유지된다면 소수이다 라는 것
    sosu.append(num)  # 해당 값을 sosu list에 추가
    if num >= M:  # M부터 출력해야하니 num >= M시 print
      print(num)

      