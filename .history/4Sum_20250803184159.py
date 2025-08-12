def fourSum(nums: list[int], target: int):
    nums.sort()
    n = len(nums)

    out = []
    i = 0
    while i < n:
        j = 0
        k = n - 1 
        while k > j:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                out.append([nums[i],nums[j],nums[k]])
                while i < n and nums[i] == nums[i-1]:
                    i+=1
                break 
            elif s < target: 
                k -= 1
                while k > j and nums[k] == nums[k+1]:
                    k -= 1
            elif s > target:
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
        i += 1
    return out        

print(fourSum([1,0,-1,0,-2,2],0))


        