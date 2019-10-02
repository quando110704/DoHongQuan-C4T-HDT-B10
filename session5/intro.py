month = int(input("what month is it? "))
print(month)

if 0 < month <= 3:
    print("spring")
elif 0 < month <= 6:
    print("summer")
elif 0 < month <= 9:
    print("autumn")
elif 0 < month <= 12:
    print("winter")
else:
    print("nothing")