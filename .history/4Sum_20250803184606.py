def fourSum(nums: list[int], target: int):
    nums.sort()
    n = len(nums)

    out = []
    i = 0
    while i < n:

        while i and nums[i] == nums[i+1]:
            i+=1

        j = 0
        k = n - 1 
        while k > j:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                out.append([nums[i],nums[j],nums[k]])
                break
            elif s < target: 
                j += 1
            elif s > target:
                k -= 1
        i += 1
    return out        

print(fourSum([1,0,-1,0,-2,2],0))


        