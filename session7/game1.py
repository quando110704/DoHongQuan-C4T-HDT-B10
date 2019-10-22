player = {
    "x": 1,
    "y": 2
}
escape = {
    "x": 2,
    "y": 3
}
key = {
    "x": 4,
    "y": 4
}
hello = False
while True:
    for i in range(4):
        for j in range(4):
            if (i == player['y'] - 1) and (j == player['x'] - 1):
                print(" P ", end=" ")
            elif (i == escape['x'] - 1) and (j == escape['y'] - 1):
                print(" E ", end=" ")
            elif (i == key['x'] - 1) and (j == key['y'] - 1):
                if hello == False:
                    print(" K ", end=" ")
                else:
                    print(" - ", end=" ")
                    
            else:
                print(" - ", end=" ")
        print(" ")
    
    
    move = input("A S D W ? ").lower()

    if move == "w":
        player['y'] -= 1
        if player['y'] == 0:
            print("OUT OF MOVE!! ")
            player['y'] += 1
    elif move == "d":
        player['x'] += 1
        if player['x'] == 5:
            print("OUT OF MOVE!! ")
            player['x'] -= 1
            
    elif move == "s":
        player['y'] += 1
        if player['y'] == 5:
            print("OUT OF MOVE!!" )
            player['y'] -= 1
    elif move == "a":
        player['x'] -= 1
        if player['x'] == 0:
            player['x'] += 1
            print("OUT OF MOVE!! ")
    if (player['x'] == key['x']) and (player['y'] == key['y']):
        print("you have the key")
        hello == True
    
       