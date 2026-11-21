#Hollow Right angle triangle
n=5
for i in range(1,n+1): #rows printing
    for j in range(1, i + 1): #columns printing
        if i==n  or j==1 or j==i: #printing stars on edge
            print("*",end=" ")
        else:
            print(" ",end=" ")#printing spaces inside
    print()
