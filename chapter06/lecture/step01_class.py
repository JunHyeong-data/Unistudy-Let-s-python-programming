# 함수 정의
def calc_func(a, b): #외부함수
    x = a
    y = b
    
    def plus(): #내부함수
        p = x + y
        return p
    def minus(): #내부 함수
        m = x - y
        return m
    return plus, minus
#함수 호출
p, m = calc_func(10, 20)
print('plus =', p())
print('minus =', m())

#클래스 정의
class calc_class :
    x = y = 0
    #생성자
    def __init__(self, a, b):
        self.x = a #10
        self.y = b #20
    #클래스 함수
    def plus(self):
        p = self.x + self.y #변수 연산
        return p
    #클래스 함수
    def minus(self):
        m = self.x - self.y
        return m
#객체 생성
obj = calc_class(10, 20)

#멤버 호출
print('plus =', obj.plus())
print('minus =', obj.minus())