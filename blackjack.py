from src.deck import Game, Player


def play():
    blackjack = input('Would you like to play a game of Blackjack?\nY: Yes\nN: No\n')
    while blackjack.upper() == 'Y':
        hand = []
        deal = Game()
        player = Player()
        deal.opening_hand(hand)
        player.turn(hand)
        blackjack = input('Would you like to play another game of Blackjack?\nY: Yes\nN: No\n')
    else:
        print('Goodbye, see you next time')


if __name__ == '__main__':
    play()
