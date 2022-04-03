from json.tool import main
from random import choice


def determine_winner(user_choice, computer_choice):
    """
    This function determines the winning choice (or lack thereof) of a single "Rock, Paper, Scissors" Game based 
    on the user's selection and the computer's selection. 
    Params: The function's two paramters are user_choice, which stores the what choice the user selects in the
    rock, paper, scissors game, and computer_choice, which stores which choice the computer randomly generates. 
    Datatypes of Params: user_choice is a String, computer_choice is a String
    Return: This function returns the winning choice (or lack thereof) amongst the user and computer's selections
    (either "paper", "rock", "scissors", or None) 

    Invoke the function like this: determine_winner("rock", "paper")
    """
    
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice


if __name__ == "__main__":

    valid_selections = ["rock", "paper", "scissors"] # only have to update in one place

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_selections:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_selections)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner(u,c)
    if winner == u:
        print("YOU WON")
    elif winner == c:
        print("COMPUTER WON")
    else:
        print("TIE")