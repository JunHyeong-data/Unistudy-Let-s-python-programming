import json
# json file 읽기
with open('c:/파이썬/chapter08/data/usagov_bitly.txt', mode='r', encoding='utf-8') as file:
    lines = file.readlines()

# json 디코딩
# file -> python dict 객체
rows = [ json.loads(row) for row in lines] 
print('rows :', len(rows))

# 10개 원소 출력
for row in rows[:10] :
    print(row) #행출력
    print(type(row))
    
# dict -> DataFrame 변환
import pandas as pd
recode_df = pd.DataFrame(rows)
print(recode_df.info)