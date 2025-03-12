from statistics import mean #평균
from math import sqrt #제곱근

data = [4,5,3.5,2.5,6.3,5.5]

# 외부 함수 : 산포도 함수
def scattering_func(data): # outer
    dataSet = data # data생성
    # 내부 함수 : 산술평균 반환
    def avg_func():
        avg_val = mean(dataSet)
        return avg_val
    # 내부 함수 : 산술평균 반환
    def var_func(avg):
        diff = [(data - avg) ** 2 for data in dataSet]
        print(sum(diff)) # 차의 합
        var_val = sum(diff) / (len(dataSet)-1)
        return var_val
    # 내부 함수 : 표준편차 반환
    def std_func(var):
        std_val = sqrt(var)
        return std_val
    # 함수 클로저 반환
    return avg_func, var_func, std_func
# outer 호출
avg, var, std = scattering_func(data)
# 내부 함수 호출
print('평균 : ', avg())
print('분산 : ', var(avg()))
print('표준편차 : ', std( var(avg())))
    
        