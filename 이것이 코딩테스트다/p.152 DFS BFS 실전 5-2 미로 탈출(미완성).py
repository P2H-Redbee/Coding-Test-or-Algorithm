# p.152 DFS / BFS
# 실전 5-2 미로 탈출

from collections import deque

# N, M 입력
n, m = map(int, input().split())

# 미로 정보 입력
maze = []
for i in range(n) :
    maze.append(list(input()))

count = 0

# 현재 위치 방문 처리

# deque 만들기

# 현재 위치 기준으로 인접 칸들 deque에 추가하기

# 거리 측정하기




# 최소 이동 칸의 개수 출력
print(count)