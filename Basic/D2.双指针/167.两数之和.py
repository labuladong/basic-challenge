



numbers = [2,5,7,11,15]
target = 9

numbers = [-1, 0]
target = 0

N = len(numbers)

for i in range(N-1):
    j = i + 1
    left = numbers[i]
    right = 0
    while left + right < target and j < N:
        right = numbers[j]
        if left + right == target:
            print(i,j)
        j += 1

#### 上面这个慢了，无法通过 leetcode ######


##增加两个可以移动的pointer
numbers = [2,5,7,11,15]
target = 9
N = len(numbers)

left = 0
right = N-1

while left <= right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
        print(left+1, right+1)
        break
    elif  current_sum > target:
        right -= 1
    else:
        left += 1







