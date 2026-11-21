#Butter fly pattern
n = 5
for i in range(1, n + 1): #for upper half rows
    for j in range(i):
        print("*", end=" ")
    for k in range(2 * (n - i)):#for middle spaces
        print("  ", end="")

    for j in range(i):
        print("*", end=" ")#for right side stars

    print()
for i in range(n - 1, 0, -1):#for lower half rows

    for j in range(i): #for left side stars
        print("*", end=" ")
    for k in range(2 * (n - i)):#for middle spaces
        print("  ", end="")
    for j in range(i):#for right side stars
        print("*", end=" ")
    print() #go to next line
