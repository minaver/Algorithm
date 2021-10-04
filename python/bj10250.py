# lesson
# 1. 예외 상황에 대한 고려를 항상 해야한다. 
# - 그렇다면 어느 상황에 예외가 발생하는가? 
# - case inital / case final / case quarter를 유심히 살피자 
# 해당 문제는 case quarter( % 결과가 max에서 0으로 바뀌는 경우 )에서 예외 발생
import sys

T = int(input())

for i in range(T):
  h, w, n = map(int,sys.stdin.readline().split()) 

  if n % h == 0 :
    room = n//h
    floor = h
  else :
    room = n // h 
    floor = n - room*h
    room += 1

  print(floor*100+room)