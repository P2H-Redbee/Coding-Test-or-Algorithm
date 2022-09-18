# p.178 정렬
# 실전 6-1 위에서 아래로

# n 입력
n = int(input())

array = []
# n개의 수 입력
for i in range(n) :
    array.append( int(input()) )

array.sort(reverse=True)

for i in array:
    print(i, end=' ')