# for loop version

N = int(input())

fac = 1

if N == 0:
    print(fac)
else:
  for n in range(2,N+1):
      fac *= n 
  print(fac)