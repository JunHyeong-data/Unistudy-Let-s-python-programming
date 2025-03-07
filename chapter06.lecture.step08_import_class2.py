# chapter06/myPackage/datetime_util.py

import datetime
from datetime import date, time

# 특정 날짜 객체 생성
today = date(2025, 3, 7)  # 날짜 객체 생성
print(today)

# 날짜 객체 멤버 변수 호출
print(today.year)
print(today.month)
print(today.day)

# 날짜 객체 메서드 호출
w = today.weekday()  # 요일 정보 (0=월요일, 6=일요일)
print("요일 정보:", w)

# 특정 시간 객체 생성
currTime = time(11, 55, 30)  # 시간 객체 생성
print(currTime)

# 시간 객체 멤버 변수 호출
print(currTime.hour)
print(currTime.minute)
print(currTime.second)

# 시간 객체 메서드 호출
isoTime = currTime.isoformat()  # ISO 8601 형식 변환
print(isoTime)
