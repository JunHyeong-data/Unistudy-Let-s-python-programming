print('\n유형별 예외처리')

try:
    div = 1000 / 2.53
    print('div = %5.2f' % div)  # 정상 실행
    div = 1000 / 0  # 1차: 산술적 예외 발생
    f = open('c:\\test.txt')  # 2차: 파일 열기 예외 발생 가능
    num = int(input('숫자 입력: '))  # 3차: 기타 예외 발생 가능
    print('num =', num)

# 다중 예외처리 클래스
except ZeroDivisionError as e:  # 산술적 예외 처리
    print('오류 정보:', e)
except FileNotFoundError as e:  # 파일이 존재하지 않는 경우 예외 처리
    print('오류 정보:', e)
except Exception as e:  # 기타 예외 처리
    print('오류 정보:', e)
finally:
    print('finally 영역 - 항상 실행되는 영역')
