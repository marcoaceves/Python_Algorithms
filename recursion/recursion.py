# Recursive Sigma

def r_sigma(num):
    if num > 0:
        return r_sigma(num-1) + num
    return(0)

print(r_sigma(5))


# Recursive Factorial

def factorial(num:int)->int:
    num = int(num)
    if num == 0:
        return 1
    return factorial(num - 1) * num


print(factorial(6))

