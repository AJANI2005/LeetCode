def threeSum(nums: list[int]) -> list[list[int]]:
    output = []
    used = set() 
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            continue
        seen.add(nums[i])
        target = -1 * nums[i]
        # find two other values that sum to target (two sum)
        memo = {}
        for j in range(i + 1,len(nums)):
            subtarget = target - nums[j]
            if subtarget in memo:
                # found a triplet
                triplet = [nums[i],nums[j],subtarget]
                triplet_key = tuple(sorted(triplet))
                if  triplet_key not in used:
                    output.append(triplet)
                    used.add(triplet_key)
            else:
                # store this subtarget
                memo[nums[j]] = j


    return output
   

print(threeSum([-1,0,1,2,-1,-4]))
