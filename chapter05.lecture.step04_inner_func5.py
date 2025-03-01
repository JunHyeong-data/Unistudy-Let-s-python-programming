# 재귀함수 정의 : 1~n 카운트
def Counter(n) :
    if n == 0 :
        return 0 #종료조건
    else :
        Counter(n-1) #5 -> 4 -> 3 -> 2 -> 1 [0]
        print(n, end=' ')
#함수 호출1
print('n=0 :', Counter(0))

#함수 호출2
Counter(5)