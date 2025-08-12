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

        path = ""        
        for letter in phone[digits[i]]:
            path = letter + dfs(i+1)
        return path
    return res 
print(letterCombinations("234"))