def letterCombinations(digits: str) -> list[str]:
    if digits == "":
        return []
    res = []

    letters = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    if len(digits) == 1:
        return list(letters[digits[0]])

    k = 0 # row
    i = 0 # current letter in letters[digits[k]]]
    while k < len(digits):




    return res


print(letterCombinations("234"))