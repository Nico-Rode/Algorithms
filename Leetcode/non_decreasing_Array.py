def checkNonDecreasing(nums):
    edit = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            edit += 1
            if i == 0:
                nums[i] = nums[i+1]
            elif nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
        if edit > 1:
            return False
    return True
