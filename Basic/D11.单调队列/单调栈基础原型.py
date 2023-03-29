# nums = [2,1,2,4,3]，你返回数组 [4,2,4,-1,-1]

# 注意！ 题目是下一个“更大”元素，不是下一个“最大”元素




nums = [2,1,2,4,3]
stack = []
result = []

for i in nums[::-1]:
    while len(stack)>0 and stack[-1] <= i:
        stack.pop()


    if len(stack) == 0:
        result.append(-1)
    else:
        result.append(stack[-1])

    stack.append(i)

print(list(reversed(result)))
