# lesson : 숫자가 지나치게 클 경우에 C,Java의 경우 에러를 출력한다 허나 파이썬은 괜찮다 
# C, Java에서 안 괜찮은 이유 : 만약 어떤 수가 50자리수라고 가정하면 적어도 10^50개의 정보를 담을 수 있는 메모리가 필요할 것이다
# 이는 log2(10^50) = 166.xx 이고 즉, 167bit 21byte가 필요하다는 것을 의미한다. 이를 한번에 관리할 수 있는 변수타입은 존재하지 않는다.
# 이때 Java에서는 BigInteger 라는 라이브러리를 사용하여 해당 자리수의 수들을 처리할 수 있다. 
# 그렇다면 파이썬은 괜찮은 이유 : 파이썬은 int형을 4byte 같이 단순하게 저장하는 것이 아니라 arbitrary precision integer 형태로 지원한다.
# 내부 구조는 다음과 같다
# struct{
#   ssize_t ob_refcnt;  # 메모리가 얼마나 많은 변수에 의해 접근되고 있는지
#   struct _typeobject *ob_type;  # 정수의 기본정보
#   ssize_t ob_size;  # 이 변수가 4byte 단위로 몇개를 할당중인지
#   uint32_t ob_digit[1]; # 변수에 저장한 값
# }
# 이러한 방식으로 원소마다 "0~2^30-1" 까지의 수를 저장할 수 있다

A,B = map(int,input().split())
print(A+B)
