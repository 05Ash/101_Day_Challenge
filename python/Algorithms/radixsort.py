from random import randint

#Assumption: Decimal System
number_system = 100

def radixsort(arr):
    if len(arr)<2:
        return arr
    #Assuming that we are sorting one digit numbers
    exp = 1
    max_num = max(arr)
    while(max_num//exp > 0):
        radix_system = [[] for _ in range(number_system)]
        for item in arr:
            radix_index = (item // exp) % number_system
            radix_system[radix_index].append(item)
        exp *= number_system
        result = []
        for j in range(number_system):
            result += radix_system[j]
        arr = result
    return arr

test_array = [randint(1, 9999) for _ in range(100)]
print(test_array)
print(radixsort(test_array))
