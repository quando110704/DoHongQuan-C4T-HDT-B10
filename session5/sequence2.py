while True:
    number = int(input("give me a number "))
    for i in range(0, number):
        print(i, end=', ')
    if number > 0:
        print("this is the sequence")
        break
    else:
        print("the number < 0")

