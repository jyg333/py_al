# deque 를 이용한 stack 구현

from typing import Any
from collections import deque
# 동작은 이전에 작성한 fixed_stack과 같지만 표준 라이브러리를 사영해서 동작이 빠르다.

class Stack:

    def __init__(self, maxlen: int=256) -> None:
        """stack initializing"""
        self.capacity = maxlen #maxlen은 deque의 최대 크기를 나타내는 속성으로 읽지 전용이다. 그게 제한이 없으면 None다.
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수 반환"""
        return len(self.__stk)

    def is_empty(self) ->bool:
        """스택이 비어 있는지 판단"""
        return not self.__stk

    def if_full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        self.__stk.append(value)

    def pop(self) -> Any:
        return self.__stk.pop()

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        """스택에서 value 를 찾아 인덱스를 반환하지 못하먄 -1 을 반환"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value : Any) -> bool:
        """스택에  value 가 포함되어 있는지 판단"""
        return self.count(value)

    def dump(self) -> int:
        """스택안에 있는 모든 데이터를 나열 bottom -> top"""
        print(list(self.__stk))

