def fourSum(nums: list[int], target: int):

    res = []
    for i in range(len(nums)):
        l,k = i + 1, len(nums) - 2
        h = len(nums) - 1

        while l < h:
            sum4 = nums[i] + nums[l] + nums[k] + nums[h]
            
            if sum4 < target:
                pass
            elif sum4 > target:
                pass
            else:
                res.append([nums[i],nums[l],nums[k],nums[h]])