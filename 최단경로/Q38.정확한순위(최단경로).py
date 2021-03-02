"""선생님은 시험을 본 학생 N명의 성적을 분실하고, 성적을 비교한 결과의 일부만 가지고있다.
학생 N명의 성적은 모두 다른데, 다음은 6명의 학생에 대하여 6번만 성적을 비교한 결과이다.

1번 학생의 성적 < 5번 학생의 성적
3번 학생의 성적 < 4번 학생의 성적
4 < 2
4 < 6
5 < 2
5 < 4

A번 학생의 성적이 B번 학생의 성적보다 낮다면 화살표가 A에서 B를 가리키도록 할 때, 위의 성적 결과를 다음 그림처럼 표현할 수 있다.
이 정보로 유추하여 순위를 정확히 알 수 있는 학생도 있고, 아닌 학생도 있다.
학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램을 작성하라."""

# 입력 : 첫 째 줄에 학생들의 수 N(2~500)과 두 학생의 성적을 비교한 횟수 M ( 2~10,000)이 주어진다.
# 다음 M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A와 B가 주어진다. 이는 A번 학생 성적 B번 학생보다 낮다는 것을 의미한다.
# 출력 : 첫 째 줄에 성적 순위를 정확히 알 수 있는 학생이 몇명인지 출력
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1



"""비용이 없고, 연결이 가능한지만 알면 되므로, 각 원소를 0으로 해놓고 ( 연결 X 라는 뜻) , 연결이 있으면 1로 바꿔줌
결과적으로 x행의 원소들 중 1인 것들의 열 index x보다 높은 노드들이고,
y행 x열의 원소들중 1인 것들은, y가 x보다 성적이 낮다는 보장이 되는 것들이다.
 
자신보다 높은것, 낮은 것들의 합이 n-1이 되면, 자신의 순위는 정확히 알 수 있는 것"""
for k in range(1, n+1):
    for i in range(1,n+1):
        for j in range(1, n+1):
            if graph[i][j] == 0 and graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] == 1 or graph[j][i] == 1:
            count += 1
    if count == n - 1:
        result += 1

print(result)