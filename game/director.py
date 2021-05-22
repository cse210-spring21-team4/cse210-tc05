from game.console import Console
from game.word_tracker import Word_Tracker
from game.parachute_tracker import Parachute_Tracker
from game.word_select import Word_Select


class Director:
    """
    A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        word_tracker (Word_Tracker): An instance of the class of objects known as Word_Tracker.
        parachute_tracker (Parachute_Tracker):
                An instance of the class of objects known as Parachute_Tracker.
        word_select (Word_Select): An instance of the class of objects known as Word_Select.
    """

    def __init__(self):
        """
        The class constructor.

        Args:
            self (Director): an instance of Director.
        """

        self.console = Console()
        # self.word_tracker = Word_Tracker()
        # (AH) instantiate Word_Tracker() in start_game Method so Word chosen once per game.
        self.keep_playing = True
        # self.parachute_tracker = Parachute_Tracker()
        # (AH) instantiate Parachute_Tracker() in start_game Method
        #               so parachute is refreshed for each game.
        self.word_select = Word_Select()

    def start_game(self):
        """
        Begin by randomly choosing a new word from list to guess.
        Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """

        # (Suggestion 1) Word is selected from MIT 1000 word list in reqmts file.
        # (AH) Class Var assigned to select_word() Method in Word_Select Class <SarahA>.
        self.word = self.word_select.select_word()

        # (AH) Explanation:
        # Create Word_Tracker Class instance in start_game Method so Word_Tracker has self.word.
        # The random chosen word from the MIT list is stored in Word_Tracker Class as self.word
        self.word_tracker = Word_Tracker(self.word)
        # Create Parachute_Tracker Class instance in start game Method
        self.parachute_tracker = Parachute_Tracker()
        # Initialize self.state_num for Parachute_Tracker Class to display
        #                                       one of 5 possible outcomes.
        self.state_num = 0

        # (AH) Loop to call Methods to continue game.
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """ (AH).
        Gets the inputs at the beginning of each round of play. In this case,
        start by displaying current word guessing status and parachute status.
        ie, word with letters filled in and empty dashes, or parachute cuts.

        Args:
            self (Director): An instance of Director.
        """

        # (AH) Word_Tracker Class determine word length.
        # (AH) Get word_status() Method in Word_Tracker Class <Mireya?>.
        word_progress = self.word_tracker.word_status()

        # (AH) Dashes displayed from write() Method in Console Class <Dalton?>.
        self.console.write(word_progress)

        # (AH) Get initial parachute from Parachute_Tracking Class. <Kelton?>.
        # (AH) Parachute_Tracking Class has 5 output possibilities. <Kelton?>.
        # (AH) self.state_num initialized in start_game() Method.
        parachute_progress = self.parachute_tracking.parachute_draw(self.state_num)

        # (AH) Send parachute to console to display.  <Dalton?>
        self.console.write(parachute_progress)

        # (AH) Class Var assigned to gett letter guess from user.
        self.guess_letter = self.console.read_word("Guess a letter [a-z]:  ")

    def do_updates(self):
        """
        Updates the important game information for each round of play.
        In this case, that means the .

        Args:
            self (Director): An instance of Director.
        """

        # (AH) Track Method in Word_Tracker Class determines if
        # 	guess_letter is correct and be put in place of a dash,
        # 	then returns a Boolean for parachute to display same
        # 	parachute as prior turn; or guess_letter is incorrect
        # 	and returns a Boolean for the parachute to be cut.
        # (AH) guess_correct is a Boolean data type.
        self.guess_correct = self.word_tracker.track(self.guess_letter)

        # (AH) increment self.state_num if word_tracker.track(self.guess_letter) is False.
        if not self.guess_correct:
            self.state_num += 1

        # (AH) Parachute_Tracking Class determine correct parachute to display;
        #                                       depending on self.state_num.
        # parachute_progress = self.parachute_tracking.parachute_draw(self.state_num)

        # (AH) Send parachute to console to display.
        # self.console.write(parachute_progress)

    def do_outputs(self):
        """
        Outputs the important game information for each round of play.
        In this case, that means the correct letter guessed fills in a dash
        while an incorrect letter guessed causes a parachute cut.

        Args:
            self (Director): An instance of Director.
        """

        # (AH) Parachute_Tracker Class determines when game ends. <Kelton?>
        # (AH) Game ends when parachute has been cut 4 times.
        current_parachute = self.parachute_tracker.game_continue()
        self.console.write(current_parachute)
        self.keep_playing = self.parachute_tracker.game_continue() is True
