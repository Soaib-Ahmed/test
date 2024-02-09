n = int (input())
a = list(map(int,input().split()))

rev_a = a[::-1]

if a == rev_a:
    print("YES")
else:
    print("NO")