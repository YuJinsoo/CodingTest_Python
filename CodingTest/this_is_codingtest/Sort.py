# 선택정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)


# 삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

## 내풀이
for i in range(1, len(array)):
    if array[i-1] < array[i]:
        continue
    
    for j in range(0, i):
        if array[j] > array[i]:
            array[i], array[j] = array[j], array[i]

print(array)

## 책풀이 >> 틀림. 뭐지? 
arr = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[i] = arr[j-1], arr[j]
        else:
            break

print(arr)