def letterCombinations(digits: str) -> list[str]:
    phone = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    res = []
    def dfs(i):
        if i >= len(digits):
            return ""
        
        digit = digits[i]
        m = ""
        for k in range(4):
            m += dfs(i+1) 
        res.append(m)
        return dfs(i+1)

   
    return res
print(letterCombinations("234"))