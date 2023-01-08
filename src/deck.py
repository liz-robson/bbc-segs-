import random


class Deck:
    def __init__(self):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

    def deal_card(self, hand):
        card = random.choice(self.cards)
        hand.append(card)
        self.cards.remove(card)


class Game:
    def __init__(self):
        self.Deck = Deck()

    def opening_hand(self, hand):
        for x in range(2):
            self.Deck.deal_card(hand)
        print(f'Your opening hand is {hand}')

    def low_score(self, hand):
        total = 0
        for i in hand:
            if i in self.Deck.values:
                total += self.Deck.values[i]
        return total

    def high_score(self, hand):
        total = 0
        for i in hand:
            if i in self.Deck.values:
                total += self.Deck.values[i]
        return total + 10

    def score(self, hand):
        if 'A' in hand:
            self.high_score(hand)
            if self.high_score(hand) <= 21:
                total = self.high_score(hand)
                return total
            else:
                self.low_score(hand)
                total = self.low_score(hand)
                return total
        else:
            self.low_score(hand)
            total = self.low_score(hand)
            return total


class Player:
    def __init__(self):
        self.game = Game()
        self.deck = Deck()
        self.total = 0

    def turn(self, hand):
        self.total = self.game.score(hand)
        while self.total == 21:
            print(f'Your score is {self.total}. You have Blackjack :)')
            break
        else:
            player_in = True
            while player_in:
                choice = input("Would you like to:\nH: Hit\nS: Stand\n")
                while choice.upper() == 'S':
                    print(f'Your final score is {self.total}')
                    player_in = False
                    break
                else:
                    self.deck.deal_card(hand)
                    self.total = self.game.score(hand)
                    print(f'Your hand is now {hand}')
                    if self.total > 21:
                        print(f'Your score is {self.total}\nBust! Your game is over')
                        player_in = False
                    elif self.total == 21:
                        print(f'Your score is {self.total}. You have Blackjack :)')
                        player_in = False
                    elif self.total < 21:
                        player_in = True
            else:
                return


