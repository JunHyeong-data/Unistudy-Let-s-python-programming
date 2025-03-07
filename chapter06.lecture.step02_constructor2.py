class Datepro :
    # 멤버 변수
    content = "날짜 처리 클래스"
    # 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    # 객체 메서드(instance method)
    def display(self):
        print(f"{self.year}-{self.month}-{self.day}")
    # 클래스 메서드(class method)
    @classmethod # 함수 장식자
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]
        print(f"{year}년 {month}월 {day}일")
# 객체 멤버
date = Datepro(1995, 10, 25) #생성자
print(date.content)
print(date.year)
date.display()
# 클래스 멤버
print(Datepro.content)
Datepro.date_string('19951025')