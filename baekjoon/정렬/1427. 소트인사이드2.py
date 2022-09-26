# 백준 정렬 
# 1427번 소트인사이드

n = list(map(int, input()))
n.sort(reverse=True)
for _ in n :
    print(_, end='')