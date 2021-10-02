
import sys

T = int(input())

for i in range(T):
  h, w, n = map(int,sys.stdin.readline().split()) 
  # 6 12 71
  if h >= n:
    room = 1
    floor = n
  elif n % h != 0 :
    room = n // h 
    floor = n - room*h
    room += 1
  else :
    room = w
    floor = h

  if(room < 10):
    room = "0"+str(room)

  print(floor,room ,sep="")