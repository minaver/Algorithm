# lesson : 하나하나의 그림을 배열로서 바라봐 한줄 한줄을 기준으로 늘려나간다고 생각한다.
# -> 그냥 string으로 접근하면 바로 옆에 저장이 안된다
# ex) ***       * <- String으로 저장시 다음 차례에 여기에 붙일 수가 없다
#     * *
#     *** 의 경우 

def pattern(N):
  if N == 1:
    return ['*']
  
  star = []
  littleStar = pattern(N//3)

  for ls in littleStar:
    star.append(ls*3)
  for ls in littleStar:
    star.append(ls+' '*(N//3)+ls) 
  for ls in littleStar:
    star.append(ls*3)
  
  return star

N = int(input())
print('\n'.join(pattern(N)))

