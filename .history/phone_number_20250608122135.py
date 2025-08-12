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
    # start with digits[0]
    # at most the len of letters is 4
    for i in range(len(digits)):
        # Choose
        for j in range(len(letters[digits[i]])):
            c = letters[digits[i]][j]
        # Explore 

        # Unchoose


    return res


print(letterCombinations("23"))