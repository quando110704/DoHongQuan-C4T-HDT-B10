items = ['45', '68', '70', '82']
new_score = input("what is your new high score? ")
items.append(new_score)
u = sorted(items, reverse = True)
print("high scores : ", u)
