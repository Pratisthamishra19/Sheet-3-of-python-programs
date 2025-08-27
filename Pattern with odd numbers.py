N = int(input("Enter number of lines: "))
for i in range(1, N + 1):
    for j in range(1, 2 * i, 2):
        print(j, end='*' if j < 2 * i - 1 else '')
    print()