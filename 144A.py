n = int(input())
heights = list(map(int, input().split()))

maximum = max(heights)
minimum = min(heights)

max_index = heights.index(maximum)
min_index = 0

for i in range(n):
    if heights[i] == minimum:
        min_index = i

answer = max_index + (n - 1 - min_index)

if max_index > min_index:
    answer -= 1

print(answer)