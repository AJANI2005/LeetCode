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
    return [] 



def comb(s):
    # Base Case
    if len(s) <= 1:
        return s
    else:

        for i in range(len(s)):
           print(s[i] + comb(s[:i] + s[i+1:]))



print(comb("abc"))
