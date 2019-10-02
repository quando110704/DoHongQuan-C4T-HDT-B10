while True:   
    password = input("enter your password ")
    print(password)
    if password.isalpha():
        print("you do not have numbers") 
 
    else:
        print("sucess")
        break