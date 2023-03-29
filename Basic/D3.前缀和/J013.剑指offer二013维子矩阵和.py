
M = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

M = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

def get_prefix_sum(M):
    prefix_sum = [[]]
    for i in range(len(M)):
        prefix_sum.append([])
        for j in range(len(M[0])):

            if i == 0 and j == 0:
                prefix_sum[i].append(
                        M[i][j])

            elif i == 0 and j > 0:
                prefix_sum[i].append(
                        M[i][j] + prefix_sum[i][j-1]
                        )
            elif j == 0:
                prefix_sum[i].append(
                        M[i][j] +prefix_sum[i-1][j]
                        )
            elif j != 0:
                prefix_sum[i].append(
                        M[i][j] + prefix_sum[i-1][j] +\
                                prefix_sum[i][j-1] -\
                                prefix_sum[i-1][j-1]
                        )
    return prefix_sum

total = prefix_sum[len(M)-1][len(M[0])-1]

prefix_sum_left = get_prefix_sum(M)
prefix_sum_right = get_prefix_sum([list(reversed(nums)) for nums in reversed(M)])
prefix_sum_right 


prefix_sum_left[2][2] +\
prefix_sum_right[3][3] -\
total

prefix_sum_right
prefix_sum_left[2][2]
prefix_sum_right[3][3] 




#######################################################################
# 双向取右上右上是不对的

# ┌──────────────────────┬───────────┐
# │┼─────────────────────┤           │
# ││                     │           │
# ││                     │           │
# ││    A                │           │
# ││         ┌───────────┼─────────┐ │
# ││         │           │         │ │
# ││         │     B     │         │ │
# ││         │           │         │ │
# ├┴─────────┼───────────┘         │ │
# │          │                     │ │
# │          │              C      │ │
# │          │                     │ │
# │          │                     │ │
# │          └─────────────────────┘ │
# │                                  │
# └──────────────────────────────────┘
# B 是 target 子矩阵
# A 和 C 加起来之后会把A的右上角多加了， 后面再剪掉会很麻烦


# 所以新的方案是这样：
# ┌────────────────┬────────────────────────┬┐
# │┼┼────────────┼┼│                        ││
# │┼│            │┼│                        ││
# │┼│            │┼│                        ││
# │┼│            │┼│                        ││
# │┼┴────────────┴┼┼────────────────────────┼│
# ││              │┼─────────────────────────┤
# ││              ││A                       B│
# ││              ││                         │
# ││              ││                         │
# ││              ││                         │
# ││              ││                         │
# ││              ││                         │
# ││              ││                         │
# ││              ││                         │
# │┼──────────────┼│                         │
# └────────────────┘C────────────────────────D
# target sum = D - B - C + A 


def get_coner_sum(matrix, x, y):
    if x == -1 or y == -1:
        return 0
    else:
        return matrix[x][y]

def get_coner_sum(self, matrix, x, y):
    if x == -1 or y == -1:
        return 0
    else:
        return matrix[x][y]


def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    A = self.get_coner_sum(self.prefix_sum_left, row1-1, col1-1)
    B = self.get_coner_sum(self.prefix_sum_left, row1-1, col2)
    C = self.get_coner_sum(self.prefix_sum_left, row2, col1-1)
    D = self.get_coner_sum(self.prefix_sum_left, row2, col2)

    # print(A,B,C,D)
    return  D - B - C + A

# DONE!







