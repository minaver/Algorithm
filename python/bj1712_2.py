# lesson 
# loop이 길어지면 시간초과를 유발한다. 
# 즉, 쉽게 계산하여 접근할 수 있는 문제는 컴퓨터에게 loop으로 시키지말고 내가 계산해서 준다!

import sys

fix_price , prd_price , sel_price = map(int, sys.stdin.readline().split())

if prd_price >= sel_price :
  print(-1)
else:
  num = fix_price // ( sel_price - prd_price ) +1
  print(num)