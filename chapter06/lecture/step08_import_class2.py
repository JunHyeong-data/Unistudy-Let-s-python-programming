# 모듈 추가
import chapter06.myPackage.scattering
# 데이터 셋
data = [1,3,1.5,2,1,3.2]
# 산술평균 함수 호출
print('평균 :', chapter06.myPackage.scattering.Avg(data))
# 분산과 표준편차 함수 호출
var, sd = chapter06.myPackage.scattering.var_sd(data)
print('분산 :', var)
print('표준편차 :', sd)
# 모듈 추가
from chapter06.myPackage.scattering import Avg, var_sd
print('평균 :', Avg(data))

var, sd = var_sd(data)
print('분산 :', Avg(data))
print('표준편차 :', sd)