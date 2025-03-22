import os

# 작업 디렉터리 변경
os.chdir('c:/파이썬/chapter08/lecture')
os.getcwd()

# 현재 작업 디렉터리 목록
print(os.listdir('.'))
# 디렉터리 생성
os.mkdir('test')
print(os.listdir('.'))

# 디렉터리 이동
os.chdir('test')
os.getcwd()

# 여러 디렉터리 생성성
os.makedirs('test2/test3')
print(os.listdir('.'))

# 디렉터터리 이동
os.chdir('test2')
print(os.listdir('.'))

# 디렉터터리 삭제 : 'test3' 삭제
os.rmdir('test3')
print(os.listdir('.'))

# 상위 디렉터터리 이동 : 상위 디렉터리 2개 이동
os.chdir('../..')
os.getcwd()

# 여러 개의 디렉터리 삭제
os.removedirs('test/test2')