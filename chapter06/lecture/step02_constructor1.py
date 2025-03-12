#생성자 이용 멤버변수 초기화
class multiply3:
    #멤버 변수 없음
    #생성자 없음
    def data(self,x,y):
        self.x = x
        self.y = y
    #곱셈 연산
    def mul(self):
        result = self.x * self.y
        self.display(result)
    #결과 출력
    def display(self, result):
        print('곱셈 = %d' % (result))
obj = multiply3() #기본 생성자
obj.data(10, 20)
obj.mul()