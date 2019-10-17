""" 
    Rock Paper Scissors
    1. Define variables 
    2. Ask for user input
    3. PC chooses randomly
    4. Check user choice vs PC choice
    5. Find out winner
""" 
import sys
import random


choices = ['paper', 'scissors', 'rock']


def get_input():
    user_choice = input('Please enter your choice: rock, paper or scissors. ')

    if user_choice == 'paper':
        user_choice = 0
    elif user_choice == 'scissors':
        user_choice = 1 
    elif user_choice == 'rock':
        user_choice = 2 
    else:
        print('Please enter rock, paper or scissors.')
        sys.exit()

    PC_choice = random.randint(0, 2)
    return user_choice, PC_choice
    check_winner()


def check_winner(user_choice, PC_choice):
    if user_choice == PC_choice:
        print('Draw. {} is equal to {}'.format(choices[PC_choice], choices[user_choice]))

    elif (user_choice > PC_choice and (user_choice != 2 and PC_choice != 0)) or \
        (user_choice == 0 and PC_choice == 2):
        print('You win! {} beats {}.'.format(choices[user_choice], choices[PC_choice]))

    elif user_choice < PC_choice or (user_choice == 2 and PC_choice == 0):
        print('Try again! {} beats {}.'.format(choices[PC_choice], choices[user_choice]))
        get_input()

    else:
        print('You win! {} beats {}.'.format(choices[user_choice], choices[PC_choice]))

        
def test_function(check_winner):
    print('Testing function!')
    outer_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

    for inner_list in outer_list:
        user_choice, PC_choice = inner_list
        check_winner(user_choice, PC_choice)


def main():
    user_choice, PC_choice = get_input()
    check_winner(user_choice, PC_choice)
    #test_function(check_winner)
    

if __name__ == '__main__':
    main()