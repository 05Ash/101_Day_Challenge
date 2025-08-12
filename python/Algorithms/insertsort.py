def insertsort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i
        while j >0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
            j -= 1
    return arr

test_arr= [19,17,15,12,16,18,4,11,13,23,12]
print(insertsort(test_arr))
