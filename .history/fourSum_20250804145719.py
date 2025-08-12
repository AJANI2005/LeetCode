
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
    return None 

def twoSum(nums: list, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 1):
        lookup = target - nums[i]
        index = binSearchIndex(nums[:i] + nums[i+1:],lookup)
        if index:
            res.append([nums[i],nums[index]])






print(twoSum([1,2,3,4,5,6],6))