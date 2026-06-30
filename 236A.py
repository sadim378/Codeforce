name = input()

unique_char = set(name)

count = len(unique_char)

if count % 2 == 0:
        print("CHAT WITH HER!")
else:
        print("IGNORE HIM!")