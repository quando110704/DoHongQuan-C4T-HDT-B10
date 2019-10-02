items = ['football', 'basketball', 'pingpong']
print(*items, sep=', ')
new_items = input("what đo you want to add ").upper()
items.append(new_items)
print(items[1].upper())
print(items[2].upper())
print(items[3].upper())