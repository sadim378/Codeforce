row = 0
col = 0

for i in range(5):
    numbers = list(map(int, input().split()))

    for j in range(5):
        if numbers[j] == 1:
            row = i + 1
            col = j + 1

moves = abs(row - 3) + abs(col - 3)

print(moves)