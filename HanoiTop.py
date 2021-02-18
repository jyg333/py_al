# 하노이 탑 구현

def move(no: int, x: int, y : int) -> None:
    if no > 1:
        print(f"1.{no}, {x}, {y}")
        move(no -1, x, 6 -x -y)
        print(f"2.{no}, {x}, {y}")

    print(f'원반 [{no}]을 {x}의 기둥에서 {y}의 기둥으로 옮긴다.')

    if no > 1:
        move(no -1, 6 - x - y, y)

print("하노이의 탑을 구현합니다.")

n = int(input("Input the number of circles:"))

move(n, 1, 3)

# 기둥번호를 정숫값 1,2,3으로 나타내서 기둥번호의 합인 6을 시작으로 위치를 나타낼 수 있다.
# simulation: (3,1,3) -> (2,1,2) -> (1,1,3) print -> no > 1 조건을 충족하지 않는다 생각하여 5번줄과 7번줄을 추가하여 과정을 보았다