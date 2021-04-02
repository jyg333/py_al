from typing import MutableSequence
def shaker_sort(a: MutableSequence):
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1): # 8부터 1까지 -1씩 감소하면서 진행
            print(f'check0: {j}')

            if a[j-1] > a[j]:
                a[j - 1], a[j] = a[j], a[j -1]
                print(f'check1: {j}')
                last = j
        left = last
        print(f'left: {left}')

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(f'check2 : {j}')
                last = j
        right = last
        print(f'right: {right}')
if __name__ =='__main__':
    print("Execute bubble_sort.")
    num = int(input("Input the Number of elements: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shaker_sort(x)

    print("All done!")
    for i in range(num):
        print(f'x[{i}] ={x[i]}')

'''출력을 통해서 진행과정을 지켜본결과, 첫번째 for 문은 나열된 원소를 맨 뒤에서 맨압으로 스캔하고 두번째 for문은  원소를 맨 앞에서 맨 뒤로 스캔한다
bubble sort 보다 비교횟수가 감소하여 개선된 효율을 보인다.'''




