items = ['football', 'basketball', 'pingpong']
item_to_delete = input("enter the item you want to delete ")
items.remove(item_to_delete)
print(*items ,sep=', ')