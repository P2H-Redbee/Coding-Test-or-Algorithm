# 백준 2022 올림피아드 1차대회 초등부 
# 25377 빵

n = int(input())

arr = []
for i in range(n) :
    a, b = map(int, input().split())
    if a <= b :
        arr.append(b)

if len(arr) == 0 :
    print(-1) # 빵 못 산다면 -1 출력
else :
    print(min(arr))  # 빵 살 수 있다면 출력
