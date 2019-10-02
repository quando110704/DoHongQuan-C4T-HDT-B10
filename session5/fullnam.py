while True:
    name = input("your name ")
    middlen = input("your middle name ")
    lastn = input("your last name ") 
    x = name.upper()
    y = middlen.upper()
    z = lastn.upper()
    print(z, y, x)
    if x.isalpha() and y.isalpha() and z.isalpha():
        print("success")
        break
    else:
        print("you must write words")