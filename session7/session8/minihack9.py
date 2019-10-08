numbers = input("what numbers do you want to caculate: ").split(' ')
from decimal import Decimal
summ = sum(Decimal(i) for i in numbers)
print("sum of the numbers: ", summ)
