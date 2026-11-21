#Inverted Right-Angled Triangle
n=5

for i in range(n,0,-1): #reverse loop from n to 1
    for j in range(i): #for printing stars
        print("*",end=" ")
    print() #go to next line
