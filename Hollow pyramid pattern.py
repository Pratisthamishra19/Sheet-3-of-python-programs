rows = int(input("enter the number of Rows: "))
for i in range(rows, 0, -1):
    print('*' * i, end='')
    print(' ' * ((rows - i) * 2), end='')
    print('*' * i)
