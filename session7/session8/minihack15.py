items = ['45', '68', '70', '82']
new_score = input("what is your new high score? ")
items.append(new_score)
for i, items in enumerate(items):
   print(i+1, "high scores : ", items)

