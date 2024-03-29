"""그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을
먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""
# 입력 : 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
# 출력 : 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.


from collections import deque

n, m, v = map(int, input().split())
#그래프를 인접리스트로 만들지, 인접 행렬로 만들지 고민하다가, 인접 행렬이 접근하는데 훨씬 빠를 것으로 판단하여 인접행렬로 그래프 생성
graph = [[0] * (n + 1) for _ in range(n+ 1)]
dfs_result = []
# dfs와 bfs의 방문 노드를 차례로 담을 리스트. 두 경우 모두 visited를 판단하는 역할도 함.
bfs_result = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
#양방향그래프이므로 간선을 양 쪽에 설정해줘야

def dfs(start):
    dfs_result.append(start)
    for i in range(n + 1):
        if graph[start][i] == 1 and (i not in dfs_result):
            dfs(i)


def bfs(start):
    bfs_result.append(start)
    q = deque()
    q.append(start)
    while q:
        tmp = q.popleft()
        for i in range(n + 1):
            if graph[tmp][i] == 1 and i not in bfs_result:
                bfs_result.append(i)
                q.append(i)


bfs(v)
dfs(v)
print(*dfs_result)
print(*bfs_result)



""" ***************************** TIP *************************************

    문제 요구조건 상, 방문 node를 차례로 저장해야함. ==> 저장하는 list를 visited를 판단하는데 사용할 수 있다.
    따라서 visited 리스트를 따로 만들지 않아도 된다!!!
    
    """