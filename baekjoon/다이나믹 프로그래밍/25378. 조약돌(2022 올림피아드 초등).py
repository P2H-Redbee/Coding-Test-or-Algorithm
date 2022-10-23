# 백준 2022 올림피아드 1차대회 초등부 
# 25378 조약돌

n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(n) :
    if arr[i] == 0 :
        continue
    if i+1 == n :
        arr[i] = 0
        count += 1
        break

    if arr[i] <= arr[i+1] :
        arr[i+1] -= arr[i]
        arr[i] -= arr[i]
        count += 1
    elif arr[i] > arr[i+1] :
        arr[i] = 0
        count += 1

    # elif arr[i] > arr[i+1] :
    #     arr[i] = 0
    #     arr[i+1] = 0
    #     count += 2
    print(arr)
    print(count)
print(count)