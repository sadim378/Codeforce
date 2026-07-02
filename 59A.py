word = input()

upper_count = 0
lower_count = 0

for ch in word:
    if ch.isupper():
        upper_count += 1
    else:
        lower_count += 1

if upper_count > lower_count:
    print(word.upper())
else:
    print(word.lower())