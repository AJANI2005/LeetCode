



def binSearchIndex(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1 

def twoSum(nums: list, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 1):
        lookup = target - nums[i]
        index = binSearchIndex(nums[i+1:],lookup)
        if index != -1:
            res.append([nums[i],nums[index + i+1]])
    return res

def fourSum(nums: list, target):
    nums.sort()
    res = []
    quad = []
    def kSum(nums : list,target,k):
        if k == 2:
            subsets = twoSum(nums,target)
            for s in subsets:
                res.append(quad + s)
        else:
            n = len(nums)
            for i in range(n - k + 1):
                # Ignore duplicates
                if i and nums[i] == nums[i-1]:
                    continue
                # Fix first value
                quad.append(nums[i])
                # Explore
                kSum(nums[i+1:],target - nums[i],k-1)
                # Undo
                quad.append(nums[i])


    kSum(nums,target,4)
    return res



print(fourSum([1,0,-1,0,-2,2],0))