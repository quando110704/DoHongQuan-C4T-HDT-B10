numbers = ['1', '32', '45', '12', '22']
from decimal import Decimal
summ = sum(Decimal(i) for i in numbers)
print(summ)

