t = int(input())

for _ in range(t):
    n = input()
    digits = list(n[::-1])
    print(' '.join(digits))