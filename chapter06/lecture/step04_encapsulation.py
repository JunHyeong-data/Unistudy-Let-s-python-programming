# 부모 클래스
class Super :
    # 생성자 : 동적멤버 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 메서드
    def display(self):
        print(f"name : {self.name}, age : {self.age}")
sup = Super('부모', 55)
sup.display() # 부모 멤버 호출

# 자식 클래스
class Sub(Super) : # 클래스 상속
    gender = None # 자식 멤버
    # 생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 메서드 확장
    def display(self):
        print(f"name : {self.name}, age : {self.age}, gender : {self.gender}")
sub = Sub('자식', 25, '여자')
sub.display()