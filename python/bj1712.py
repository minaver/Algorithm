# lesson :
# loop이 길어지면 시간초과를 유발한다. 
# 즉, 쉽게 계산하여 접근할 수 있는 문제는 컴퓨터에게 loop으로 시키지말고 내가 계산해서 준다!

import sys

fix_price , prd_price , sel_price = map(int, sys.stdin.readline().split())

num = 1

if prd_price >= sel_price :
  print(-1)
else:
  # if fix_pirce가 굉장히 큰 값, sel_price - prd_price가 굉장히 작은 값이면 
  # 상당히 많은 loop을 돌아야 한다. 비록 O(n)이지만 효율성이 떨어지는 문제를 야기한다.
  while True: 
      if fix_price + prd_price * num < sel_price * num :
        break
      num = num +1

  print(num)
