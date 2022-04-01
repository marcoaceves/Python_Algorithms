def array_diff(a, b):
    #your code here
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a



print(array_diff([1,2,3],[1,3]))