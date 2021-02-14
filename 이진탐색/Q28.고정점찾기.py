"""고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다. 예를 들어, 수열 a = {-15, -4, 2, 8,13}이 있을 때 a[2] = 2이므로,
고정점은 2가 된다.  하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어있다.
이 때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하라. 고정점은 최대 1개만 존재한다. 만약 고정점이 없다면 -1을 출력한다.
단, 이 문제는 시간 복잡도 O(logN)으로 설계하지 않으면 시간초과 판정을 받는다"""
# 입력 : 첫 째 줄에 N이 입력됩니다. ( 1 ~ 100만)
# 둘 째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다.( 각 원소 값 -10억 ~ 10억)
# 출력 : 고정점을 출력한다. 고정점이 없다면 -1을 출력한다.
import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int, input().rstrip().split()))

# 주인공( 고정점 ) 기준으로 생각해보기!
# 생각해보자. data[k] == k다.  그러면, 고정점이 유일하다고 했으니, data[k+1], data[k+2]....은 아무리 작아도  k+2, k+3...이라서, 인덱스보다 값이 더 클 수 밖에 없다.
# 마찬가지로, data[k] == k면, data[k-1], data[k-2],.....은 아무리 커봐야 고정점이 되면 안되므로, k-2, k-3...이라서, 인덱스보다 값이 작을 수 밖에 없다.

start = 0
end = n - 1

while True:
    mid = (start + end) // 2
    if data[mid] == mid:
        print(mid)
        exit()
    elif data[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
    if start > end:
        break

print(-1)

