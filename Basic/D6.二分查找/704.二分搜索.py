from typing import List

def search(nums: List[int], target: int) -> int:

    
    if len(nums) == 0:
        return -1

    left = 0
    right = len(nums) - 1

    n = 0

    while left < right - 1:
        mid = left + (right - left)//2
        n+=1
        print(left, mid, right)
        if n > 10:
            break
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid

    return -1



nums = [-1,0,3,5,9,12]
target = 2

search(nums, target)


















