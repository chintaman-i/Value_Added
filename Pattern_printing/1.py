#Right angle trainge
#n=int(input("Enter NUmber"))
#for i in range(1,n+1):
  #  print("*"*i,end="\n")

#Right angle trainge
#n=int(input("Enter NUmber"))
#for i in range(1,n+1,-1):
  #  print("*"*i,end="\n")

#square
# n=4
# for rows in range(n):
#    for col in range(n):
#        print("*",end='')
#    print()




# n=5
# for i in range(1,n+1): 
#     print(" ",end="\n")
#     for j in range(1,i+1):
#         print(j,end='')


#
# n=int(input("Enter NUmber"))
# for i in range(1,n+1):
#     print(" ",end="\n")
#     for j in range(i):
#         print(i,end='')


# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("*", end="")
#     print()


# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()

# n = 5
# for i in range(n,0,-1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()


# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()

n=5
for i in range(1,n+1):
    for j in range(i,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


