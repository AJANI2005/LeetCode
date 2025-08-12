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
    start = letters[digits[0]]
    for i in range(1,len(digits)):
        end = letters[digits[i]]

        for j in range(len(end)):
            if j < len(start):
                res.append([start[j],end[j]])
            else:
                res.append([start[len(start)-1],end[j]])

    return res

print(letterCombinations("23"))