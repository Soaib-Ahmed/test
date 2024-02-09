n = int(input())
a = list(map(int,input().split()))
cnt={}

for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i]=1
        
remove_cnt=0
for i, fnd in cnt.items():
    if i > fnd:
        remove_cnt += fnd
    elif i < fnd:
        remove_cnt += fnd - i

print(remove_cnt)
