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
        letters = phone[digits[i]]
        for l1 in letters:
            start = i+1
            col = 0 
            combo = ""
            while start < len(digits):
                for j in range(start+1,len(digits)):
                   if col < len(phone[digits[j]]) :
                       combo += phone[digits[j]][col]

            res.append(combo)





    return res


print(letterCombinations("234"))