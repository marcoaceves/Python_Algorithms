from array import array

# Min Max AVG Algo
def min_max_avg(arr):
    min = arr[0]
    max = 0
    avg = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
        avg += arr[i]
    avg = avg / len(arr)

    new_arr = [min, max, avg]
    return new_arr


print(min_max_avg([1,5,10,-2]))


# 2nd largest value
def second_largest(arr):
    second = 0
    high = 0
    low =0
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
    for i in range(len(arr)):
        if arr[i] > low and arr[i] != high:
            low = arr[i] - 1
            second = arr[i]
    return second

print(second_largest([1,3,5,7,6,9]))

# skyline heights

def skyline(arr):
    can_see = []
    x=0
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] > x:
            can_see.append(arr[i])
            x = arr[i]
    return can_see
print(skyline([-1,1,1,7,3,9]))