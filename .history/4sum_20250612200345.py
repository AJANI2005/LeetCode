def fourSum(nums: list[int], target: int):

    if len(nums) < 4:
        return []

    res = []
    nums.sort()
    i = 0
    while i < len(nums): 

        l,h = i + 1, len(nums) - 1
        k = h - 1

        while l < k:
            sum4 = nums[i] + nums[l] + nums[k] + nums[h]
            
            if sum4 < target:
                l += 1
            elif sum4 > target:
                if h - k > 1:
                    h -= 1
                else:
                    k -= 1
            else:
                print([i,l,k,h])
                res.append([nums[i],nums[l],nums[k],nums[h]])
                l += 1
                while l < k and nums[l] == nums[l-1]:
                    l += 1
        
        i += 1         
        while i > 0 and nums[i] == nums[i-1]:
            i += 1
    return res

print(fourSum([2,2,2,2,2],8))