# lesson : 재귀문은 함수안에 자기 자신이 들어가 자기 자신을 계속해서 호출하게 구현
# 재귀 손 테스트시 적당한 수를 골라 테스트했다. 여기서는 3,4에 대해 어떠한 느낌으로 구현되는지 테스트함

def pivo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return pivo(n-1) + pivo(n-2) 
  

n = int(input())
p = pivo(n)

print(p)