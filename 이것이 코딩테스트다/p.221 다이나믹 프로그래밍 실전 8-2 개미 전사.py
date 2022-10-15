# p.221
# 실전8-2 개미 전사

n = int(input())
array = list(map(int, input().split()))

d = [0]*n

d[0] = array[0]
d[1] = array[1]

for i in range(2, n) :
    d[i] = max(array[i] + d[i-2],  d[i-1])

print(max(d))