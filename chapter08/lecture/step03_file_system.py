import os.path

#현재 경로 확인
print(os.getcwd())
# 경로 변경
os.chdir('c:/파이썬/chapter08')
print(os.getcwd())

# lecture 디렉터리의 step01_try_except.py 파일 절대경로
print(os.path.abspath('step01_try_except.py'))

print(os.path.dirname('lecture/step01_try_except.py'))

print(os.path.exists('C:/파이썬/workspace'))

print(os.path.isfile('lecture/step01_try_except.py'))

print(os.path.isdir('lecture'))

os.path.split('C:/test/test1.txt')
os.path.join('C:/test', 'test1.txt')

# step01_try_except.py 파일 크기
os.path.getsize('lecture/step01_try_except.py')