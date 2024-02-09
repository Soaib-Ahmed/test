def oddd(x, y):
    odd_sum = 0
    for i in range(min(x, y) + 1, max(x, y)):
        if i % 2 != 0:
            odd_sum += i
    return odd_sum

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    res = oddd(x, y)
    print(res)
