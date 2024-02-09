n, q = map(int, input().split())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]


for _ in range(q):
    l, r = map(int, input().split())
    q_sum = prefix_sum[r] - prefix_sum[l - 1]
    print(q_sum)
