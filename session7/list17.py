items = ['tennis', 'pingpong', 'football', 'soccer', 'basketball']
choices = input("what do you choose? ").lower()
if choices == 'c':
    new_item = input("what do you want to add? ")
    items.append(new_item)
    print(*items, sep=', ')
elif choices == 'r':
    L = len(items)
    if L == 0:
        print("no items")
    else:
        print(*items, sep=', ')
elif choices == 'u':
    i = int(input("what number do you want to update? "))
    items[i] = input("you want to change it to: ")
    print(*items, sep=', ')

elif choices == 'd':
    item_to_delete = int(input("what position you want to delete? "))
    items.pop(item_to_delete)
    print(*items, sep=', ')
else:
    print("you must choose c or r or u or d ")