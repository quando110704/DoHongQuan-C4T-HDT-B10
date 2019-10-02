items = ['football', 'basketball', 'pingpong']
if 'LOL' in items:
    items.remove('LOL')

else:
    print("there is no item")
print(*items ,sep=', ')