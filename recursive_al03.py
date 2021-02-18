# 스택을 이요하여 재귀함수 구현

from stack import Stack

def recur(n: int) -> int:
    """재귀를 제하건 recur() function"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break
x = int(input('정수값을 입력하시오: '))

recur(x)
""" 4를 전달 받을 때 처리 순서.
4를 스택에 푸시 -> n값을 1 감소시켜 3으로 만든다. continue문이 실행되어 while문으로 돌아간다 
첫번째 if 문은 반복하면서 스택에는 [4, 3, 2, 1]이 쌓인다 1까지 쌓은 후 n은 0 이 되고 첫번째 if 문은 실행되지 않는다.
 pop한 값은 bottom 값을 반환하고 포인터를 1감소시킨다 n에 1이 입력되고 출력 후 -1로 반환된다 비어질 때까지 두번째 if 문을 반복한다."""