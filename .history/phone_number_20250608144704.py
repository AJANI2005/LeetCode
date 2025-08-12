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
    res = []
    def comb(str):
        if len(str) == 1:
            return [str] 
        else:
            for i in range(len(str)):
                out = [] 
                # Choose
                c = str[i]
                # Explore
                out.append([c].append(comb(str[:i] + str[i+1:])))
            return out

    print(comb("abc"))
    return res 
print(letterCombinations("234"))