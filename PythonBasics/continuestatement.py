#continue statement program
cart= ['apple','banana','grapes','orange','milk','bread','rice']
for item in cart:
    if item=='milk' or item=='bread':
        continue
    print("You can buy",item)