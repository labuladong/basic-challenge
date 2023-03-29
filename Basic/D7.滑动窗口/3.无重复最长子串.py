
s = "abcabcbb"

s = "a"
s = "pwwkew"
# if s == ""

left = 0
right = 0
result = 0 
while right < len(s):
    window = s[left:right]
    if s[right] in window:
        left += 1
        # right += 1
    else:
        right += 1

    if (right - left) > result:
        result = right - left
    print(window)

print(result)

        



