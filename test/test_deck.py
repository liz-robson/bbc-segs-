import unittest
from src.deck import Deck, Game, Player


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_opening_hand(self):    # Scenario test - opening hand deals 2 cards
        hand = []
        game = Game()
        game.opening_hand(hand)
        self.assertEqual(len(hand), 2)

    def test_hit(self):             # Scenario test - when you 'Hit', you get another card
        hand = []
        game = Game()
        play = Player()
        game.opening_hand(hand)
        game.score(hand)
        play.turn(hand)
        self.assertGreater(len(hand), 2)

    def test_stand(self):           # Scenario test - when you 'Stand', you get no new cards and score is evaluated
        hand = []
        game = Game()
        play = Player()
        game.opening_hand(hand)
        game.score(hand)
        play.turn(hand)
        self.assertEqual(len(hand), 2)

    def test_blackjack1(self):      # Scenario - King & Ace equate to 21 (Blackjack)
        player_hand = ['K', 'A']
        game = Game()
        total = game.score(player_hand)
        print(total)
        self.assertEqual(total, 21)

    def test_blackjack2(self):      # Scenario - King, Queen & Ace equate to 21 (Blackjack)
        player_hand = ['K', 'Q', 'A']
        game = Game()
        total = game.score(player_hand)
        print(total)
        self.assertEqual(total, 21)

    def test_blackjack2(self):      # Scenario - King, Queen & Ace equate to 21 (Blackjack)
        player_hand = ['9', 'A', 'A']
        game = Game()
        total = game.score(player_hand)
        self.assertEqual(total, 21)


if __name__ == '__main__':
    unittest.main()
