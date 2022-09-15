# p.149 DFS / BFS
# 실전 5-1 음료수 얼려 먹기

def DFS(form, i, j) :
    if i == -1 or j == -1 or i >= N or j >= M :
        return

    if(form[i][j] == 0) : 
        form[i][j] = "*" # 방문했으면 방문했다는 표시하기
        DFS(form, i-1, j)
        DFS(form, i+1, j)
        DFS(form, i, j-1)
        DFS(form, i, j+1)
        return True    

# 입력부분
N, M = map( int, input().split() ) # 세로길이 N, 가로길이 M 입력
form = [] 
for i in range(N) : # 얼음 형태 입력
    form.append(list(map(int, input() )))

# icecream 변수 초기화
icecream = 0

# 시작
for i in range(N) : 
    for j in range(M) : 
        if form[i][j] == 0 :
            if DFS(form, i, j) == True :
                icecream += 1

print(icecream)
