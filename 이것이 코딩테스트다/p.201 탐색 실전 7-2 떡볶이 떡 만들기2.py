# p.201 탐색
# 실전7-2 떡볶이 떡 만들기2

n, m = map(int, input().split())

dduk = list(map(int, input().split()))

i = 0
j = max(dduk)

while i<=j :
    mid = (i + j) //2
    length = 0

    #길이 계산하기
    for x in dduk :
        if x > mid :
            length += x - mid
    if length >= m :   
        i = mid + 1
        top = mid
    elif length < m :
        j = mid - 1

print(top)