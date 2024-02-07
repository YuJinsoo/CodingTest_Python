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


## 퀵정렬
arr = [5,7,9,0,3,1,6,2,4,8]

## 내가짜보기?

## 표준 >> 안되는데?
def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
            
        while right > start and array[right] >= array[pivot]:
            right -= 1
            
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[pivot] = array[left], array[pivot]
            
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# quick_sort(arr, 0, len(arr)-1)

print('--------------------')
print(arr)
## pythonic

def quick_pythonic(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>=pivot]
    
    return quick_pythonic(left_side) + [pivot] + quick_pythonic(right_side)

result = quick_pythonic(arr)
print(result) ## [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]