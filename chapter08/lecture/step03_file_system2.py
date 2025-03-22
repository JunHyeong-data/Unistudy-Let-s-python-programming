import os
# 텍스트 디렉터리 경로 지정
print(os.getcwd())
txt_data = 'C:/파이썬/chapter08/txt_data/' # 상대경로 지정
# 만약 경로에 first와 second가 없다면면
# os.chdir('C:/파이썬/chapter08/txt_data/')
# os.mkdir('first')
# os.mkdir('second')
# 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir)

# 디렉터리의 텍스트 자료 수집 함수
def textPRo(sub_dir) :
    first_txt = []
    second_txt = []
    
    # 디렉터리 구성
    for sdir in sub_dir :
        dirname = txt_data + sdir # 디렉터리 구성
        file_list = os.listdir(dirname) # 파일 목록 반환
        
        # 파일 구성
        for fname in file_list :
            file_path = dirname + '/' + fname # 파일 구성
            
            # file 선택
            if os.path.isfile(file_path) :
                try :
                    # 텍스트 자료 수집
                    file = open(file_path, 'r')
                    if sdir == 'first':
                        first_txt.append(file.read())
                    else :
                        second_txt.append(file.read())
                except Exception as e:
                    print('예외발생 :', e)
                finally :
                    file.close() 
    return first_txt, second_txt # 텍스트 자료 반환

# 함수 호출
first_txt, second_txt = textPRo(sub_dir)

# 수집한 텍스트 자료 확인
print('firtst_tex 길이 =', len(first_txt))
print('second_txt 길이 =', len(second_txt))

# 텍스트 자료 결합
tot_texts = first_txt + second_txt
print(tot_texts)
print(type(tot_texts))