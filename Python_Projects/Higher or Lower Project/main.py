import random
from traceback import print_tb

# display art
from art import logo,vs
from game_data import data
import random


# generate a random account from the game


# format the account data in to the printable format
def format_data(account):

    account_name = account["name"]
    account_descrip = account["description"]
    account_country = account["country"]
    return f"{account_name},{account_descrip},{account_country}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess=="b"



print(logo)
score = 0
should_continue = True
account_b = random.choice(data)
while should_continue:
    account_a= account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask userr for a guess
    guess =input("Who has more followers? Type 'A' or 'B' : ").lower()


    # check if user is correct
    #--get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    #--use if statement to check if user is correct
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    #Give user feedback on their guess
    if is_correct:
        score +=1
        print(f"you are right! your score: {score}")
    else:
        should_continue= False
        print(f"wrong! your score: {score}")
#score keeping

#Make the game repeatable

# Making account at position B become the next account at position A.







