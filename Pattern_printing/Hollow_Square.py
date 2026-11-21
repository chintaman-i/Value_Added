#Hollow Square
n=5
for i in range(n):#rows printing
    for j in range(n):#columns printing
        if i==0 or i==n-1 or j==0 or j==n-1:#printing stars on edge
            print("*",end=" ")
        else:
            print(" ",end=" ")#printing spaces inside
    print()#next line
