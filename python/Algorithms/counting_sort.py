from random import choice
KEY = [1,2,3,4,5,6,7,8,9,10]

def countingsort(arr):
    if not arr:
        return []
    counts = {}
    sorted_arr = []
    min = arr[0]
    max = arr[0]
    for item in arr:
        min = item if item < min else min
        max = item if item > max  else max
        counts[item] = counts.get(item, 0) + 1
    print(min, max)
    for item in range(min, max+1):
        sorted_arr += [item]*counts.get(item, 0)
    return sorted_arr


test_arr = [choice(KEY) for _ in range(100)]
print(test_arr)

print(countingsort(test_arr))
