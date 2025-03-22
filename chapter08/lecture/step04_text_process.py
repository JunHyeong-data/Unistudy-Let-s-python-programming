import os 
from glob import glob

# 이미지 파일 경로
print(os.getcwd())
img_path = 'c:/파이썬/chapter08/images/'
img_path2 = 'c:/파이썬/chapter08/images2/'

# 디렉터리 존재 유무
if os.path.exists(img_path) :
    print('해당 디렉터리가 존재함')
    # 이미지 파일 저장, 파일 이동 디렉터리 생성
    images = []
    # os.mkdir(img_path2) 없을때 사용
    # 이미지 디렉터리에서 png 검색
    for pic_path in glob(img_path + '*.png') :
        # 경로와 파일명 분리, 파일명 추가
        img_path = os.path.split(pic_path)
        images.append(img_path[1])
        
        # 이진파일 읽기
        with open(file = pic_path, mode='rb') as rfile :
            output = rfile.read()
        with open(img_path2 + img_path[1], mode='wb') as wfile :
            wfile.write(output)
else :
    print('해당 디렉터리가 없음')
print('png file =', images)