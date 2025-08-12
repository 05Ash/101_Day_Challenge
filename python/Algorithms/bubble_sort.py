def Bubble_Sort(arr):
    length =  len(arr)
    sorted = False
    for i in range(length):
        sorted = True
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        if sorted:
            break
    return arr

test_array = [23, 45, -4, 3, 0, 89, 2]
print(Bubble_Sort(test_array))
