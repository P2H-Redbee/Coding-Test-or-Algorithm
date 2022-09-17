# p.157 선택 정렬 
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range( len(array) ) :
    temp = i
    for j in range(i+1, len(array)) :
        if array[j] < array[temp] : 
            temp = j
    array[i], array[temp] = array[temp], array[i]

print(array)    


# p.161 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j-1] > array[j] :
            array[j-1], array[j] = array[j], array[j-1]
        else :
            break
print(array)


# p.164 퀵 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array, start, end) :
    if(start < end) :
        pivot = array[start]
        i = start + 1
        j = end

        print('star:',start, 'end:',end)

        while i <= j :  # 정렬 실행 조건 넣기 i < j ??
            while i <= end and pivot >= array[i] : # i 위치 잡기
                i = i + 1
            while start < j and pivot <= array[j] : # j 위치 잡기
                j = j - 1

            if i <= j : # i와 j 바꾸기
                array[i], array[j] = array[j], array[i]
            else : # i와 j 엇갈리면 j를 피벗과 스왑
                array[start], array[j] = array[j], array[start]

        quick(array, start, j-1)
        quick(array, j+1, end)

quick(array, 0, len(array)-1)
print(array)



# p.164 퀵 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array, start, end) :
    if(start < end) :
        pivot = array[start]
        i = start + 1
        j = end

        while i <= j :  # 정렬 실행 조건 넣기 i < j ??
            while i <= end and pivot >= array[i] : # i 위치 잡기
                i = i + 1
            while start < j and pivot <= array[j] : # j 위치 잡기
                j = j - 1

            if i <= j : # i와 j 바꾸기
                array[i], array[j] = array[j], array[i]
            else : # i와 j 엇갈리면 j를 피벗과 스왑
                array[start], array[j] = array[j], array[start]

        quick(array, start, j-1)
        quick(array, j+1, end)

quick(array, 0, len(array)-1)
print(array)

