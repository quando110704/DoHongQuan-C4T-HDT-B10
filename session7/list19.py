import random
word = "champion"
shuffled = list(word)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print(shuffled)