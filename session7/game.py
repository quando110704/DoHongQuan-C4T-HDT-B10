import os
import random
import sys

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Notify user of his/her location.
def print_coor(player):
    print("Your coordinates now are x: {}, y:"
              " {}.".format(player['x'], player['y']))

def print_help():
    print("Type a command to execute the desired action:\n"
          "'up' -> go up\n"
          "'down' -> go down\n"
          "'left' -> go left\n"
          "'right' -> go right\n"
          "'help' -> show help\n"
          "'quit' -> exit the game\n")

def exit_game():
    print("Exiting into the light...")
    sys.exit()

def play_again():
    try:
        user_response = input("Would you like to try your luck again? "
                              "Y/n\n> ").lower()
    except ValueError:
        print("What did you say? Y/n\n> ")
    else:
        if user_response == 'n':
            exit_game()
        else:
            play()

def print_map(x_axis, y_axis, player, player_traces):
    # Start by drawing the top of the map.
    map = "+" + ("---+" * max(x_axis)) + "\n"

    # Draw line by line. Since the origin is located
    # at the bottom left corner, use the reversed order
    # of the y axis.
    for y in reversed(y_axis):
        map += "|"

        # For each quadrant, draw a space and decide what
        # to fill it with depending on what's in there;
        # the player, a trace, or just empty space.
        for x in x_axis:
            if x == player['x'] and y == player['y']:
                fill = "X"
            elif (x, y) in player_traces:
                fill = "*"
            else:
                fill = " "
            map += " {} ".format(fill)
            if x == max(x_axis):
                map += "|\n"
            else:
                map += " "

        # Draw the decoration between lines.
        if y > min(y_axis):
            map += "+" + ("    " * (max(x_axis) - 1)) + "   +\n"

    # Finish it off by drawing the bottom of the map.
    map += "+" + ("---+" * max(x_axis))
    print(map)

def play():
    clear_screen()

    # Create a map of coordinates.
    x_axis = tuple(range(1, 11))
    y_axis = tuple(range(1, 11))

    # Put the player on the map.
    player = {'x': random.choice(x_axis), 'y': random.choice(y_axis)}

    # Create a trace the player will leave as he/she moves around.
    player_traces = []

    # Put the monster on the map while making sure it won't
    # appear in the same spot as the player.
    monster_spawn_area_x = list(x_axis)
    monster_spawn_area_x.remove(player['x'])
    monster_spawn_area_y = list(y_axis)
    monster_spawn_area_y.remove(player['y'])
    monster = {'x': random.choice(monster_spawn_area_x), 'y': random.choice(monster_spawn_area_y)}

    # Put the exit door, again making sure not to place it
    # in the same place as the player or the monster.
    door_spawn_area_x = monster_spawn_area_x
    door_spawn_area_x.remove(monster['x'])
    door_spawn_area_y = monster_spawn_area_y
    door_spawn_area_y.remove(monster['y'])
    door = {'x': random.choice(door_spawn_area_x), 'y': random.choice(door_spawn_area_y)}

    print("######################## DUNGEON "
          "ESCAPE #############################\n\n")            
    print("Welcome to 'Dungeon Escape': an adrenaline packed horror game "
          "back from a time when nobody knew what the hell a GUI was.\n\n"
          "Find your way out from the dungeon by moving one step at a time "
          "without being noticed by the evil monster lurking in the "
          "shadows. Good luck! "
          "You are gonna need it.\n\n")
    # Tell the user how to play the game from the very start.
    print_help()
    print("The dungeon's size is 10 by 10. You can move one step at a time.")
    print_coor(player)
    print_map(x_axis, y_axis, player, player_traces)

    while True:
        # Let the player be able to move one step at a time.
        try:
            direction = input("> ").lower()
        except ValueError:
            print("Invalid direction. Try again.")
        else:
            clear_screen()

            # Make help available to the player at any time.
            if direction == 'help':
                print_help()
            # Let the player leave the game at any moment.
            elif direction == 'quit':
                exit_game()
            elif direction == 'up':
                # Don't let the player go beyond the top border.
                if (player['y'] + 1) > max(y_axis):
                    print('You hit a wall. Try going in another direction.')
                else:
                    print('Went UP one step.')
                    player_traces.append(tuple([player['x'], player['y']]))
                    player['y'] += 1
            elif direction == 'down':
                # Don't let the player go beyond the bottom border.
                if (player['y'] - 1) < min(y_axis):
                    print('You hit a wall. Try going in another direction.')
                else:
                    print('Went DOWN one step.')
                    player_traces.append(tuple([player['x'], player['y']]))
                    player['y'] -= 1
            elif direction == 'left':
                # Don't let the player go beyond the left border.
                if (player['x'] - 1) < min(x_axis):
                    print('You hit a wall. Try going in another direction.')
                else:
                    print('Went LEFT one step.')
                    player_traces.append(tuple([player['x'], player['y']]))
                    player['x'] -= 1
            elif direction == 'right':
                # Don't let the player go beyond the right border.
                if (player['x'] + 1) > max(x_axis):
                    print('You hit a wall. Try going in another direction.')
                else:
                    print('Went RIGHT one step.')
                    player_traces.append(tuple([player['x'], player['y']]))
                    player['x'] += 1
            else:
                print('Wrong direction. Try again.')

        # Notify user of his/her new location.
        print_coor(player)
        print_map(x_axis, y_axis, player, player_traces)

        # Make character die if it lands on the monster.
        if player['x'] == monster['x'] and player['y'] == monster['y']:
            # Player loses the game if character dies and the game ends.
            print("As soon as you step into a new area, you are caught by "
                  "the nefarious creature who drags you to the very doors of hell.")
            # Ask user if he/she wants to play again once game is over.
            play_again()

        # Player wins if character reaches the door.
        if player['x'] == door['x'] and player['y'] == door['y']:
            print("You find the exit! Without looking back you run desperately "
                  "while feeling the ominus presence rushing after you. But "
                  "you finally make it through in one peace. The door closes "
                  "and you never look back. Congratulations!")
            # Ask user if he/she wants to play again once game is over.
            play_again()

play()


