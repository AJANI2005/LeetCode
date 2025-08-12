def fourSum(nums: list[int], target: int):
    n = len(nums)
    out = []
    for r in range(n-3):
        for i in range(r+1,n-2):
            # two pointer
            j = i + 1
            k = n - 1
            total = nums[r] + nums[i] + nums[j] + nums[k]
            if total == target:
                out.append([nums[r],nums[i],nums[j],nums[k]])
                pass
            elif total < target:
                j += 1
            elif total > target:
                k -= 1

            




print(fourSum([1,0,-1,0,-2,2],0))

        