
nums = [5,6,6,6,7,7,10]
target = 8



# 左边界 
"""
停止条件 左边恰好小于 target
"""


left = 0 
right = len(nums) - 1

while left < right - 1:

    mid = left + (right - left) // 2
    # print(left, mid, right)

    if nums[mid] < target:
        left = mid
    elif nums[mid] >= target:
        right = mid

left, right

leftbound = -1
if nums[left] == target:
    leftbound = left
elif nums[right] == target:
    leftbound = right

nums = [5,6,6,6,7,7,8,8, 9,9,9,10]
nums = [8,8,8,8,8,8]
target = 8
rightbound = -1
left = 0 
right = len(nums) - 1
while left < right - 1:

    mid = left + (right - left) // 2

    if nums[mid] <= target:
        left = mid
    elif nums[mid] > target:
        right = mid

if nums[right] == target:
    rightbound = right
elif nums[left] == target:
    rightbound = left








