t = int(input())

for i in range(t):
    a, b = input().split()

    now_a = b[0] + a[1:]
    now_b = a[0] + b[1:]

    print(now_a, now_b)