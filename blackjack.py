import random

def would_you_like_to_play(yes_no_answer):
    if yes_no_answer.lower() == 'y':
        print("Awesome! Let's get started!")
    else:
        print("Thank you, try again later!")

yes_no_answer = input("Welcome to the table! We are about to play some blackjack, would you like to join? y/n ")
would_you_like_to_play(yes_no_answer)
print("Let's get started, I will start by dealing you two cards!")

card1 = random.randint(1, 10)
card2 = random.randint(1, 10)

two_card_total = card1 + card2 


def dealed_cards():
    print(f"{card1} and {card2}")
    return card1 + card2

random_card_total = dealed_cards()  
    
print("You have been dealt a total of", int(random_card_total))  

def playing_blackjack(total):
    if total > 21:
        print("You went over 21, you have lost!")
        exit()
    elif total == 21:       
            print("You just got 21! Blackjack!")
            exit()
    else:
        print("Keep going!")

def keep_playing(total):
    print("You're doing great let's keep playing! Here is your next card")
    card3 = random.randint(1,10)
    print(f"Here is your next card {card3}")
    new_total = total + card3
    print(f"Your new total is {new_total}!")
    return new_total
    
while True:
    another_card = input("Would you like another card? y/n ")
    if another_card == 'y':
        random_card_total = keep_playing(random_card_total)
        playing_blackjack(random_card_total)
    else:
        print("Alright! Let's see what the dealer got!")
        exit()




    





    

    






