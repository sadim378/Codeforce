n = int(input())

cards = list(map(int, input().split()))

left = 0
right = n - 1

sereja = 0
dima = 0

for i in range(n):
    if cards[left] > cards[right]:
        picked = cards[left]
        left += 1
    else:
        picked = cards[right]
        right -= 1


    if i % 2 == 0:
        sereja += picked
    else:
        dima += picked

print(sereja, dima)