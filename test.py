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


moveZeroes([0,1])
