# lesson : 소수 검사시 해당 값의 전값까지 계속 비교하는 것이 아니라 해당 값의 루트값까지 비교해보면 된다.

def isSosu(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isSosu(i):
        print(i)