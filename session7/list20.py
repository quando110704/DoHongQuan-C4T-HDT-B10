items = ('tennis', 'pingpong', 'football', 'soccer', 'basketball')
import random
item = random.randint(0, 4)
shuffled = list(item)
random.shuffle(shuffled) 
shuffled = ''.join(shuffled)
print(shuffled) 
anwser = input("what word is it? ")
if anwser == shuffled:
    print("correct")
else:
    print("wrong")
            