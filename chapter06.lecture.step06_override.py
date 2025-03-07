# 부모클래스
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass
# 자식클래스 : 정규직
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)
    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print(f"총 수령액 : {self.pay}")
# 자식클래스 : 임시직
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)
    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print(f"총 수령액 : {self.pay}")
# 객체 생성
p = Permanent('이순신')
p.pay_calc(3000000,200000)
t = Temporary('홍길동') 
t.pay_calc(15000, 80)       