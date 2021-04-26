from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, key: Any, value, left: Node = None, right: Node = None):
        self.key =key
        self.value = value
        self.left = left
        self.right = right

class binarySearchingTree:
    def __init__(self):
        self.root = None

    '''Node class의 __init__()함수는 4개의 매개변수로 전달받은 값을 각 필드에 대입'''

 #search 함수는 이진트리에서 키를 값는 노드를 검색
    def search(self, key: Any) -> Any:

        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key: #key와 노드 p가 같으면
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
# Insert Node: Be careful that after insert Node, Tree have to maintain binary tree search conditions
# 노드를 삽입 할 위치를 찾은 뒤 수행한다
    def add(self, key : Any, value: Any) -> bool:

        def add_node(node: Node, key: Any, value:Any) -> None:
            """node를 root로 하는 subTree key가 key , 값이 value인 노드를 삽입"""
            if key == node.key: #key값이 이미 존재
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else: # 왼쪽 노드에 자식노드가 이미 존재하면, 주목노드를 왼쪽 자식으로 이동
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key,value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None: #Tree is empty ,key ,value, left right is None
            self.root = Node(key, value, None, None)
            return True
        else: #Tree is not empty, 내부함수 add_node()를 호출하여 노드 삽입
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None: # 더 이상 진행할 수 없는 경우
                return False

            if key == p.key: # key and Node's p Key is same
                break

            else:
                parent = p #가지를 내려가기 전에 부모를 설정
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:  #key > p.key
                    is_left_child = False
                    p = p.right #오른쪽 서브트레에서 검색한다.

        #자식노드가 없는 노드를 삭제하거나 자식노드가 1개인 노드를 삭제하는 경우
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right #부모의 왼쪽 포이터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.right

        else: #자식 노드가 2개인 노드를 삭제하는경우
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key # left의 키를 p로 이동
            p.value = left.value #left의 데이터를 p로 이동
            if is_left_child:
                parent.left =left.left #remove left
            else:
                parent.right = left.left
        return True

#모든 노드를 오름차순으로 출력하는 dump()함수
    def dump(self, reverse = False) -> None:
        def print_subtree(node: None): #node를 root로 하는 subTree's node를  키의 오름차순으로 출력
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key}  {node.value}')
                print_subtree(node.right) #오른쪽 서브트리르 오름차순으로 출력


        def print_subtree_rev(node: None):
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node:key}   {node:value}')
                print_subtree_rev(node.left)
        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

# 최대 키와 최소 키를 반환하는 min_key(), max_key()function
    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key






