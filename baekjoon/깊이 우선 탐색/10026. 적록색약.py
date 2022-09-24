# 백준 DFS 10026번 적록색약

def dfs(array, visited, n, x, y) :
    global count, blind
    global before
    # 방문한 곳이거나 좌표가 벗어나면 실행 ㄴ
    if x<0 or y<0 or x>=n or y>=n : 
        return False

    color = array[x][y]
    if before != color :
        return False

    if visited[x][y] == False : 

        # 방문하면 방문 처리
        visited[x][y] = True

        # 상하좌우 방문
        before = color
        dfs(array, visited, n, x+1, y)
        dfs(array, visited, n, x-1, y)
        dfs(array, visited, n, x, y+1)
        dfs(array, visited, n, x, y-1)
        return True

# n 입력
n = int(input())

# 그림 입력
array = []
for i in range(n) :
    array.append(input())

# 방문여부 리스트
visited =[]
for i in range(n) :
    temp = [False] * n
    visited.append(temp)

# 일반인 탐색 실행
count = 0
before = array[0][0]
for i in range(n) :
    for j in range(n) :
        before = array[i][j]
        if dfs(array, visited, n, i, j) == True :
            count = count + 1

# 초기화
# 그림
for i in range(n) :
    array[i] = array[i].replace("R", "G")
# 방문여부 리스트 
visited =[]
for i in range(n) :
    temp = [False] * n
    visited.append(temp)

# 색맹 탐색 실행
blind = 0
before = array[0][0]
for i in range(n) :
    for j in range(n) :
        before = array[i][j]
        if dfs(array, visited, n, i, j) == True :
            blind = blind + 1

print(count, blind)
