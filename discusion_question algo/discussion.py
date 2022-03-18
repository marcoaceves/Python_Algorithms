arr = [4,2,5,10,18,-3,14,1,6,9]


# bubble

n = len(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)


# # selection
n = len(arr)

for i in range(n-1):
    pos_smallest = i
    for j in range(i+1, n):
        if  arr[j] < arr[pos_smallest]:
            pos_smallest = j

    arr[i], arr[pos_smallest] = arr[pos_smallest], arr[i]


print(arr)

# # insertion
n = len(arr)

for i in range(1,n):
    temp = arr[i]
    j = i - 1
    while(j >= 0 and temp < arr[j]):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = temp

print(arr)