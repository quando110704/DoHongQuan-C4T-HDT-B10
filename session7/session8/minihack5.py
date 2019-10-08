colors = ['blue', 'red', 'green']
color_to_delete = input("enter the item you want to delete ")
colors.remove(color_to_delete)
print(*colors ,sep=', ')
colour_to_delete = int(input("enter the number you want to delete "))
colors.pop(colour_to_delete)
print(*colors ,sep=', ')
