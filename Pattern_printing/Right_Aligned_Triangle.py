#Right Aligned Triangle
n=5
for i in range(1,n+1): #for rows printing
    for j in range(n-i): #for printing spaces
        print("  ",end="")
    for k in range(i): #for printing stars
        print("*",end=" ")
    print()
