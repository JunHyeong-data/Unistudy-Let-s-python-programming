# chapter06/myPackage/enumerate_dict.py

def list_enumerate(lst):
    """
    리스트의 요소를 enumerate()를 사용하여 인덱스와 함께 출력하는 함수
    """
    for i, value in enumerate(lst):
        print(f"색인: {i}, 내용: {value}")


def dict_enumerate(d):
    """
    딕셔너리의 키와 값을 enumerate()를 사용하여 출력하는 함수
    """
    for i, (key, value) in enumerate(d.items()):
        print(f"순서: {i}, 키: {key}, 값: {value}")


# 테스트 코드 (이 파일을 직접 실행하면 동작)
if __name__ == "__main__":
    sample_list = [1, 3, 5]
    sample_dict = {"name": "홍길동", "job": "회사원", "addr": "서울시"}

    print("🔹 리스트 열거형 출력")
    list_enumerate(sample_list)

    print("\n🔹 딕셔너리 열거형 출력")
    dict_enumerate(sample_dict)
