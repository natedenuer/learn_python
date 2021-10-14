s = input()
counter = 1

for index in range(1, len(s)):
    a = s[index]
    if s[index - 1] == s[index]:
        counter += 1

    else:
        print(f'{s[index - 1]}{counter}', end='')
        counter = 1

print(f'{s[-1]}{counter}')