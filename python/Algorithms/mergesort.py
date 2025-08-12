def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    left = mergesort(arr[:n//2])
    right = mergesort(arr[n//2:])
    return merge(left, right)

def merge(arr1, arr2):
    result = []
    i = j = 0

    while( i < len(arr1) and j < len(arr2)):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


test_arr = [19,17,15,12,16,18,4,11,13,23,12]
print(mergesort(test_arr))
