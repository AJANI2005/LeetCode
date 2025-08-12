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
        j = 0
        for letter in phone[digits[i]]:


    return res


print(letterCombinations("234"))