out = []
nums=[2,10,10,30,30,30]
for i in range(len(nums)):
    if(i and (nums[i] == nums[i-1])):
        continue
    out.append(nums[i])

print(out)
print(len(out))