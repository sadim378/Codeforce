t = int(input())

for i in range(t):
    n = int(input())

    round_numbers = []
    place = 1

    while n > 0:
        digit = n % 10

        if digit != 0:
            round_numbers.append(digit * place)

        n = n // 10
        place = place * 10

    print(len(round_numbers))
    print(*round_numbers)