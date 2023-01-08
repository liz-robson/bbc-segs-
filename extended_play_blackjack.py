import random

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}


def deal_card(hand):                    # deals 1 card
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)


def deck_reset(hand1, hand2):
    used_cards = hand1 + hand2
    deck.extend(used_cards)
    return deck


def deal_hand(player, dealer):  # deals opening hand to player and dealer
    for x in range(2):
        deal_card(player)
    print(f'{name}, your opening hand is {player}')
    for x in range(2):
        deal_card(dealer)
    print(f'The dealer has [ {dealer[0]} ]')


def low_score(hand):                    # calculates value for 'Ace's low' hand
    total = 0
    for i in hand:
        if i in values:
            total += values[i]
    return total


def high_score(hand):                   # calculates value for 'Ace's high' hand
    total = 0
    for i in hand:
        if i in values:
            total += values[i]
    return total + 10


def score(hand):                        # compares Ace's low & high value and decides best total for the hand
    if 'A' in hand:
        high_score(hand)
        if high_score(hand) <= 21:
            total = high_score(hand)
            return total
        else:
            low_score(hand)
            total = low_score(hand)
            return total
    else:
        low_score(hand)
        total = low_score(hand)
        return total


def player_choice(hand, total):         # runs through player choice to hit/stand
    while total == 21:
        print(f'Your score is {total}\nYou have Blackjack!')
        break
    else:
        player_in = True
        while player_in:
            choice = input("Would you like to:\nH: Hit\nS: Stand\n")
            while choice.upper() == 'S':
                print(f'Your final score is {total}')
                player_in = False
                break
            else:
                deal_card(hand)
                total = score(hand)
                print(f'Your hand is now {hand}')
                if total > 21:
                    print(f'Your score is {total}\nBust! Dealer wins')
                    player_in = False
                elif total == 21:
                    print(f'Your score is {total}. You have Blackjack :)')
                    player_in = False
                elif total < 21:
                    player_in = True
        else:
            return


def dealer_choice(hand, total):             # decides dealer choice and when to stand
    print(f"The dealer's hand is {hand}")
    while total < 17:
        print(f'The dealer will draw again')
        deal_card(hand)
        total = score(hand)
        print(f"The dealer's hand is now {hand}")
    else:
        if total > 21:
            print(f"The dealer's score is {total}")
            return total
        else:
            print(f"The dealer will stand. The dealer's score is {total}")
            return total


def decide_winner(player_score, dealer_score):      # chooses winner by evaluating final scores after standing
    if dealer_score == player_score:
        print(f'Its a push!')
    elif dealer_score == 21:
        print(f'Blackjack for Dealer! Dealer wins')
    elif player_score == 21:
        print(f'Blackjack for {name}, {name} wins!')
    elif dealer_score > 21:
        print(f'Dealer bust, {name} wins!')
    elif dealer_score > player_score:
        print(f'Dealer wins!')
    elif player_score > dealer_score:
        print(f'{name} wins!')


def game():                                             # runs game
    deal_hand(player, dealer)
    player_choice(player, score(player))
    while score(player) > 21:
        break
    else:
        dealer_choice(dealer, score(dealer))
        decide_winner(score(player), score(dealer))


name = input('What is your name?\n')                       # script to start game play
play = input('Would you like to play a game of Blackjack?\nY: Yes\nN: No\n')
while play.upper() == 'Y':
    player = []
    dealer = []
    game()
    play = input('Would you like to play another game of Blackjack?\nY: Yes\nN: No\n')
    deck_reset(player, dealer)
else:
    print('Goodbye, see you next time')


# Scenarios

# Given my score is updated
# When it is 22 or more
# Then I am ‘bust’ and do not have a valid hand

# hand = ['K', '10']
# total = score(hand)
# player_choice(hand, total)   # Select to 'hit' to show Bust (unless you get an Ace!)

# Given I have a king and an ace
# When my score is evaluated
# Then my score is 21

# hand = ['K', 'A']
# total = score(hand)
# player_choice(hand, total)
#

# Given I have a king, a queen, and an ace
# When my score is evaluated
# Then my score is 21

# hand = ['K', 'A', 'Q']
# total = score(hand)
# player_choice(hand, total)

# Given that I have a nine, an ace, and another ace
# When my score is evaluated
# Then my score is 21

# hand = ['9', 'A', 'A']
# total = score(hand)
# player_choice(hand, total)