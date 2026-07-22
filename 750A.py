n , k = map(int, input(). split())

available_time = 240 - k
used_time = 0
solved = 0

for i in range(1, n + 1):
    problem_time = 5 * i

    if used_time + problem_time <= available_time:
        used_time += problem_time
        solved += 1
    else:
        break

print(solved)