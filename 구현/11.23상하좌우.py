"""여행가는 N x N 크기의 정사각형 공간 위에 서있다. 가장 왼쪽 위 좌표는 (1,1)이며, 여기서 출발한다.
여행가는 상, 하, 좌, 우 방향으로 이동할 수 있음, 시작 좌표는 항상 (1, 1)이다. 우리 앞에는 이동 계획서가 놓여있다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D중 하나의 문자가 반복적으로 적혀있다.
N x N크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
계획서가 주어졌을 때, 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오."""

#첫 째 줄에 공간의 크기를 나타내는 N이 주어진다. ( 1~ 100 사이)
#둘 째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (이동횟수 1~100 사이)
''' 첫 째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.'''

n = int(input())
data = list(input().split())

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dir = ['L', 'R', 'U', 'D']


for direction in data:   ##### 중요
    for k in range(len(dir)):  #range로 접근하지 않고 dir자체로 접근한다면, dx,dy 배열과의 접점을 인덱스로 만들어낼 수 없다!
        if direction == dir[k]:
            newx = x + dx[k]
            newy = y + dy[k]
            break

    if newx > n or newx < 1 or newy > n or newy < 1:
        continue
    x = newx
    y = newy

print('(', x, y, ')')


