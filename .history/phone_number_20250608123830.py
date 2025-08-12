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
    # start with digits[0]
    # at most the len of letters is 4
    for i in range(len(digits)):
        # Choose
        for a in letters[digits[i]]:
            for k in range(4):
                n = a 
                for j in range(i+1,len(digits)):
                    if k < len(letters[digits[j]]):
                        n += letters[digits[j]][k]
                res.append(n)

    return res


print(letterCombinations("234"))