
def twoSum(nums: list, target):
    nums.sort()
    n = len(nums)

    def binSearch(arr, target):
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

    print(binSearch(nums,5))


print(twoSum([1,2,3,4,5,6],6))