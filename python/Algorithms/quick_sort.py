def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    pivot = median(arr)
    pre_arr = []
    post_arr = []
    pivot_count = 0
    for item in arr:
        if item < pivot:
            pre_arr.append(item)
        elif item > pivot:
            post_arr.append(item)
        else:
            pivot_count += 1

    if len(pre_arr) > 1:
        pre_arr = Quick_Sort(pre_arr)
    if len(post_arr) > 1:
        post_arr = Quick_Sort(post_arr)
    sorted_arr = pre_arr + [pivot] * pivot_count + post_arr

    return sorted_arr

def median(arr):
    n = len(arr)
    high = arr[0] if arr[0] > arr[n//2] else arr[n//2]
    return arr[-1] if arr[-1] < high else high





test_arr = [19,17,15,12,16,18,4,11,13,23,12]
print(Quick_Sort(test_arr))
