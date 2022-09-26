# 백준 정렬 
# 1427번 소트인사이드

# 계수 정렬 사용

n = input()
m = int(max(n))

arr = [0] * (m+1)

for i in n :
    arr[int(i)] += 1

for i in range(len(arr)-1, -1, - 1) :
    for j in range(arr[i]) :
        print(i, end='')