import json
# json 인코딩
user = { 'id' : 1234, 'name' : '홍길동'} #python dict
print(type(user))
print(user['name'])

# json 인코딩
jsonstring = json.dumps(user, ensure_ascii=False)
# ascill 인코드 방식 적용안함

# 문자열 출력
print(jsonstring)
print(type(jsonstring))

# json 디코딩
pyobj = json.loads(jsonstring)
print(type(pyobj))

# dict 자료확인
print(pyobj['name'])
for key in pyobj :
    print(key, ':', pyobj[key])