import random


class BH_back:
    """A class representing the backend of a Bulls and Cows local game play"""

    def __init__(self):
        """
        Initializes an instance of the Bulls and Cows game backend.

        :param: None
        :type: None
        :return: None
        :rtype: None
        """
        # initialize empty lists for num of bulls and num of hits
        self.guess = None
        self.number_of_bulls = 0
        self.number_of_hits = 0

        # Secret Code
        self.secret_num = self.generateNum()
        self.tries = 8
        self.current_try = 0

    def initiate_game(self, tries):
        """
        Initialize the game with the given number of tries.

        :param tries: the number of tries to be given to the player
        :type tries: int
        :return: None
        :rtype: None
        """
        self.tries = tries
        self.secret_num = self.generateNum()
        # print(self.secret_num)

    def check_guess(self, guess):
        """
        Check the player's guess and return a message, status code,
        number of bulls, and number of cows.

        :param guess: the player's guess
        :type guess: int
        :return: a message indicating the result of the guess, a status code, the number of bulls, and the number of cows
        :rtype: tuple[str, int, int, int]
            first string is a msg to display
            int -1(error) / 0(in game) / 1(win) / 2(lose)
            int bulls
            int cows (hits)
        """
        self.guess = guess
        if not self.no_duplicates(guess):
            return "Number should not have repeated digits. Try again.", -1, 0, 0
        bull_cow = self.numOfBullsCows(self.secret_num, guess)
        if bull_cow[0] == 4:
            return "You guessed right!", 1, bull_cow[0], bull_cow[1]
        self.tries -= 1
        if self.tries == 0:
            return f"You ran out of tries. Number was {self.secret_num}", 2, bull_cow[0], bull_cow[1]
        return "", 0, bull_cow[0], bull_cow[1]

    def no_duplicates(self, num):
        """
        Checks if a number has any duplicate digits.

        :param num: The number to check for duplicate digits.
        :type num: str
        :return: Returns True if the number has no duplicate digits, False otherwise.
        :rtype: bool
        """
        if len(num) == len(set(num)):
            return True
        return False

    def generateNum(self):
        """
         Generates a random 4-digit number with no repeated digits.

         :param : None
         :type : None
         :return: A random 4-digit number with no repeated digits.
         :rtype: str
         """
        while True:
            num = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            if self.no_duplicates(num):
                return num

    def numOfBullsCows(self, num, guess):
        """
        Calculates the number of bulls and cows for the given guess.

        Bulls are the digits in the guess that match exactly with the digits in the secret number
        in the same position.

        Cows are the digits in the guess that match with the digits in the secret number, but are not
        in the same position.

        :param num: The secret number.
        :type num: str
        :param guess: The guess made by the player.
        :type guess: str
        :return: A tuple containing the number of bulls and cows respectively.
        :rtype: tuple
        """

        bull_cow = [0, 0]

        for i, j in zip(num, guess):
            if j in num:  # common digit present
                if j == i:  # common digit exact position match
                    bull_cow[0] += 1
                else:  # common digit match but in wrong position
                    bull_cow[1] += 1
        return bull_cow
