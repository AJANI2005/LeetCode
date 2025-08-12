def fourSum(nums: list[int], target: int):

    res = []
    for i in range(len(nums)):
        l,h = i + 1, len(nums) - 1
        k = h - 1

        while l < k and l < h:
            sum4 = nums[i] + nums[l] + nums[k] + nums[h]
            
            if sum4 < target:
                l += 1
            elif sum4 > target:
                if h - k > 1:
                    h -= 1
                else:
                    k -= 1
            else:
                res.append([nums[i],nums[l],nums[k],nums[h]])
                while nums[l] == nums[l-1] and l < k:
                    l += 1
    return res

print([1,0,-1,0,-2,2],0)