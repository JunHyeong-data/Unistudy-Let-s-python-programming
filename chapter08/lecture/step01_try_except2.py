#(1) 현재 작업디렉터리
import os 
print('\n현재 경로 :', os.getcwd())

#(2) 예외 처리
try :
    #(3) 파일 읽기
    ftest1 = open('C:/파이썬/chapter08/data/ftest.txt', mode = 'r')
    print(ftest1.read()) # 파일 전체 읽기
    
    #(4) 파일 쓰기
    ftest2 = open('C:/파이썬/chapter08/data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~')
    
    #(5) 파일 쓰기 + 내용 추가
    ftest3 = open('C:/파이썬/chapter08/data/ftest2.txt', mode = 'a')
    ftest3.write('\nmy second text~~~')
except Exception as e:
    print('Error 발생', e)

finally :
    ftest1.close()
    ftest2.close()
    ftest3.close()