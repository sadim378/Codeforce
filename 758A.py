n = int(input())
a = list(map(int, input().split()))

maximum = max(a)

total = 0

for i in range(n):
    total += maximum - a[i]

print(total)