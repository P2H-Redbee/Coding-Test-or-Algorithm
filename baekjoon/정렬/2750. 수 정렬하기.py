# 백준 정렬 
# 2750번 수 정렬하기

n = int(input())

array = []
for i in range(n) :
    array.append( int(input()) )

for i in range(1, n) :
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break

for i in range(n) :
    print(array[i])
