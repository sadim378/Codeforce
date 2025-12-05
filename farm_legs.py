t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    if n % 2 == 1:
        print(0)
    else:
        print(n // 4 + 1)
    