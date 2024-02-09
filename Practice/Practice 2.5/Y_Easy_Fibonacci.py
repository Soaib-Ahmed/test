def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        result = n - 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result

n = int(input())

for i in range(1, n + 1):
    print(fib(i), end=" ")
