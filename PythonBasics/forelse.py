#for else break statement program
cart= ['apple','banana','grapes','orange','milk','bread','rice']
for item in cart:
    if item=='milk' or item=='bread':
        print("Item found in cart:",item)
        break
else:
    print("Item not found in cart")