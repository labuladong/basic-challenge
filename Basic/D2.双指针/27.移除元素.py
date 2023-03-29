
nums = [0,1,2,2,3,0,4,2]
val = 2
left_pointer = 0
right_pointer = 0

while right_pointer < len(nums):
    print(nums)
    print(left_pointer, right_pointer)
    if nums[left_pointer] == val and nums[right_pointer] != val:
        nums[left_pointer], nums[right_pointer] =\
            nums[right_pointer], nums[left_pointer]
        right_pointer += 1
        left_pointer += 1
    
    elif nums[left_pointer] == val and nums[right_pointer] == val:
        right_pointer += 1
    
    elif nums[left_pointer] != val:
        left_pointer += 1
        right_pointer += 1



