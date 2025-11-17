data = input().split()
g = int(data[0])
c = int(data[1])
l = int(data[2])

scores = [g, c, l]
scores.sort()

if scores[2] - scores[0] >= 10:
    print("check again")
else:
    print(f"final {scores[1]}")