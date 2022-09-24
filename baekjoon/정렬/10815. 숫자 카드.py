# 백준 정렬 
# 10815번 숫자 카드

n = int(input())
array = list(map(int, input().split()))

m = int(input())
search = list(map(int, input().split()))

have = []
for i in range(m) :
    have.append(0)

array.sort()

# 이진탐색
for k in range(m) :
    to = search[k]
    i = 0
    j = n-1
    while i <= j :
        mid = (i+j) // 2

        if(array[mid] == to) :
            have[k] = 1
            break            
        elif(array[mid] > to) :
            j = mid - 1
        elif(array[mid] < to) :
            i = mid + 1
print(have)
