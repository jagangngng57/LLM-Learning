#accept keyboard input and print it
data=input("Enter something: ")
print("You entered:",data)  
i=0
for x in data:
    print("the character present at ",i,"index is",x)
    i=i+1