n = int(input())

presents = list(map(int, input().split()))

answer = [0] * n

for i in range(n):
    receiver = presents[i]

    answer[receiver - 1] = i + 1

print(*answer)