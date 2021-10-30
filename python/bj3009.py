# how to solve : 각 점들의 x,y값을 따로 list에 저장 후 loop을 돌며 리스트에서 해당 요소의 개수가 한개일 때 해당값을 출력하게 설계

x_list = []
y_list = []

for i in range(3):  # 각 점들의 x,y값을 각각의 list에 저장
  x , y = map(int,input().split())
  x_list.append(x)
  y_list.append(y)

for xl in x_list:   # list에서 요소의 개수가 한개인 요소 등장시 해당값 출력 
  if x_list.count(xl) == 1:
    print(xl,end=" ")
    break

for yl in y_list:   # list에서 요소의 개수가 한개인 요소 등장시 해당값 출력
  if y_list.count(yl) == 1:
    print(yl)
    break



