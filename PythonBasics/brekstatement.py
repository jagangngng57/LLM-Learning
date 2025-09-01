#break statement program
i=0
while True:
    print("Hello")
    i=i+1
    if i==5:
        break
print("Out of loop")
for i in range(10):
    if i==5:
        print( "Breaking the loop")
        break
    print(i)