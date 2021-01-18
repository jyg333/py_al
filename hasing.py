#해시법 :데이터의 추가, 삭제를 효율적으로 수행할 수 있는 방법
#이진 검색 후 데이터를 한칸씩 이동시켜준다.
#키와 해시값으 대응관계가 꼭 1:1 일 필요는 없다. 이처럼 저장할 버킷이 중복되는 현상을 충돌이라고 한다.
#해결방법으로는 chaining이 있다. 해시값이 같은 데이터를 연결 리스트에 의해 체인 모양으로 연결한다.

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node: #node that organizes hash

    def __init__(self, key:Any, value: Any, next: Node) -> Node:
        #initializing
        self.key = key  #임의의 자료형
        self.value = value  #임의의 자료형
        self.next = next  #뒤쪽 노드 참조

class ChainedHash:

    def __init__(self, capacity: int) -> Node:
        self.capacity = capacity
        self.table = [None] * self.capacity


    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    #해시 테이블의 각 버킷은 맨 앞부터 table[0],table[1], ..table[capacity-1] 순으로 접근할 수 있다.
    #__init__ 함수가 호출된 직후 배열 table의 모든 원소는 None 이고 버킷이 빈 상태이다.
    #sha256 알고리즘: haslib 모듈에서 제공하는 sha256은 문자열의 해시값을 구하는 해시 알고리즘의 생성자이다.
    #encode() 함수: hahlib.sha256에는 바이트 문자열의 인수를 전달해야한다. 그래서 key를 str형 문자열로 변환한 뒤 그 문자열을 encode()함수에 전달하여 바이트 문자열을 생성
    #hexdigest: sha256 알고리즘에서 해시값을 16진수 문자열로 꺼낸다.

    def searching(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
