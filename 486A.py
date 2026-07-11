n = int(input())

if n % 2 == 0:
    answer = n // 2
else:
    answer = -((n + 1) // 2)

print(answer)