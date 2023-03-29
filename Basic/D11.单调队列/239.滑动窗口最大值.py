

#######  try 1 #######

nums = [1,3,-1,-3,5,3,6,7]
k = 3


m = max(nums[0:k])

left = 0
right = k - 1

res = [m]

for i in range(len(nums) - k + 1):
    # print(nums[left:right+1])

    left += 1 
    right += 1

# 这样做是有问题的，如果恰好最左边的元素是最大值，而且当前有重复的几个最大值在
# 数组的中间，那移动的时候，m值没办法比较，所以无法确定是否更新
##############################
# 单调队列 
class MonotonicQueue():

    def __init__(self):
        self.queue = []

    def push(self, n):

        # if len(self.queue) == 0:
        #     self.queue.append(n)
        #     return self.queue
        #
        while len(self.queue) > 0 and self.queue[-1] < n:
            self.queue.pop()
        
        self.queue.append(n)
        return self.queue

    def get(self, n):
        if len(self.queue) > 0 and self.queue[0] == n:
            self.queue.pop(0) 
            return n
        
        return None

    def getMax(self):
        return self.queue[0]



a = MonotonicQueue()
a.push(5)
a.push(3)
a.push(4)
a.push(7)
a.push(6)
a.push(6)
a.queue
a.get(7)

nums = [1,3,-1,-3,5,3,6,7]
k = 3

queue = MonotonicQueue()

i = 0
for _ in range(k):
    queue.push(nums[i])
    i += 1
j = 0

result = []
result.append(queue.getMax())

while i < len(nums):
    print(queue.queue)
    queue.get(nums[j])
    queue.push(nums[i])
    result.append(queue.getMax())
    i+=1
    j+=1


print(result)








