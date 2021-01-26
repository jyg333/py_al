# 고정길이 스택 클래스 구현!!

"""스택은 데이터를 임시저장할 때 사용하는 자료구조이다. 데이터의 입력과 출력 순서는 후입선출 방식이다.
   푸시한 데이트를 저장하느 스택 본체는 list형 배열이다. stk[0] 부터 푸시받은 데이터를 저장한다.
   스택의 크기는 capacity로 int형 정수이다.
   예외처리: 프로그램을 실행하다 오류가 발생하면 예외처리 메시지를 내보낼 수 있다. 오류처리를 수행하면 오류를 복구하여 프로그램이 실행되다 중단되는
   것을 피할 수 있다. """

from typing import Any

class FixedStack:
    """고정길이 스택 클래스"""

    class Empty(Exception): #비어있는 FixedStack에 팝 또는 피크 할때 내보내는 예외처리
        pass

    class Full(Exception): #가득찬 FixedStack 애 푸시할 때 내보내는 예외처리
        pass

    def __init__(self, capacity: int = 256) ->None:
        self.stk = [None] * capacity # main body of stack
        self.capacity = capacity  #size of stack
        self.ptr = 0 # pointer of stack

    def __len__(self) -> int: #스택에 쌓여있는 데이터 개수를 반환
        return self.ptr

    def is_empty(self) -> bool: # 스택이 비어있는지 판단
        return self.ptr <= 0

    def is_full(self) -> bool: #스택이 가득 차 있는지 판단
        return self.ptr >=self.capacity


    """push()는 스택에 데이터를 추가, 스택이 가득차서 더 이상 푸시할 수 없을 때 FixeStack.Full을 통해서 예외처리
       pop()은 스택의 꼭대기에서 데이터를 꺼내서 그 값을 반, 스택이 비어있지 않으면 ptr을 1감소시킨다
       peek()는 스택의 꼭데이 데이트를 들여다본다. 데이터의 입출력이 없기 때문에 ptr은 변하지 않는다"""

    def push(self, value: Any) -> None:
        if self.is_full(): #case stack is full
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.str += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.str -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None: #clear all data
        self.ptr = 0 #스택의 포인터 값을 0으로 함으로 빈 스택을 만든다.


    """find() 는 스택 main body의 배열 stk안에 value와 값이 같이 데이터가 포함되어 있는지 확인하고, 위치를 검색
    count()는 스택에 쌓여있는 데이터(value)의 개수를 구하여 반환
    __contain__()는 tmxordp 데이터(value)가 있는지 판단. 있으면 True, 그렇지 않으면 False를 반환. 판단연산자 in을 사용하여 수행가능"""

    def find(self, value: Any) -> Any:
        for i in range(self.ptr -1, -1, -1): #꼭대기 부터 선형검색
            if self.str[i] == value:
                return i
            return -1

    def count(self, value: Any) ->bool:
        c = 0
        for i in range(self.ptr): #바닦 쪽부터 선형검색
            if self.stk[i] == value:
                c += 1
        return c

    def __contain__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) ->None: #dump: output all of data in stack from top to bottom
        if self.is_empty():
            print('Stack is empty')
        else:
            print(self.stk[:self.ptr])

