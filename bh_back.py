import random

class BH_back:
    def __init__(self):

        # initialize empty lists for num of bulls and num of hits
        self.number_of_bulls = 0
        self.number_of_hits = 0

        # Secret Code
        self.secret_num = self.generateNum()
        self.tries = 8
        self.current_try = 0

        # self.guess = int(input("Enter your guess: "))

    def initiat_game(self, tries):
        self.tries = tries
        self.secret_num = self.generateNum()
        print(self.secret_num)

    # return tuple in this template:
    # ("MSG", -1(error)/0(in game)/1(win)/2(lose) , bulls, cows)
    def check_guess(self, guess):
        self.guess = guess
        if not self.noDuplicates(guess):
            return "Number should not have repeated digits. Try again.", -1, 0, 0
        if guess < 1000 or guess > 9999:
            return "Enter 4 digit number only. Try again.", -1, 0, 0
        bull_cow = self.numOfBullsCows(self.secret_num, guess)
        if bull_cow[0] == 4:
            return "You guessed right!", 1, bull_cow[0], bull_cow[1]
        self.tries -= 1
        if self.tries == 0:
            return f"You ran out of tries. Number was {self.secret_num}", 2, bull_cow[0], bull_cow[1]
        return "", 0, bull_cow[0], bull_cow[1]

    def get_guess(self, guess):
        self.guess_numbers = guess

    # Returns list of digits of a number
    def getDigits(self, num):
        return [int(i) for i in str(num)]

    # Returns True if number has no duplicate digits otherwise False
    def noDuplicates(self, num):
        num_li = self.getDigits(num)
        if len(num_li) == len(set(num_li)):
            return True
        else:
            return False

    # Generates a 4 digit number
    # with no repeated digits
    def generateNum(self):
        while True:
            num = random.randint(1000, 9999)
            if self.noDuplicates(num):
                return num

    # Returns common digits with exact
    # matches (bulls) and the common
    # digits in wrong position (cows)
    def numOfBullsCows(self, num, guess):
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
