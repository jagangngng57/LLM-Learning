#dele keyword program
mylist=['apple','banana','grapes','orange','milk','bread','rice']
print("Original list:",mylist)
del mylist[2]  # Delete the item at index 2 ('grapes')
print("List after deleting item at index 2:",mylist)
del mylist[1:4]  # Delete items from index 1 to 3
print("List after deleting items from index 1 to 3:",mylist)
del mylist  # Delete the entire list
print("List deleted",mylist)
#print(mylist)  # This will raise an error since mylist is deleted