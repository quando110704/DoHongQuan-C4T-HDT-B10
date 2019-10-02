items = ['football', 'basketball', 'pingpong']
print(*items, sep=', ')
new_items = input("what đo you want to add ")
items.append(new_items)
print(items[1])
print(items[2])
print(items[3])