# 중첩함수 정의
def main_func(num) :
    num_val = num #자료 생성
    def getter(): #휙득자 함수, return 있음
        return num_val
    def setter(value): # 지정자 함수 인수 있음
        nonlocal num_val #nonlocal 명령어
        num_val = value
    return getter, setter

# 외부함수 호출
getter, setter = main_func(100) #num 생성

# 휙득자 호출
print('num =', getter()) #휙득한 num 확인인

#지정자 휙득
setter(200) #num 값 수정
print('num =', getter()) #num 수정 확인인