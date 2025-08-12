# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"



    
def convert(s:str,numRows:int)->str:
    grid = {}
    i = 0
    step = 1
    while(len(s)):
        if i not in grid:
            grid[i] = ""

        grid[i] += s[0]
        i += step
        s = s[1:]

        if i < 0:
            i = 1
            step *= -1
        if i >= numRows:
            i = numRows - 2
            step *= -1
    result = ""
    for i in grid:
        result+=grid[i]
    return result

print(convert("PAYPALISHIRING",3))
             


