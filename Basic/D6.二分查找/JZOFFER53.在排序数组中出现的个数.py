
nums = [5,5,5,8,8,8,8,8,8,8,10]
# nums = [4,8,8]

target = 8


N = len(nums)
left = 0
right = N-1
while left < right:

    mid = left + (right - left)//2

    # find the left bound
    if nums[mid] < target:
        left = mid
    else:
        right = mid

    if left >= right - 1:
        break


if nums[left] == target:
    left_bound = left
elif nums[right] == target:
    left_bound = right
else:
    left_bound = -1



# find the right bound
left = 0
right = N-1
while left < right:

    mid = left + (right - left)//2

    # find the left bound
    if nums[mid] <= target:
        left = mid
    else:
        right = mid

    if left >= right - 1:
        break


if nums[right] == target:
    right_bound = right
elif nums[left] == target:
    right_bound = left
else:
    right_bound = -1

print(right_bound , left_bound)
print(right_bound - left_bound + 1)





class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def binary_search(left,right,target):   #此处left、right变化方式与判断条件的写法是在查找 “值为target的目标” 的最小下标
            while(left<right):
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        left,right = 0,len(nums)
        res = []
        res.append(binary_search(left,right,target))      #查找target的最小下标
        res.append(binary_search(left,right,target+1) - 1)  #查找target+1的最小下标，然后-1即为target的最大下标
        if res[0] > res[1]:
            return [-1,-1]
        else:
            return res

# 作者：mei-tian-yi-dian-dian-h
# 链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-by-mei-tian-yi-dian-dian-p3xi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
