items = ['football', 'basketball', 'pingpong']
item_to_add = input("enter the item you want to add ")
items.append(item_to_add)
add_more = input("add more ")
items.append(add_more)
add_more2 = input("add more ")
items.append(add_more2)
l = len(items)
for i in range(l):
    print(items[i])