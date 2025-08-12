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

    def f(digits) :
        # Base case
        # e.g. "2" -> ['a','b','c']
        if len(digits) == 1:
            return list(phone[digits])
        else:         
            res = []
            for i in range(len(digits)):
                # get characters for this digit
                characters = phone[digits[i]]
                # get other array of characters to combine with this list of characters
                other = f(digits[i+1:])
                for c in characters:
                    for a in other:
                        res.append(sorted(a + c))
            return res

    return f(digits) 

print(letterCombinations("23"))

def comb(s):
    # Base Case
    if len(s) <= 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
          other = comb(s[:i] + s[i+1:])
          for o in other:
              res.append(s[i] + o)
        return res

