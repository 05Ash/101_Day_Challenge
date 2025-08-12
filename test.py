import random
from time import sleep

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)-1
    if length > 0:
        for i in range(length, -1, -1):
            print(nums[i])
            if not nums[i]:
                nums.pop(i)
                nums.append(0)
            print(nums)


# moveZeroes([0,1])

def bubble_Sort(nums):
    """Sorting Algorithm for Bubble Sort in ascending order"""
    length = len(nums)-1

    if length > 1:
        for k in range(length, -1, -1):
            swapped = False
            for i in range(k):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True
            if not swapped:
                break
    return nums

def quick_Sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        # print(f"Pivot at index {pivot_index}, current array: {nums}")
        quick_Sort(nums, low, pivot_index - 1)
        quick_Sort(nums, pivot_index + 1, high)
    return nums

def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        print(array,i)
    array[i], array[high] = array[high], array[i]
    return i

def insert_Sort(nums):
    for i in range(1,len(nums)):
        j = i
        while j > 0:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums


def merge_Sort(nums):
    length = len(nums)
    if length <= 1: return nums
    l_array = merge_Sort(nums[:length//2])
    r_array = merge_Sort(nums[length//2:])
    # print("Step-1:",l_array, r_array)
    return merge(l_array, r_array)

def merge(arr1, arr2):
    # print("step 2:",arr1,arr2)
    i=j=0
    merged_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    return merged_array


def counting_sort(array):
    sample_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    merge_array = []
    for num in array:
        sample_dict[num] += 1
    for key in sample_dict.keys():
        merge_array.extend([key]*sample_dict[key])
    return merge_array


array = [random.randint(0,9) for _ in range(50)]
print(array)
# print(partition(array,0,len(array)-1))
# print(quick_Sort(array,0,len(array)-1))
# print(insert_Sort(array))
# print(merge_Sort(array))
print(counting_sort(array))
