n=5
for i in range(1, n + 1):#for upper half rows
    for j in range(n - i):#for spaces
        print("  ", end="")
    for k in range(2 * i - 1):#for stars
        print("*", end=" ")
    print()#next line
for i in range(n-1,0,-1):#for lower half rows
    for j in range(n - i):#printing spaces
        print("  ", end="")
    for k in range(2 * i - 1):#for printing stars
        print("*", end=" ")
    print()