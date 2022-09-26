# 백준 정렬
# 5800번 성적 통계

k = int(input())

room = []
for i in range(k) :
    room.append(list(map(int, input().split()))[1:])
    room[i] = sorted(room[i], reverse=True)

for i in range(k) :
    gap = 0
    for j in range(len(room[i])-1) :
        if room[i][j] - room[i][j+1] > gap :
            gap = room[i][j] - room[i][j+1]

    print("Class", i+1)
    print("Max {}, Min {}, Largest gap {}". format(max(room[i]), min(room[i]), gap))