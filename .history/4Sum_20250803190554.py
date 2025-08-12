def fourSum(nums: list[int], target: int):
    nums.sort()
    n = len(nums)

    out = []
    r = 0
    while r < n:
        while r and nums[r] == nums[r-1]:
            r+=1
        i = r + 1 
        while i < n:
            j = i + 1
            k = n - 1 
            while k > j:
                s = nums[r] + nums[i] + nums[j] + nums[k]
                if s == target:
                    out.append([nums[r],nums[i],nums[j],nums[k]])
                    break
                elif s < target: 
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                elif s > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
            i += 1
        r += 1
    return out        

print(fourSum([2,2,2,2],8))


        