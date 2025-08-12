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
    def combine(i):
        if i >= len(digits):
            return "" 

        digit = digits[i]
        letters = phone[digit]
        string = "" 
        for l in letters:
            string += l + combine(i+1)
        return string

    print(combine(0))
    return [] 
print(letterCombinations("234"))