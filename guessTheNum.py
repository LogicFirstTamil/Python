import random

def guess_the_num_game():
    if __name__=='__main__':
        print("You are running this directly....")
    print(__name__)
    num = random.randint(1, 20)

    guess = int(input("Can you guess the number I am thinking? Its less than 20: "))

    while num != guess:
        if guess > num:
            print("Your guess in higher")
        else:
            print("Your guess is lower")
        guess = int(input("Guess again: "))

    print("You won!")

guess_the_num_game()




