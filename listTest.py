#display sum of list elements
numbers = eval(input("Enter a list of numbers: "))
sum = 0
for num in numbers:
    sum += num
print("The sum of the list elements is:", sum)