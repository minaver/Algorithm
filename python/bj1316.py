import sys

number = int(input())
count = 0
isTrue = True
indexArray = []

for i in range(number):
  word = (sys.stdin.readline().rstrip())

  if len(word) == 1 :
    count = count + 1
    break

  for target in word :
    index = -1
    
    i = 0
    while True:
      index = word.find(target,index+1)
      indexArray.append(index)

      if i > 0 :
        if indexArray[1] == -1:
          break
        
        if indexArray[i-1] != indexArray[i] - 1 :
          isTrue = False
          break

      i = i+1 

      if index == -1:
        break

  if isTrue == True :
    count = count +1

print(count)  




