from math import gcd

Y, W = map(int, input().split())

winning = 7 - max(Y, W)

g = gcd(winning, 6)

print(f"{winning //g}/{6 // g}")