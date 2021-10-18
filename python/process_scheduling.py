# Process Scheduling에서 Shortest-remaining-time-first 방식과 Round-Robin 방식 구현
print("|| Scheduling Type (SR, RR) >>  ",end="")
Type = input()
print("|| Process Number >>  ",end="")
N = int(input()) # process 개수

GantChart = []
if Type == "SR":
  print("|| Arrival Time(start from 0) >>  ",end="")
  Atime = list(map(int,input().split()))  # Arrival Time
  print("|| Burst Time(start from 0) >> ",end="")
  Btime = list(map(int,input().split()))  # Burst Time
  time = sum(Btime)

  for t in range(time): # 전체 비교 횟수 만큼 loop
    compareList = []
    for n in range(N):  # 비교할 프로세스들만 추림 매번의 비교 횟수에서 process가 시작했는지 끝났는지 체크 
      if Atime[n] <= t and Btime[n] > 0:  # Arrival Time이 해당 시간보다 작거나 같으면 시작된것 && Burst time이 0보다 커야지 아직 종료되지 않은 것
        compareList.append(n)
    compareList_Btime = [ Btime[comp] for comp in compareList]  # CompareList 각 element의 Btime으로 구성된 리스트
    index = compareList_Btime.index(min(compareList_Btime)) # 그중 최소값의 index
    Btime[compareList[index]] -= 1 # 최소값인 process의 Btime을 하나 줄여준다.
    GantChart.append(compareList[index]+1)  # 간트차트에 해당 프로세스 넣어준다.
else:
  print("|| Burst Time(start from 0) >> ",end="")
  Btime = list(map(int,input().split()))  # Burst Time
  print("|| Time Quantum >> ",end="")
  timeq = int(input())

  q_timer = timeq
  q_process = 1 # quantum time에 권한이 있는 process
  while sum(Btime) != 0: # 전체 비교 횟수 만큼 loop
    if q_timer == 0 or Btime[(q_process-1)] == 0 :
      q_process = q_process%N + 1
      q_timer = timeq
      continue
    Btime[(q_process-1)] -= 1
    GantChart.append(q_process)  # 간트차트에 해당 프로세스 넣어준다.
    q_timer -= 1



# for make Gantchart seen easier
print("[ GantChart ]")
count = 1
for idx in range(len(GantChart)): 
  if idx != len(GantChart)-1 and GantChart[idx] == GantChart[idx+1]:
    count += 1
    continue
  else:
    print("[ P",GantChart[idx],"] x ",count)
    count = 1



