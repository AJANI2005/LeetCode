def longestCommonPrefix(strs: list[str]):

    prefix = ""
    match = True
    j = 0
    while match:
        c = ""
        for i in range(len(strs)):
            if(j >= len(strs[i])): 
                match = False
                break
            if c == "":
                c = strs[i][j]
            elif strs[i][j] != c:
                match = False
                break 

        if(match) : prefix += c
        j += 1    
    return prefix

print(longestCommonPrefix(["dog","racecar","car"]))


        