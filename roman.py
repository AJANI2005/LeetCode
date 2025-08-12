def intToRoman(num: int) -> str:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num



def romanToInt(s: str):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    result = 0
    j = 0
    i = 0
    while i < len(s) and j < len(syms):
       
       if syms[j] == s[i]:
           result += val[j]
           i += 1
       elif i < len(s) - 1 and syms[j] == s[i:i+2]:
           result += val[j]
           i += 2
       else:
           j += 1
       
    return result 
print(romanToInt("MCMXCIV"))
