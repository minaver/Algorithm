# lesson : 시간초과 되었다. O(n^3)이 걸려 그런것 같다.

T = int(input())

while T != 0:
  x,y = map(int,input().split())
  a,b = 0,y-x-2
  
  move = 1
  count = 2
  end = True
  while end == True:
    for i in range(move+1,move-2,-1): # move+1 , move , move-1 에 대하여
      if a+i < b:
        a = a+i
        move += 1
        count += 1
        break
      elif a+i == b:
        count += 1
        end = False
        break
      # a+i > b 이면 for loop을 돌며 i 값을 줄여준다.
  T -= 1
  print(count)