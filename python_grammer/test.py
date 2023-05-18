# f = open(".\\result.txt", 'w')


# f.write('abcd')

# s = 'True'

# a = bool(s)

# isinstance(a, bool)

def length_of_lis(nums):
    idx_s = 0
    answer = []
    while idx_s < len(nums):
        li = []
        tmp = 0

        for i in range(idx_s, len(nums)):
            if idx_s == i:
                li.append(nums[i])
                tmp = i
                if idx_s == len(nums) - 1:
                    answer.append(li)
                    idx_s+=1 # break
                continue
            
            if nums[tmp] < nums[i]:
                li.append(nums[i])
                tmp = i
            else:
                answer.append(li)

        idx_s += 1
    return answer# len(max(answer, key=len))


nums1 = [1, 2, 3, 4, 5]
print(length_of_lis(nums1))