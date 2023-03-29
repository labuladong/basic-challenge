nums1 = [4,1,2]
nums2 = [1,3,4,2]



nums = nums2
stack = []
result = {}

for i in nums[::-1]:
    while len(stack)>0 and stack[-1] <= i:
        stack.pop()


    if len(stack) == 0:
        result[i] = (-1)
    else:
        result[i] = stack[-1]

    stack.append(i)


