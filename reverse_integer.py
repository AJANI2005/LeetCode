
def reverse(x : int):
    if x <= -2 ** 31 or x >= (2 ** 31) - 1:
        return 0
    if x <= 9 and x >= -9:
        return x
    y = 0
    c = abs(x)
    while c > 0:
        y *= 10
        y += c % 10
        c //= 10
    if x < 0: 
        y *= -1

    return y


print(reverse(120))        
