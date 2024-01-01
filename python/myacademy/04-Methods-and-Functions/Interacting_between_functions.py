# Several functions interacting with each other
# Three Cup Monte

from random import shuffle

# Initial list
comp_choice = ['_', 'O', '_']


# Shuffle List
def shuffle_list(computer_choice):
    shuffle(computer_choice)
    return computer_choice


def player_guess():
    user_guess = ''

    while user_guess not in ['0', '1', '2']:
        user_guess = input("Enter your choice (0,1 or 2): ")

    return int(user_guess)


def check_guess(mylist, user_guess):
    if mylist[user_guess] == 'O':
        print("You win")
    else:
        print("Computer wins")

    print("You have entered: ",
          user_guess)
    print("Computer's choice: ", mylist)


mixed_up_list = shuffle_list(comp_choice)
guess = player_guess()

check_guess(mixed_up_list, guess)
