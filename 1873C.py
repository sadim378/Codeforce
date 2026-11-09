t = int(input())

for _ in range(t):
    score = 0

    for i in range(10):
        s = input()

        for j in range(10):
            if s[j] == 'X':
                point = min(i, j, 9 - i, 9 - j) + 1
                score += point

    print(score)