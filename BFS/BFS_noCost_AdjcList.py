"""BFS는 너비우선 탐색  Breadth First Search"""
''' 일반적으로 실제 수행시간이 DFS보다 좋은 편이라고 한다.. 시간복잡도는 O(N)'''
#  1. 탐색시작노드를 큐에 삽입 + 방문처리
   # 2. 큐에서 하나를 꺼내, 해당 노드의 인접 노드 중에서 방문X 노드를 모두 큐에 삽입 + 방문처리
   # 3. 2번을 수행할 수 없을 때까지 반복


from collections import deque

graph = [ [], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]

visited = [False]*9

queue = deque([])

def bfs( graph, visited, vertex):
    queue.append(vertex)
    visited[vertex] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



bfs(graph, visited, 1)



