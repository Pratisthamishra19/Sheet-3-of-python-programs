N = int(input("Enter the number of lines: "))
for i in range(N):
    print("*", end="")
    spaces = N - i
    print(" " * spaces, end="")
    print("*")