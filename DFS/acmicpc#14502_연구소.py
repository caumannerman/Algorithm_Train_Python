"""인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
"""
#입력 : 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
#둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
#빈 칸의 개수는 3개 이상이다.
# 출력 : 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

from itertools import combinations
import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().strip().split())
data = []
virus = []
for _ in range(n):
    data.append(list(map(int, input().strip().split())))
zero = []

for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            virus.append((i, j))
        if data[i][j] == 0:
            zero.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
zero_num = len(zero)

# 복잡한 문제일수록 꼭 필요한 별개의 기능은 함수로 구현해놓고 본 연산을 코딩하는게 머리가 안 복잡해지고 좋다.
def spread_virus(newdata, x, y):
    newdata[x][y] = 2
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]

        if newx < 0 or newy < 0 or newx >= n or newy >= m:
            continue
        if newdata[newx][newy] == 0:
            spread_virus(newdata, newx, newy)

# 맵이 최대 8* 8이므로 그렇게 크지 않다. 모든 경우를 어찌되었든 다 체크해줘야하므로, 세군데 고르기 위한 모든 경우를 combinations를 이용하여 구했다.
combi = list(combinations(zero, 3))
result = -1

for i in combi:
    newdata = copy.deepcopy(data)
    for j in i:
        newdata[j[0]][j[1]] = 1
    for k in virus:
        spread_virus(newdata, k[0], k[1])
    safe = sum(s.count(0) for s in newdata)
    if result < safe:
        result = safe

print(result)