def fourSum(nums: list[int], target: int):

    nums.sort()
    res = []
    for i in range(len(nums)):

        l,h = i,len(nums)-1
        l2,h2 = l + 1, h - 1

        while l2 < h2:
            print(l2,h2)
            sum4 = nums[l] +  nums[l2] + nums[h] + nums[h2]
            if sum4 < target:
                l += 1
                l2 += 1
            elif sum4 > target:
                h -= 1
                h2 -= 1    
            else:
                res.append([nums[l],nums[l2],nums[h],nums[h2]])
                while nums[l] == nums[l2] and l2 < h2:
                    l += 1
                    l2 += 1

    return res


print(fourSum([1,0,-1,0,-2,2],0))