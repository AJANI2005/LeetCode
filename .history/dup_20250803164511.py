out = []
nums=[1,1,2,3]
for i in range(len(nums)):
    if(i and (nums[i] == nums[i-1])):
        continue
    out.append(nums[i])

print(out)
print(len(out))