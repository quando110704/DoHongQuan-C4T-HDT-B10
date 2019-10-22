items = ['football', 'basketball', 'pingpong']
print(*items)
new_items = input("what do you want to add? ")
items.append(new_items)
print(*items)