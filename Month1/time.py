# n = int(input())
n = 6

for i in range(1, n + 1):
    print(' ' * (n - i), '*' * (i * 2 - 1))
print(' ' * ((n + 1) // 2), '*' * (n // 2 * 2 - 1))
print(' ' * ((n + 1) // 2), '*' * (n // 2 * 2 - 1))
