t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    solved = []
    balloons = 0

    for ch in s:
        if ch not in solved:
            balloons += 2
            solved.append(ch)
        else:
            balloons += 1

    print(balloons)
