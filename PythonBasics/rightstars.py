#right starts display rows 5
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end="")
    print()