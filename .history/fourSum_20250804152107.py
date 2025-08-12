



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
    n = len(nums)
    res = []
    quad = []

    def kSum(numbers,subtarget,k = 4):
        if k != 2:
            # go through each value excluding the last 3
            for i in range(len(numbers) - 3):
                # duplicate skip
                if i and numbers[i] == numbers[i-1]:
                    continue
                # fix the first value
                quad.append(numbers[i])
                # calculate all groups of len k when summed with numbers[i] == target
                kSum(numbers[i+1:],subtarget - numbers[i],k-1)
                # remove the fixed first value
                quad.append(numbers[i])
        else:
            # Two Sum (k=2)
            for subset in twoSum(numbers,subtarget):
                res.append(quad + subset)

    kSum(nums,target,4)
    return res


print(fourSum([1,0,-1,0,-2,2],0))