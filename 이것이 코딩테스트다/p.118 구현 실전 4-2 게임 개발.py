# p.118 구현
# 실전 4-2 게임 개발

# N * M 사이즈 입력
N, M = map(int, input().split())

# 캐릭터 좌표(A,B), 바라보는 방향 입력
A, B, d = map(int, input().split())

# 맵 지형 입력 
array = []
for i in range(N) :  # input을 N번 실행
    temp = list(input())
    array.append(temp)   # input 입력 값을 2차원 리스트로 합치기
for i in range(N) :  # 공백 제거
    for j in range(M-1) :
        array[i].remove(' ')

# 매뉴얼 구현
array[A][B] = "x"
cant = 0
count = 1
d = (d-1) % 4  # 왼쪽 방향부터 간다.

while cant != 4 :
    left() # d 값에 따라 이동가능 여부 판단 후 이동

    #뒤로 갈 수 있는지 판단 후 이동. 뒤로 못 가면 그냥 끝
    if cant == 4:
        if d == 0 and A+1 == "0": # 북쪽 보는 경우
            A = A + 1
            cant = 0
        elif d == 3 and B+1 == "0" : # 서쪽 보는 경우
            B = B + 1
            cant = 0
        elif d == 2 and A-1 == "0": # 남쪽 보는 경우
            A = A -1
            cant = 0
        elif d == 1 and B-1 == "0": # 동쪽 확인
            B = B - 1
            cant = 0

print("최종좌표", A, B)
print(count)
for row in array :
    print(row)



# 왼쪽 이동하는 함수
def left() : 
    global d, A, B, array, cant, count

    if d == 0: # 북쪽 확인
        if(array[A-1][B] == "0" ) :
            array[A-1][B] = "x"
            A = A - 1
            cant = 0
            count = count + 1
            #for row in array :
                #print(row)
        else : 
            d = (d-1) % 4 # 왼쪽 방향 못 가면 다시 왼쪽으로 회전한다.
            cant = cant + 1

    elif d == 3: # 서쪽 확인
        if(array[A][B-1] == "0" ) :
            array[A][B-1] = "x"
            B = B - 1
            cant = 0
            count = count + 1
            #for row in array :
                #print(row)
        else : 
            d = (d-1) % 4
            cant = cant + 1
    
    elif d == 2: # 남쪽 확인
        if(array[A+1][B] == "0" ) :
            array[A+1][B] = "x"
            A = A + 1
            cant = 0
            count = count + 1
            #for row in array :
                #print(row)
        else : 
            d = (d-1) % 4
            cant = cant + 1
    
    elif d == 1: # 동쪽 확인
        if(array[A][B+1] == "0" ) :
            array[A][B+1] = "x"
            B = B + 1
            cant = 0
            count = count + 1
            #for row in array :
                #print(row)
        else : 
            d = (d-1) % 4
            cant = cant + 1