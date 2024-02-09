s = input()

new_string = []
curr_string = ""
cnt_l=0
cnt_r=0

for char in s:
    curr_string += char
    if char == 'L':
        cnt_l += 1
    else:
        cnt_r += 1

    if cnt_r == cnt_l:
        new_string.append(curr_string)
        curr_string=""
print(len(new_string))
for s in new_string:
    print(s)
