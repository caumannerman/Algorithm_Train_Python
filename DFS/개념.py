''':keyword
DFS, BFS
STACK
QUEUE ( DEQUE )
RECURSIVE FUNCTION

'''

# dfs, bfs 는 stack과 queue를 많이 씀. 출제도 많이 하므로 잘 알아둬야함.
# list와 append(), pop()을 이용해 스택기능 다 쓸 수 있다.


#from collections import deque 해주면 덱 -> 스택, 큐 기능 모두 있음!!!!
# stack은 그냥 리스트 쓰는게 보편적 .    덱은deque import해서 append(), popleft()쓰면 됨

# 재귀함수 (Recursive function)  자기 자신을 다시 호출 .  -재귀함수로 만들 수 있는 것들은  무조건 반복문으로도 만들 수 있다.

따라서 어떤게 해당 문제에서 유리할지 판단해서 선택사용. stack을 사용해야할 때 구현 상 스택 라이브러리 대신에 재귀함수를 이용하는경우 많음.

DFS(Depth-First Search) 깊이우선탐색 -> STACK 사용

BFS 너비우선탐색  가까운 노드부터 우선적으로 탐색
큐 자료구조를 이용

각 노드는 2차원 list로 표현한다. 단, 0번 인덱스 리스트는 비워둔다. 노드들이 1번부터 있으므로.

------------------------------------------------------------------------------
그래프 (Node(Vertex) + Edge)를 데이터로 나타내는 방법 2가지

    1. Adjacency Matrix (인접 행렬)
        -> (n,m)은 n번 노드에서 m번 노드로 가는 비용을 나타냄. 따라서 대각선 위치는 모두 0 {(n,n)이므로}
    2. Adjacency List (인접 리스트 )
        -> Node갯수만큼 행이 존재하는 2차원 리스트를 만들고, n번째 행에는 (연결된 노드번호, 비용)을 각각 원소로 채워넣는다. (리스트.append()이용)

 정리 : 인접 행렬은 모든 관계를 저장하므로, 메모리 낭비. but 접근 빠름!
       인접 리스트는 연결된 것만 저장하므로 메모리 효율적! but 접근이 느림
 -> 어떤 노드에 연결된 모든 노드를 순회해야하는 경우, 인접 리스트가 낫다.(접근 효율 크게 차이X, 메모리 효율 좋으므로 )


INF =10000000
  그래프는 비용이 있는 경우 // 비용이 없는  단순 연결 그래프로 나눌 수 있다.

 비용이 없는 경우 인접 행렬은 [[0,0,0,1], [0,1,1,0], [INF,1,0,0]...]과 같이 0,1,INF만으로 채운다.
 비용이 없는 경우 인접 리스트는 [[2,3,8],[1,7], [1,4,5], [3,5], [3,4]]와 같이 연결된 노드 번호로 채운다.

비용이 있는 경우 인접행렬은 [[0,23,4,6], [23,0,INF,5], [1,3,0,INF]...] 과 같이 각 노드 번호에 대응하는 인덱스에 비용의 크기와 INF로 채운다
비용이 있는 경우 인접 리스트는 [[(2,7),(5,10)], [(1,7),(5,2)]...] 과 같이 행의 인덱스의 대응하는 노드에 인접한 노드의 번호와 비용을 쌍으로 채운다.


4가지 경우를 모두 코딩해본 결과, 비용이 있는 경우는 인접행렬 // 비용이 없는 경우는 인접리스트로 만드는 것이 코딩하는 입장, 보는 입장에서 편하다.
