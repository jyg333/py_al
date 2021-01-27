#고정길이 스택 클래스 FixedStack 사용하기

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu',['Push', 'Pop','Searching','Peek','Dump','Quit'])

def select_menu() ->Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ',end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64) #Stack can be push Max to 64

while True:
    print(f'The number of data: {len(s)} / {s.capacity}')
    menu = select_menu() #메뉴선택

    if menu == Menu.Push:
        x = int(input('Input the data: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print("Stack is Full")

    elif menu == Menu.Pop:
        try:
            x = s.pop()
            print(f'Popped data is {x}.')
        except FixedStack.Empty:
            print("Stack is empty")

    elif menu == Menu.Peek:
        try:
            x = s.peek()
            print(f'Peeked data is {x}')
        except FixedStack.Empty:
            print("Stack is empty")

    elif menu == Menu.Searching:
        x = int(input("Input what you searching for: "))
        if x in s:
            print(f'Includes {s.count(x)} amount, Location of Front is {s.find(x)}.')
        else:
            print("Can't find that you searching for.")

    elif menu == Menu.Dump:
        s.dump()
    else:
        break

        # Searching 에서 오류를 발견했는데 모듈 fixed_stack find 함수에서 오타가 있었음.
        # pop 에서도 오류가 발견됨
        # "Popped data is <bound method FixedStack.pop of <fixed_stack.FixedStack object at 0x102c4a250>>."
        #위와같은 오류가 발생함 : 함수 pop에서 x =s.pop -> x = s.pop()로 수정
