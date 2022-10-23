# p.201 탐색
# 실전 7-2 떡볶이 떡 만들기

n, m = map(int, input().split())

dduk = list(map(int, input().split()))
dduk.sort() # 정렬 되어 있어야 정확한 최대길이를 찾을 수 있다.

cut = max(dduk) - 1 # 칼 길이 설정
while cut > 0 :
    count = 0
    for i in dduk :
        if i - cut > 0 : # 떡을 칼로 자를 수 있는 정도의 길이라면 자른 길이 계산. 떡길이 - 칼길이
            count += i - cut
        else :
            continue
    if count >= m : 
        print(cut)
        break
    else :
        cut -= 1
