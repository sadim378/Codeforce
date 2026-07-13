colors = list(map(int, input().split()))

unique_colors = len(set(colors))

print(4 - unique_colors)