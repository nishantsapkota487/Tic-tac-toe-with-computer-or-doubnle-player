#Tictac toe project

import random
table = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

count = 0

#To check the numbers played by humand and computers
already_exisitng_num = []

#This function helps to create the table
def create_table():
    print(f"{table[0][0]} | {table[0][1]} | {table[0][2]}")
    print(f"--|---|--- ")
    print(f"{table[1][0]} | {table[1][1]} | {table[1][2]}")
    print(f"--|---|---")
    print(f"{table[2][0]} | {table[2][1]} | {table[2][2]}")

#This function determines who is the winner
def determine_winner():
    #left diagional
    if (table[0][0] == 'x' and table[1][1] == 'x' and table[2][2] == 'x') or (table[0][0] == 'o' and table[1][1] == 'o' and table[2][2] == 'o'):
        return True, table[0][0]

    #right diagonal
    if (table[0][2] == 'x' and table[1][1] == 'x' and table[2][0] == 'x') or (table[0][2] == 'o' and table[1][1] == 'o' and table[2][0] == 'o'):
        return True, table[0][2]

    #leftmost column
    if (table[0][0] == 'x' and table[1][0] == 'x' and table[2][0] == 'x') or (table[0][0] == 'o' and table[1][0] == 'o' and table[2][0] == 'o'):
        return True, table[0][0]

    #middle column
    if (table[0][1] == 'x' and table[1][1] == 'x' and table[2][1] == 'x') or (table[0][1] == 'o' and table[1][1] == 'o' and table[2][1] == 'o'):
        return True, table[0][1]

    #rightmost column
    if (table[0][2] == 'x' and table[1][2] == 'x' and table[2][2] == 'x') or (table[0][2] == 'o' and table[1][2] == 'o' and table[2][2] == 'o'):
        return True, table[0][2]

    #uppermost row
    if (table[0][0] == 'x' and table[0][1] == 'x' and table[0][2] == 'x') or (table[0][0] == 'o' and table[0][1] == 'o' and table[0][2] == 'o'):
        return True, table[0][0]

    #middle row
    if (table[1][0] == 'x' and table[1][1] == 'x' and table[1][2] == 'x') or (table[1][0] == 'o' and table[1][1] == 'o' and table[1][2] == 'o'):
        return True, table[1][0]

    #lowermost row
    if (table[2][0] == 'x' and table[2][1] == 'x' and table[2][2] == 'x') or (table[2][0] == 'o' and table[2][1] == 'o' and table[2][2] == 'o'):
        return True, table[2][0]

    return False, table[0][0]


#This fucntion is called if user opts to play double player
def user_input():
    global count, table
    user_num  = 0

    if count % 2 == 0:
        user_num = int(input("Enter the number from 1 to 9 for char x "))
    else:
        user_num = int(input("Enter the number from 1 to 9 for char o "))

    #To ensure that the number is not out of range
    while user_num > 9 or user_num < 0 or user_num in already_exisitng_num:
        if count % 2 == 0:
            user_num = int(input("Enter the number from 1 to 9 for char x "))
        else:
            user_num = int(input("Enter the number from 1 to 9 for char o "))

    already_exisitng_num.append(user_num)

    if user_num >= 1 and user_num <= 3 and count % 2 == 0:
        table[0][user_num-1] = 'x'

    elif user_num >= 1 and user_num <= 3 and count % 2 != 0:
        table[0][user_num-1] = 'o'

    elif user_num >= 4 and user_num <= 6 and count % 2 == 0:
        if user_num == 5:
            table[1][1] = 'x'
        elif user_num == 6:
            table[1][2] = 'x'
        else:
            table[1][0] = 'x'

    elif user_num >= 4 and user_num <= 6 and count % 2 != 0:
        if user_num == 5:
            table[1][1] = 'o'
        elif user_num == 6:
            table[1][2] = 'o'
        else:
            table[1][0] = 'o'

    elif user_num >= 7 and user_num <= 9 and count % 2 == 0:
        if user_num == 7:
            table[2][0] = 'x'
        elif user_num == 8:
            table[2][1] = 'x'
        else:
            table[2][2] = 'x'

    elif user_num >= 7 and user_num <= 9 and count % 2 != 0:
        if user_num == 7:
            table[2][0] = 'o'
        elif user_num == 8:
            table[2][1] = 'o'
        else:
            table[2][2] = 'o'


    count += 1



def computer_move():
    global count, already_exisitng_num

    #Range of numbers to choose from by the computer
    choices_of_num = [i for i in range(1, 10)]
    computer_num = random.choice(choices_of_num)


    #To ensure that computer does not choose already chosen number
    while computer_num in already_exisitng_num:
        computer_num = random.choice(choices_of_num)

    already_exisitng_num.append(computer_num)

    print(f"Computer played at box number { computer_num }")

    if computer_num >= 1 and computer_num <= 3:
        table[0][computer_num-1] = 'o'

    elif computer_num >= 4 and computer_num <= 6:
        if computer_num == 5:
            table[1][1] = 'o'
        elif computer_num == 6:
            table[1][2] = 'o'
        else:
            table[1][0] = 'o'

    elif computer_num >= 7 and computer_num <= 9:
        if computer_num == 7:
            table[2][0] = 'o'
        elif computer_num == 8:
            table[2][1] = 'o'
        else:
            table[2][2] = 'o'

    count += 1



#This function is called if user opts to play with the computer
def human_move():
    global count, already_exisitng_num

    user_num = int(input("Enter the number you want put from 1 to 9 "))
    print()
    #To ensure that the number is within the range
    while user_num > 9 or user_num < 0 or user_num in already_exisitng_num:
        user_num = int(input("Enter the number you want to put form 1 to 9 that is not already used by you or computer "))

    print(f"You entered the number { user_num }")

    already_exisitng_num.append(user_num)

    if user_num >= 1 and user_num <= 3 and count % 2 == 0:
        table[0][user_num-1] = 'x'

    elif user_num >= 4 and user_num <= 6 and count % 2 == 0:
        if user_num == 5:
            table[1][1] = 'x'
        elif user_num == 6:
            table[1][2] = 'x'
        else:
            table[1][0] = 'x'

    elif user_num >= 7 and user_num <= 9 and count % 2 == 0:
        if user_num == 7:
            table[2][0] = 'x'
        elif user_num == 8:
            table[2][1] = 'x'
        else:
            table[2][2] = 'x'

    count += 1



def main():
    option = input("Enter 1 to play with double player and 2 to play with computer")
    print()
    while option != "1" and option != "2":
        option = input("Enter 1 to play with double player and 2 to play with computer")
    if option == "1":
        while True:
            create_table()
            user_input()
            bool_val, winner_char = determine_winner()
            if bool_val:
                print(f"The winner is { winner_char }")
                create_table()
                break
            if count == 9:
                print("None of the players won. Its a draw")
                create_table()
                break
            print()
            print()
    else:
        print("Computer is o and Human is x")
        while True:
            create_table()
            human_move()

            bool_val, winner_char = determine_winner()
            if bool_val:
                if winner_char == 'x':
                    print("Human won")
                    create_table()
                else:
                    print("Computer won")
                    create_table()
                break
            if count == 9:
                print("Its a draw. Neither Human nor computer won")
                create_table()
                break

            create_table()
            computer_move()

            bool_val, winner_char = determine_winner()
            if bool_val:
                if winner_char == 'x':
                    print("Human won")
                    create_table()
                else:
                    print("Computer won")
                    create_table()
                break
            if count == 9:
                print("Its a draw. Neither Human nor computer won")
                create_table()
                break
            print()
            print()



main()
