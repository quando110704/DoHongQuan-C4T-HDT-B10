items = ['football', 'basketball', 'pingpong']
print(*items, sep=', ')
new_items = input("what đo you want to add ")
items.append(new_items)
print(*items, sep=', ')