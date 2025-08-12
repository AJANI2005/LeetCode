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
        if digits == "":
                return []
        if len(digits) == 1:
            return list(phone[digits])
        else:         
            res = []
            # get characters for this digit
            characters = phone[digits[0]]
            # get other array of characters to combine with this list of characters
            other = f(digits[1:])
            for c in characters:
                for a in other:
                    res.append(c + a)
            return res

    return f(digits) 

print(letterCombinations("234"))

def perm(s):
    # Base Case
    if len(s) <= 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
          other = perm(s[:i] + s[i+1:])
          for o in other:
              res.append(s[i] + o)
        return res
def comb(s):
    seen = set()
    def combHelper(s_,i):
        # Base Case
        if len(s_) <= 1:
            return [s_]
        else:
            res = []
            # fix the first value
            v = s[i]
            if v in seen:
                return res

            # Go through all the other slots and generate combinations
            other = combHelper(s_[:i] + s_[i+1:], i)
            for c in other:
                res.append(v + c)
            return res 
    res = combHelper(s,0)
    return res
print(comb("1011"))