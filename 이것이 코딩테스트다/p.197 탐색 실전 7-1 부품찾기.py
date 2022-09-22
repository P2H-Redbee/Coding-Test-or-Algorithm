# p.197 
# 실전7-1 부품 찾기

# 이진탐색
def binSearch(array, search) :
    i = 0
    j = len(array)-1
    while i <= j :
        mid = (i+j) // 2
        if array[mid] == search : # 탐색 값 찾은 경우
            return "yes"
        elif array[mid] > search : 
            j = mid - 1
        elif array[mid] < search : 
            i = mid + 1
    return "no"



n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
want = list(map(int, input().split()))

# want의 데이터 하나씩 탐색(이진탐색)
for i in want :  # want의 원소별로 n번씩 이진탐색 진행
    print(binSearch(array, i), end=' ')
