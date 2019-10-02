items = ['football', 'basketball', 'pingpong']
item_to_delete = int(input("enter the number "))
items.pop(item_to_delete)
print(*items ,sep=', ')
