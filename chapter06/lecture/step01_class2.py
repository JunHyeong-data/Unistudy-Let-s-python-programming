class Car:
    # 멤버 변수
    cc= 0 #엔진 cc
    door = 0 # 문짝 개수
    carType = None # null
    
    # 생성자
    def __init__(self, cc, door, carType):
        # 멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType #승용차, suv
    
    # 메서드
    def display(self):
        print(f"자동차 {self.cc}이고, 문짝은 {self.door}개, 타입은 {self.carType}")
    
# 객체 생성
car1 = Car(2000, 4, '승용차') # 객체 생성 + 초기화
car2 = Car(3000, 5, 'suv')
    
#멤버 호출 : object.member()
car1.display() # car1 멤버 호출
car2.display() # car2 멤버 호출출