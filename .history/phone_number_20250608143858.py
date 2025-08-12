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
    def dfs(i,path):
        if i >= len(digits): return [] 
        res = [] 
        for letter in phone[digits[i]]:
            res += [letter] + dfs(i+1,path)
        return res

    print(dfs(0,""))
    return res 
print(letterCombinations("234"))