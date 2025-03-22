import pandas as pd
import os

# 현재 작업 디렉터리 확인
print(os.getcwd())

# csv 파일 읽기
score = pd.read_csv('c:/파이썬/chapter08/data/score.csv', header = 0)
print(score.info)
print(score.head())

# 과목별 최고 점수
print('max kor =', max(score['kor']))
print('max eng =', max(score['eng']))
print('max math =', max(score['mat']))

# 과목별 최하 점수
print('min kor =', min(score['kor']))
print('min eng =', min(score['eng']))
print('min math =', min(score['mat']))

# 과목별 평균 점수
from statistics import mean

print('국어 점수 평균:', round(mean(score['kor']), 3))
print('영어 점수 평균:', round(mean(score['eng']), 3))
print('수학 점수 평균:', round(mean(score['mat']), 3))

# dept 빈도수
dept_count = {}
dept = score['dept']
for key in dept :
    dept_count[key] = dept_count.get(key, 0) + 1
print(dept_count)
    
    