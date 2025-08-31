#sum of numbers from given range
n=int(input("Enter starting number: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("The sum of numbers from 1 to",n,"is:",sum)