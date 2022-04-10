# Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order. As always, do not use built-in array functions.

def removeNegatives(arr):
    for i in arr:
        if i < 0 :
            arr.remove(i)

    return arr

print(removeNegatives([1, -5, 4, 3, -2, 6]))

# Second-to-Last

# Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.

def second_to_last(arr):

    if len(arr) <= 1:
        return 'null'
    else:
        return arr[len(arr)-2]

print(second_to_last([42]))
print(second_to_last([42,True,4,"Kate",7]))




