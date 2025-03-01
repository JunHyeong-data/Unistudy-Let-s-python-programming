#래퍼 함수
def wrap(func):
    def decorated():
        print('방가워요!') #시작 부분에 삽입
        func() #인수로 넘어온 함수(hello)
        print('잘가요!') #종료 부분에 삽입
    return decorated #클로저 함수 반한
# 함수 장식자 적요
@wrap
def hello():
    print('hi ~ ', '홍길동')
    
# 함수 호출
hello()