
matrix = [[1,2,3],[4,5,6],[7,8,9]]





def cut_top(matrix):
    return matrix[0][:], matrix[1:][:]

def cut_right(matrix):
    return ([matrix[i][-1] for i in range(len(matrix))], 
            ([matrix[i][:-1] for i in range(len(matrix))] if len(matrix[0]) > 1
             else [])
            )

def cut_bottom(matrix):
    return matrix[-1][::-1], matrix[:-1][:]

def cut_left(matrix):
    return ([matrix[-i-1][0] for i in range(len(matrix))], 
            ([matrix[i][1:] for i in range(len(matrix))] if len(matrix[0]) > 1
             else [])
            )

cut_top(matrix)

cut_right([[2],[3]])

cut_bottom(matrix)

cut_left(matrix)

print_edge_v2([])

def print_edge_v2(matrix):

    if len(matrix) == 0:
        return []

    counter = 0
    store = []
    while True:
        # top
        if counter % 4 == 0:
            temp, matrix = cut_top(matrix)
            store += temp
        # right
        elif counter %4 == 1:
            temp, matrix = cut_right(matrix)
            store += temp
        # bottom
        elif counter %4 == 2:
            temp, matrix = cut_bottom(matrix)
            store += temp
        # right
        elif counter %4 == 3:
            temp, matrix = cut_left(matrix)
            store += temp

        if matrix == []:
            break

        counter += 1
 
    return store


matrix = [[1],[2],[3]]
print_edge_v2(matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print_edge_v2(matrix)

def print_edge(matrix, M, N):

    # top 
    pos = (0,0)
    for _ in range(N-1):
        print(matrix[pos[0]][pos[1]])
        pos = step_position(pos, (0,1))


    print('yyyyyyy')
    # right 
    for _ in range(M-1):
        print(matrix[pos[0]][pos[1]])
        pos = step_position(pos, (1,0))


    print('xxxxxxx')
    if N == 1:
        return 

    # bottom 
    for _ in range(N-1):
        print(matrix[pos[0]][pos[1]])
        pos = step_position(pos, (0,-1))

    if M == 1:
        return 

    # left 
    for _ in range(M-1):
        print(matrix[pos[0]][pos[1]])
        pos = step_position(pos, (-1,0))


        
def step_position(pos, direction):
    x,y = pos
    a,b = direction
    return x+a, y+b
    

print_edge([[1,2,3]], 1, 3 )
    










