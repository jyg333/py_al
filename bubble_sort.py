# 이웃한 두 원소의 대소 관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘

from typing import MutableSequence

def bubble_sort(a ) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j -1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                '''뒤의 원소보다 앞으 원소의 크기가 크면 순서를 바꿔준다, Bubble_sort의 핵심코드이'''

if __name__ =='__main__':
    print("Execute bubble_sort.")
    num = int(input("Input the Number of elements: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print("All done!")
    for i in range(num):
        print(f'x[{i}] ={x[i]}')


