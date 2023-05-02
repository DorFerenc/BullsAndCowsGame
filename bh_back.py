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
        self.guess_numbers = None
        self.number_of_bulls = 0
        self.number_of_hits = 0

        # Secret Code
        self.secret_num = self.generateNum()
        self.tries = 8
        self.current_try = 0

    def initiat_game(self, tries):
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
        if not self.noDuplicates(guess):
            return "Number should not have repeated digits. Try again.", -1, 0, 0
        if guess < 1000 or guess > 9999:
            return "Number can't start with ZERO. Try again.", -1, 0, 0
        bull_cow = self.numOfBullsCows(self.secret_num, guess)
        if bull_cow[0] == 4:
            return "You guessed right!", 1, bull_cow[0], bull_cow[1]
        self.tries -= 1
        if self.tries == 0:
            return f"You ran out of tries. Number was {self.secret_num}", 2, bull_cow[0], bull_cow[1]
        return "", 0, bull_cow[0], bull_cow[1]

    def get_guess(self, guess):
        """
         Set the guess numbers for the current game.

         :param guess: the player's guess
         :type guess: int
         :return: None
         :rtype: None
         """
        self.guess_numbers = guess

    # Returns list of digits of a number
    def getDigits(self, num):
        """
        Get the digits of a number and return them as a list.

        :param num: the number to get the digits of
        :type num: int
        :return: a list of digits of the given number
        :rtype: List[int]
        """
        return [int(i) for i in str(num)]

    def noDuplicates(self, num):
        """
        Checks if a number has any duplicate digits.

        :param num: The number to check for duplicate digits.
        :type num: int
        :return: Returns True if the number has no duplicate digits, False otherwise.
        :rtype: bool
        """
        num_li = self.getDigits(num)
        if len(num_li) == len(set(num_li)):
            return True
        else:
            return False

    def generateNum(self):
        """
         Generates a random 4-digit number with no repeated digits.

         :param : None
         :type : None
         :return: A random 4-digit number with no repeated digits.
         :rtype: int
         """
        while True:
            num = random.randint(1000, 9999)
            if self.noDuplicates(num):
                return num

    def numOfBullsCows(self, num, guess):
        """
        Calculates the number of bulls and cows for the given guess.

        Bulls are the digits in the guess that match exactly with the digits in the secret number
        in the same position.

        Cows are the digits in the guess that match with the digits in the secret number, but are not
        in the same position.

        :param num: The secret number.
        :type num: int
        :param guess: The guess made by the player.
        :type guess: int
        :return: A tuple containing the number of bulls and cows respectively.
        :rtype: tuple
        """

        bull_cow = [0, 0]
        num_li = self.getDigits(num)
        guess_li = self.getDigits(guess)

        for i, j in zip(num_li, guess_li):

            # common digit present
            if j in num_li:

                # common digit exact match
                if j == i:
                    bull_cow[0] += 1

                # common digit match but in wrong position
                else:
                    bull_cow[1] += 1

        return bull_cow
