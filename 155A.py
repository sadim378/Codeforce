n = int(input())
scores = list(map(int, input().split()))

maximum = scores[0]
minimum = scores[0]
amazing = 0

for i in range(1, n):
    if scores[i] > maximum:
        amazing += 1
        maximum = scores[i]
    elif scores[i] < minimum:
        amazing += 1
        minimum = scores[i]

print(amazing)