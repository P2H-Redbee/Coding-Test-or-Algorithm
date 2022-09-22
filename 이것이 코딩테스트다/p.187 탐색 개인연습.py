# p.187 탐색 연습

# 이진탐색

def bin_search(array, target, start, end) :
    mid = (start + end) // 2   # 중간지점으로 가기 (소숫점 내림)

    if start > end :
        return None

    if array[mid] == target :
        return mid
    elif array[mid] < target : 
        return bin_search(array, target, mid+1, end)
    elif array[mid] > target : 
        return bin_search(array, target, start, mid-1)
    

# 갯수와 찾으려는 값 입력
n, target = map(int, input().split())

array = list(map(int, input().split()))

result = bin_search(array, target, 0, n-1)
if result == None : 
    print("없음")
else :
    print("위치", result+1)