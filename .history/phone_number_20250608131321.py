def letterCombinations(digits: str) -> list[str]:
    if digits == "":
        return []
    res = []

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
    if len(digits) == 1:
        return list(phone[digits[0]])

    for i in range(len(digits)):
        for letter in phone[digits[i]]:
            for j in range(len(digits)):
                if i == j: continue


    return res


print(letterCombinations("234"))