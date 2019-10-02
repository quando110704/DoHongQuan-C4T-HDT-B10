while True:
    username = input("enter your username ")
    email = input("enter your email ")
    password = input("enter your password ")
    password2 = input("enter your password again ")
    if password2 == password:
        print("success")
        break
    else:
        print("incorrect")

    
    