n = int(input(" number of rows: "))
for i in range(n):
    print("_" * i, end="")
    print("*", end="")
    if i < n - 1:
        print("*" * (n - i - 1), end="")
    print()



    

  