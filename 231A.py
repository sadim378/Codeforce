n = int(input())
count = 0

for i in range(n):
    p, v, t = map(int, input().split())

    total = p + v + t

    if total >= 2:
        count += 1

print(count)