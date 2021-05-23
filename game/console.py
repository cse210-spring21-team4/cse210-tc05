import os
from game.parachute_tracker import Parachute_Tracker

class Console:
    """A code template for a computer console. The responsibility of this
    class of objects is to control CLI display. This includes clearing the
    screen, coordinating the printing of game screen instances (with the
    parachute, word letters/blanks, and prompt), and receiving user input.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        director (Director): An instance of the class of objects known as Director.
        guess (string): A one-character string of promted user input.
        parachute_tracker (Parachute_Tracker): An instance of the class of objects known as Parachute_Tracker.
    """


    def __init__(self):
        """The class constructor.

        Args:
            self (Console): an instance of Console.
        """
        self.guess = ""
        self.parachute = Parachute_Tracker().get_parachute()

    def clear_screen(self):
        """Detects OS type and sends appropriate console command to clear screen.

        Args:
            self (Console): An instance of Console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def write_output(self, word_progress):
        """Performs all output to console, prompts user input.

        Args:
            self (Console): An instance of Console.
        """
        prompt = "\nGuess a letter [a-z]: "
        while True:
            self.clear_screen()

            print(word_progress)
            print(self.parachute)

            letter = input(prompt).lower().strip()
            if letter.isalpha() and len(letter) == 1 and (letter not in word_progress):
                break

            prompt = "\nPlease enter a letter [a-z]\nyou have not guessed yet: "

        self.guess = letter

    def write(self, msg):
        """ (AH)
        Displays string message.

        Args:
            msg = a string parameter.
        """
        print(msg)


    def read_letter(self, msg):
        """Returns user's letter guess as one-character string.

        Args:
            self (Console): An instance of Console.
        """
        # (AH)
        return input(msg)
