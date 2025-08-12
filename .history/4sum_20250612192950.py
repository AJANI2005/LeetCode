def fourSum(nums: list[int], target: int):

    for i in range(len(nums)):
        j,k = i + 1, len(nums) - 2
        h = len(nums) - 1
