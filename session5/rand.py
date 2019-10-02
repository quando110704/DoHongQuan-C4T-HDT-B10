import random
 
number = random.randrange(0, 100)
print(number)

if number < 30:
    print("rainy")
elif 30 <= number < 60:
    print("cloudy")
else:
    print("sunny")
