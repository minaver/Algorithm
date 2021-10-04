# lesson
# 1. 분기에서의 조건 분류
# 2. low_room = room(39) 같은 갱신 위치가 어디일지 정확하게 확인. 
# <- 갱신위치를 잘못 잡아 i%n == 0 일때만 갱신해야 하는데 계속 갱신하고 있었다.
# 3. 좀더 간편한 알고리즘을 찾자 이번 room[count -1] = room[count -2] + low_room[count-1] 처럼
T = int(input())

for t in range(T):
  k = int(input())  # k층
  n = int(input())  # n호

  low_room = [] # 전층 리스트
  room = [0 for _ in range(n)]  # 해당층 리스트

  if n == 1:  # 1호 기준은 모두 1이므로 바로 1 출력
    print(1)
  else: 
    for i in range(1,k*n+1):  # O(n^2)을 만들지 않기 위해 O(n)으로 1차원 loop 돌림 -> i%n == 0 일때 분기하도록!
      count = i%n # 층별 호수를 나타내줌 (1~n-1,0) 이때 마지막에 0으로 리턴되므로 case 나눠 처리해주어야
      if i <= n:  # 초기 1층 만들때 한에서만 빈 배열에 append 사용하여 low_room 초기화
        if count == 1:  # 101동은 1
          low_room.append(1)
        else:
          if count != 0:  # count : 1~n-1
            low_room.append( low_room[count-2] + i )
          else: # count : 0( count == n ) & 층이 바뀌는 분기점
            low_room.append( low_room[n-2] + i )
        
      else:
        if count == 1:  # 각 층 1동은 1
          room[count-1] = 1
        else:
          if count != 0:  # count : 1~n-1
            room[count -1] = room[count -2] + low_room[count-1] 
          else: # count : 0( count == n ) & 층이 바뀌는 분기점
            room[n -1] = room[n-2] + low_room[n-1]
            low_room = room # 층이 바뀌는 분기점이므로 low_room 값을 room 값으로 갱신
      
    print(low_room[len(low_room)-1])