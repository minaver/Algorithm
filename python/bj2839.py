# lesson
# 1. 큰 범위부터 작은 범위로의 확장 문제 : 
#   3보다 5에 우선순위가 주어져 있었으므로 loop을 거꾸로 사용하면서 5를 MAX 치에서 점점 줄여주고 그와 동시에 3을 점점 증가시켜 주는 방향으로 작성
# 2. loop 외부에서 loop안에서의 특정 조건을 원하는 경우 전역적으로 사용할 수 있는 boolean 값을 넣어주었다.
N = int(input())

los = N//5  # 5로 나누었을 때의 몫 값
count5 = 0  # 5개수 초기화
result = False  # for loop안에서 조건 만족시 True로 바꿔줄 boolean

for i in range(los,-1,-1):  # los부터 -1씩 0까지 loop :: 5가 MAX인 경우부터 MIN인 경우까지 차례대로 loop 실행
  if (N-5*i)%3 == 0:  # 5로 가져간 후 나머지 값을 3의 배수로 가져갈 수 있는지 확인(가져갈 수 있는 경우) 
    count5 = i  # 그때의 i값이 5의 개수
    result = True # 외부 조건문에서 사용
    break

if result == False: # 위 for loop에서 if 조건문에 한번도 적용된 적이 없는 경우 == N을 5와 3으로 분리할 수 없는 경우
  print(-1) 
else:
  count3 = (N - count5*5) // 3  # 3의 개수 계산 전체에서 5 가져갈 만큼 가져가고 나머지를 3으로 나눈 몫
  print(count3+count5)

