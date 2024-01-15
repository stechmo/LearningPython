for i in range(6):
    for j in range(i+1):
        print("x", end="")
    for j in range(20-2*i-2):
        print(" ", end="")
    for j in range(i+1):
        print("o", end="")
    print("")
for i in range(5,-1,-1):
    for j in range(i):
        print("x", end="")
    for j in range(20-2*j-2):
        print(" ", end="")
    for j in range(i):
        print("o", end="")
    print("")