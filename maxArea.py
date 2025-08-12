
def maxArea(height: list[int]) -> int:
    i, j = 0, len(height) - 1
    max_area = 0
    while i < j:
        h = min(height[i], height[j])
        max_area = max(max_area, (j - i) * h)
        # Move the shorter line inward
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))