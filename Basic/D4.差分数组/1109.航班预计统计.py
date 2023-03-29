


bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5

# 差分数组一般都是 t = nt - n_{t-1} （除了第一个）


### 一般情况
# 0 0 0 10 10 10 0 0 0 
# 0 0 0 10 0  0  -10 0 0
# 0 0 0 10 10 10 0 0 0 

### 在第一位的情况
# 10 0 0 0
# 10 -10 0 0 
# 10 0 0 


### 在最后一位的情况
# 0 0 0 10
# 0 0 0 10
# 0 0 0 10 
diff_list = [0 for _ in range(n)]
for start, end, num in bookings:
    start -= 1
    end -= 1
    diff_list[start] += num
    if end >= n - 1:
        pass
    else:
        diff_list[end+1]  -= num

# recover the sum list

diff_list
sum_list = [diff_list[0]]
for j in range(n-1):
    i = j+1
    sum_list.append(sum_list[i-1] + diff_list[i])

sum_list

###############################################################
#### merge the two for loop 
###############################################################

diff_list = [0 for _ in range(n)]
sum_list  = []
for i, (start, end, num) in enumerate(bookings):

    start -= 1
    end -= 1
    diff_list[start] += num
    if end >= n - 1:
        pass
    else:
        diff_list[end+1]  -= num

    if i == 0:
        sum_list = [diff_list[0]]
    else:
        sum_list.append(sum_list[i-1] + diff_list[i])




# recover the sum list

diff_list
for j in range(n-1):
    i = j+1
    sum_list.append(sum_list[i-1] + diff_list[i])

sum_list


