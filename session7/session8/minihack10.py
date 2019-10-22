numbers = input("enter numbers: ").split(' ,')
out = []
for i in numbers:
    if int(i) % 2 == 0:
        out.append(i)
        print(out)
    else:
        print("this can not be divided by 2")