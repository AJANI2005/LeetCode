import math

def median(nums1,nums2):
    a = sorted(nums1 + nums2)
    s = len(a)
    m = math.floor((s-1)/2)

    if s % 2 == 0:
        return (a[m] + a[m+1])/2
    else:
        return a[m]
print(median([1,2],[3,4]))
