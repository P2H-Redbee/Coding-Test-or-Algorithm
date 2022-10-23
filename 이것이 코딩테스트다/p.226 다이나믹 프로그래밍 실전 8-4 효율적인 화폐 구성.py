# p.226 다이나믹 프로그래밍
# 실전8-4 효율적인 화폐 구성

# n : 지폐 종류
# m : 목표 금액
n, m = map(int, input().split())

currencies = []
for _ in range(n) :
    currencies.append( int(input()) )

arr = [10001] * (m+1)
arr[0] = 0

# 리스트 칸마다 그 금액을 구하기 위한 최소값 넣기
for curr in currencies : # 화폐 단위별로 다 계산
    for i in range(curr, m+1) :
        if arr[i-curr] != 10001 : # A(i-k)가 있다면
            arr[i] = min(arr[i-curr] + 1, arr[i])
            print(i, arr[i])

if arr[m] == 10001 :
    print(-1)
else :
    print(arr[m])
