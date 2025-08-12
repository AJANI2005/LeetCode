def fourSum(nums: list[int], target: int):
    nums.sort()
    n = len(nums)
    out = []
    for r in range(n-3):
        for i in range(r+1,n-2):
            # two pointer
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[r] + nums[i] + nums[j] + nums[k]
                if total == target:
                    out.append([nums[r],nums[i],nums[j],nums[k]])
                    # move pointers and skip duplicates
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif total < target:
                    j += 1
                elif total > target:
                    k -= 1
          
                
    return out
            




print(fourSum([2,2,2,2,2],8))

        