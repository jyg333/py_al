from enum import Enum
from BST import binarySearchingTree


"""key should be Integer,
value is string."""
Menu = Enum("Menu",["Insert","Remove","Search","Dump","Range","Exit"])

def select_Menu() -> Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep=' ', end= "")
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = binarySearchingTree()  #이진트리 검색 생성

while True:
    menu = select_Menu()

    if menu == Menu.Insert:
        key = int(input('Input the inserted key: '))
        value = input("Input the inserted value: ")
        if not tree.add(key, value):
            print("Fail to insert.")

    elif menu == Menu.Remove:
        key = int(input("Input the key removed: "))
        tree.remove(key)

    elif menu == Menu.Search:
        key = int(input("input the key that you searching: "))
        t = tree.search(key)
        if t is not None:
            print(f'The value of this key is {t}')
        else:
            print("There is no matching Data")

    elif menu == Menu.Dump:
        tree.dump()

    elif menu == Menu.Range:
        print(f'Minimum key is {tree.min_key()}.')
        print(f'Maximum key is {tree.max_key()}.')

    else:
        break

