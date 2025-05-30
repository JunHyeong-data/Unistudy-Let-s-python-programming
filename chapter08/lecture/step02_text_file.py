# 파일 읽기 관련 함수
try :
    #(1) read() : 전체 텍스트 자료 읽기
    ftest = open('C:/파이썬/chapter08/data/ftest.txt', mode = 'r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))
    
    #(2) readlines() : 전체 텍스트 줄 단위 읽기
    ftest = open('C:/파이썬/chapter08/data/ftest.txt', mode = 'r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단 수:', len(lines))
    
    #(3) list -> 문장 추출
    docs = []
    for line in lines :
        print(line.strip) # text만 출력
        docs.append(line.strip())
    print(docs)
    
    #(4) readline() : 한 줄 읽기
    ftest = open('C:/파이썬/chapter08/data/ftest.txt', mode = 'r')
    line = ftest.readline()
    print(line)
    print(type(line))
except Exception as e:
    print('Error 발생 :', e)

finally :
    # 파일 객체 담기
    ftest.close()