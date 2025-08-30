#Giveb number between 1 to 100
num=int(input("Enter a number between 1 to 100: "))
if num<1 or num>100:
    print("Invalid input! Please enter a number between 1 to 100.")
else:
    print("Valid input! You entered:", num)