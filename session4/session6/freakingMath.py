import random
count = 0
while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    saiSo = random.randint(-3, 3)
    sum = num1 +num2 + saiSo

    print("{} + {} = {}".format(num1, num2, sum))

    answer = input("T and F ? ").lower()

    if saiSo == 0:
        if answer == "t":
            print('correct')
            count=count+1
            print(count)
            

        else:
            print("game over")
            count=count-1
            print(count)
            

    
    else:
        if answer == 'f':
            print("correct")
            count=count+1
            print(count)
            

        else:
            print("game over")
            count=count-1
            print(count)
    
            
            
        