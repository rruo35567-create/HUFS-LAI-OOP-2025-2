VERSION = "3.0"

def print_version_info() -> None: #(간단 출력)
    print(f"{VERSION}")

#gpt
# dict의 method에 무엇이 있는지 물어보고 그에 대한 개념을 물어보았습니다.

class Cache:
    def __init__(self) -> None: #내부 dict 초기화
        self._dict = {}
    
    def put(self, key, value) -> None:
        di = self._dict[key] = value
        return di

    def get(self, key, default=None):
        ge = self._dict.get(key, default = "None")
        return ge

    def __len__(self) -> int:
        le = len(self._dict)
        return le

    def clear(self) -> None:
        cl = self._dict.clear
        return cl

''' 오류 부분을 확실하게 모르겠어서 gpt에 돌려본 결과에서 코드는 
VERSION = "3.0"
def print_version_info() -> None:
    print(f"{VERSION}")

class Cache:
    def __init__(self) -> None:
        self._dict = {}

    def put(self, key, value) -> None:
        self._dict[key] = value

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def __len__(self) -> int:
        return len(self._dict)

    def clear(self) -> None:
        self._dict.clear()
이 나왔고, 변수의 수를 줄이는 것이 더 효율적이라서 채용할까 생각했지만 일단 저의 스타일로 코딩을 남기고 싶어 각주로 코드를 남기고 제 스타일 코드를 남겨놓겠습니다. '''

__all__ = ["Cache", "print_version_info", "VERSION"]
