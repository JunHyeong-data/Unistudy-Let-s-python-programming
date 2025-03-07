class Account:
    # 은닉 멤버변수
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNo = None #계좌변호
    # 생성자: 멤버변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no
    # 계좌정보 확인 : Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo
    # 입금하기 : Setter
    def deposit(self, money):
        if money < 0 :
            print('금액 확인')
            return # 종료
        self.__balance += money
    # 출금하기 : Setter
    def withdraw(self, money) :
        if self.__balance < money:
            print('잔액 부족')
            return
        self.__balance -= money
# 객체 생성
acc = Account(1000, '홍길동', '125-152-4125-41') # 생성자
# Getter 호출
bal = acc.getBalance()
print('계좌 정보 :', bal)
# Setter 호출
acc.deposit(10000)
bal = acc.getBalance()
print('계좌정보 :', bal)            