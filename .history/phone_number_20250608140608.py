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
            return [] 

        digit = digits[i]
        letters = phone[digit]
        strings = [] 
        for l in letters:
            strings.append([l] + combine(i+1))
        return strings

    return combine(0)
print(letterCombinations("234"))