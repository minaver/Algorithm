# lesson 
# ex) a b v 각각 5 1 10
# 4*n +5 >= 10 >> n >= 5/4 
# (a-b)*n + a >= v >> n >= (v-a)/(a-b)
# 즉 (v-a)/(a-b)보다 크면 성공 조건이다! 이때 좌항의 마지막 +a 횟수도 더해줘야 하므로 +1을 해주다.

import sys
import math

a, b, v = map(int,sys.stdin.readline().split())

n = math.ceil((v-a)/(a-b)) +1 # 올림함수를 이용해 (v-a)/(a-b)보다 크게 변환 & +1

print(n)