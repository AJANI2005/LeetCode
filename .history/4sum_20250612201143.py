def fourSum(nums: list[int], target: int):

  

    res = []
    nums.sort()
    i = 0

    while(i < len(nums)):
        j = i + 1
        while(j < len(nums)):
            l = j + 1
            r = len(nums) - 1
            while(l < r):
                if nums[i] + nums[j] + nums[l] + nums[r] == target:
                    res.append([nums[i],nums[j],nums[l],nums[r]])
                    l += 1
                    r -= 1
                elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            j += 1
        i += 1
    return res
   
print(fourSum([1,0,-1,0,-2,2],0))