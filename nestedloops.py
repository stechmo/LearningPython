print("How many rows do you want me to create?")
rows = input()

for i in range(1, int(rows)+1):
    for j in range(i):
        print(i, end="")
    print()