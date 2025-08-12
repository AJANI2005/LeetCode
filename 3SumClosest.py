def threeSumClosest(nums: list[int], target: int) -> int:
    # Start with threeSum
    nums.sort()

    closest = 10000000000   
    for i in range(len(nums)):
        # find three values that sum to target
        l,r = i+1,len(nums)-1

        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]

            if abs(target - threeSum) < abs(target - closest):
                closest = threeSum 

            if threeSum > target:
                r -= 1
            elif threeSum < target:
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            else:
                # found exact triplet
                closest = threeSum 
                return closest
              
    return 0 if closest == 10001 else closest
print(threeSumClosest([-1000,-1000,-1000],10000))