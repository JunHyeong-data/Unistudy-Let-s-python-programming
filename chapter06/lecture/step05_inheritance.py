# 부모 클래스
class Parent :
    # 생성자 : 동적멤버 생성
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # 메서드
    def display(self):
        print(f"name : {self.name}, age : {self.job}")
p = Parent('홍길동', '회사원')
p.display() # 부모 멤버 호출

# 자식 클래스
class Children(Parent) : # 클래스 상속
    gender = None # 자식 멤버
    # 생성자
    def __init__(self, name, job, gender):
        self.name = name
        self.job = job
        self.gender = gender
    # 메서드 확장
    def display(self):
        print(f"name : {self.name}, age : {self.job}, gender : {self.gender}")
# 자식 클래스 객체 생성
chil = Children('이순신', '해군 장군', '남자')
chil.display()