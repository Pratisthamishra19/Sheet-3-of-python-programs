n = int(input("Enter a number: ")) 
for i in range(n):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()  
for j in range(2 * n):
    print("*", end="")
print()

