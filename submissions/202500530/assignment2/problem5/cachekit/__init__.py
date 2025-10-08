VERSION: "3.0"

def print_version_info() -> None: #(간단 출력)
    print(f"{VERSION}")

#gpt
# dict의 method에 무엇이 있는지 물어보고 그에 대한 개념을 물어보았습니다.

class Cache:
    def __init__(self) -> None: #내부 dict 초기화
        self._dict = {}
    
    @property
    def _dict(self) -> dict:
        return self._dict
    
    @_dict.setter
    def put(self, key, value) -> None:
        self._dict[key] = value
        return self._dict

    def get(self, key, default=None):
        self._dict.get(key, default = None)
        return self._dict

    def __len__(self) -> int:
        le = len(self._dict)
        return le

    def clear(self) -> None:
        self._dict.clear
        return self._dict

__all__ = ["Cache", "print_version_info", "VERSION"]