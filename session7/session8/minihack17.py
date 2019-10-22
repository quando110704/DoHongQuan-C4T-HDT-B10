items = ['45', '68', '70', '82', '26', '99']
new_score = input("what is your new high score? ")
items.append(new_score)
u = sorted(zip(items), reverse=True)[:5]
print("high scores : ", u)