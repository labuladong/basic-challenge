

s = "cbaebabacd"

p = "abc"


left = 0
N = len(p)
right = N-1

target_dict = {}
for i in p:
    if i in target_dict:
        target_dict[i] += 1
    else:
        target_dict[i] = 1
    

for i in range(N):
    if i in target_dict :
        target_dict[i] -= 1


def check_fit(t_dict):
    for i in t_dict:
        if t_dict[i] != 0:
            return False
    return True


while left <= len(s) - N + 1:




