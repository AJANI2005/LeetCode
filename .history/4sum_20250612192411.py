def fourSum(nums: list[int], target: int):

    nums.sort()
    res = []
    for i in range(len(nums)):
        l,k = i + 1,len(nums) - 1
        while l < k:
            sum4 = nums[i] + nums[l] + nums[k]
            print(res)
            if sum4 < target:
                l += 1
            elif sum4 > target:
                 k -= 1
            else:
                res.append([nums[i],nums[l],nums[k]])
                while nums[l] == nums[l-1] and l < k:
                    l += 1
                break

    return res


print(fourSum([1,0,-1,0,-2,2],0))