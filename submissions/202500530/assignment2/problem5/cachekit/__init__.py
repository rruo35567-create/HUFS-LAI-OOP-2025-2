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
        ge = self._dict.get(key, default = None)
        return ge

    def __len__(self) -> int:
        le = len(self._dict)
        return le

    def clear(self) -> None:
        cl = self._dict.clear
        return cl

__all__ = ["Cache", "print_version_info", "VERSION"]
