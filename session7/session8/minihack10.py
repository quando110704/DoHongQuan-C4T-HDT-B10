numbers = (input("enter numbers: ").split(' ,')
out = []
i = int(numbers)
for i in numbers:
    if i % 2 == 0:
        out.append(i)
        print(out)
    else:
        print("this can not be divided by 2")