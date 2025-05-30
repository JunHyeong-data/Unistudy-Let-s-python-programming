'''
csv -> db table
  1차 실행 : table 생성 -> 레코드 추가
  2차 실행 : 레코드 검색
'''

import pandas as pd
import pymysql

bmi = pd.read_csv("chapter10/data/bmi.csv")
print(bmi.info())
'''
height    20000 non-null int64 -> int
weight    20000 non-null int64 -> int
label     20000 non-null object -> varchar(20)
'''

height = bmi['height']
weight = bmi['weight']
label = bmi['label']

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # table 조회
    cursor.execute("show tables")
    tables = cursor.fetchall()
    sw = False
    for table in tables :
        #print(table) # ('bmi_tab',)
        #print(table[0]) # bmi_tab
        if table[0] == 'bmi_tab' :
            sw = True # table 있는 경우 swapping

    if not sw :
        print('테이블 없음')
        # table 없으면 생성
        sql="""create table bmi_tab(
        height int not null,
        weight int not null,
        label varchar(15) not null
        )"""
        cursor.execute(sql)

    cursor.execute("select * from bmi_tab")
    rows = cursor.fetchall()
    if rows : # 레코드 있는 경우 : 레코드 조회
        for row in rows :
            print(f"{row[0]}    {row[1]}    {row[2]}")

        print('전체 레코드 수 : ', len(rows))
    else: # 레코드 없는 경우 : 레코드 추가
        print("100 레코드 추가")
        for i in range(100) :
            h = height[i]
            w = weight[i]
            l = label[i]
            cursor.execute(f"insert into bmi_tab values({h}, {w}, '{l}')")
            conn.commit()

except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()


# exam04