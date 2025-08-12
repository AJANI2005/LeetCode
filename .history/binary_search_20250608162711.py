def binS(nums =[3,4,7,8],target = 5):
    l = 0
    h = len(nums) - 1
    while l < h:
        mid = (l+h) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            h = mid - 1 
        else:
            break
    return l
print(binS())