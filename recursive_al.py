# 재귀함수 기초
#1
# def factorial(n :int)-> int:
#     if n > 0:
#         return n * (factorial(n-1))
#     else:
#         return 1
#
# if __name__== '__main__':
#     n = int(input("출력할 팩토리얼 값을 입력하시오: "))
#     print(f'{n}의 펙토리얼을 {factorial(n)} 입니다.')

# 최대 공약수 구하기 (유클리드 호제법)

def gcd(x :int, y : int)-> int:
    if y == 0:
        return x
    else:

        return gcd(y, x%y)
# example // x = 10, y =30 -> (30, 10) -> (10, 0)  -> return x
# example2 //  x = 18, y =133 -> (133, 18) -> (18, 7) -> (7, 4) - >(4,3) -> (3, 1) -> (1, 0) return x

if __name__ =='__main__':
    print('두 정수값의 최대 공약수를 구합니다.')
    x = int(input("Input first integer: "))
    y = int(input("Input Second integer: "))

    print(f'GCD of Twp numbers is {gcd(x, y)}')
