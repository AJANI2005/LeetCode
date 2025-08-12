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

    letters = []
    for i in range(len(digits)):
        letters.append(phone[digits[i]])

    # Combinations
    def combination(l):
        if len(l) == 1:
            return l
        for i in range(len(l)):
            # Choose
            r = l[i] + combination(l[i+1:])

    return res


print(letterCombinations("234"))