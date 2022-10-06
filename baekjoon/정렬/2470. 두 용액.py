# 백준 정렬
# 2470 두 용액

# n 입력
n = int(input())
# n 개의 특성값 입력
array = list(map(int, input().split()))
array.sort()



if max(array) <= 0 : # 모든 수가 음수
    print(array[n-2], array[n-1])

elif 0 <= min(array) : # 모든 수가 양수
    print(array[0], array[1])

else :
    temp = 10000000000
    i = 0
    j = n-1


    # 이부분 이진탐색으로 구현
    while i < j :
        if array[i] + array[j] == 0 : 
            mini_i = i
            mini_j = j
            break
        elif abs(array[i] + array[j]) < abs(temp) : # 최소의 abs(산성값) 구하기
            temp = array[i] + array[j]
            mini_i = i # 최소의 산성값을 만들어내는 두 용액의 값 기억
            mini_j = j
        elif array[i] + array[j] > 0 :
            j -= 1
        elif array[i] + array[j] < 0 : 
            i += 1

    print(array[mini_i], array[mini_j])
        