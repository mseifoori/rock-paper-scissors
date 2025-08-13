import random
from typing import List, Dict, Callable


def main():
    pass


def see_rules() -> str:
    print("Rules:\n"
          "Dear User,\n"
          "You choose between 'Rock', 'Paper' and 'Scissors' while the computer choose between the same options randomly.\n"
          "Rock beats Scissor, Scissors beats Paper and Paper beats Rock."
          "Goodluck with the game :)")


def welcome_user() -> Callable:
    """Asks the user what he wants to do with the game.

    :return: game.play() if the user wants to play
    :rtype: function
    """
    while True:
        w_u_choice: str = input('\n\nWelcome to the famous Rock Paper Scissor game!\n\nTo play, enter p/P\nto exit the game enter q/Q\nto see the rules enter r/R.\n').lower()
        if w_u_choice == 'p':
            game = RockPaperScissors()
            return game.play()
        elif w_u_choice == 'q':
            print('Hope to see you soon :)')
            break
        elif w_u_choice == 'r':
            see_rules()
        else:
            print('Invalid Input!\nPlease if you want to play, enter p/P\nto exit the game enter q/Q\nto see the rules enter r/R.')
            continue


class RockPaperScissors():
    """ Main class for the game.
    """
    def __init__(self):
        self.list_of_choices: List[str] = ['rock', 'paper', 'scissors']
    
    def getting_computer_choice(self) -> str:
        """Get's computer's choice.

        :return: Computer's choice.
        :rtype: str
        """
        self.computer_choice: str = random.choice(self.list_of_choices).lower()
        return self.computer_choice
        
    def getting_user_choice(self) -> Callable:
        """Get's user's choice.

        :return: User's choice.
        :rtype: function
        """
        self.user_choice: str = input(f"\nWhat's your choice? {self.list_of_choices}.\nTo exit the game, enter q/Q:\n")
        return self.user_choice_validation()
        
    def user_choice_validation(self) -> Callable:
        """Validates user's choice.

        :return: game.logic() if the user input is valid, else it calls game's main method.
        :rtype: function
        """
        if self.user_choice not in self.list_of_choices:
            print(f'\nInvalid input! Choose from the list above: {self.list_of_choices}')
            return self.getting_user_choice()
        elif self.user_choice == 'q':
            print('\nBye! Hope to see you soon :)')
        else:
            return self.game_logic()
            
    def game_logic(self) -> str:
        """Decides who is the winner of the game from the rules.

        :return: Game result.
        :rtype: str
        """
        self.winning_conditions: Dict[str: str] = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        if self.user_choice == self.computer_choice:
            return f"\nIt's a tie! You and Computer both chose {self.computer_choice}."
        else:
            if self.winning_conditions[self.user_choice] == self.computer_choice:
                return f"\nCongrats! Your {self.user_choice} beats computer's {self.computer_choice}!"
            else:
                return f"\nOh no! Your {self.user_choice} loses against computer's {self.computer_choice}!"
    
    def play(self) -> Callable:
        """Asks the user whether he/she wants to play another round or not.

        :return: Calls game's main method if the user wants to play again, else it exits the game.
        :rtype: function
        """
        self.getting_computer_choice()
        game_result: Callable = self.getting_user_choice()
        print(game_result)
        
        self.game_continuation: str = input('\nDo you want to play again?\nTo play, enter any key.\nTo exit the game, enter q/Q:\n').lower()
        if self.game_continuation == 'q':
            print('\nThanks for playing! Hope to see you soon :)')
        else:
            return self.play()


welcome_user()

if __name__ == '__main__':
    main()
