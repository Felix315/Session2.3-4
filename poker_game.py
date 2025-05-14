from deck import Deck, Card

class PokerHand:
    """
    A class representing a 5-card poker hand with methods to evaluate its type.
    """

    def __init__(self, deck):
        """
        Initialize a PokerHand by dealing 5 cards from the given deck.

        :param deck: An instance of the Deck class to deal cards from.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Get the list of cards in the hand.

        :return: A list of 5 Card objects.
        """
        return self._cards

    def __str__(self):
        """
        Return a string representation of the hand.

        :return: A string listing the 5 cards.
        """
        return str(self._cards)

    @property
    def is_flush(self):
        """
        Check if all cards in the hand share the same suit.

        :return: True if the hand is a flush, False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        Check if the hand is a full house (a three-of-a-kind and a pair).

        :return: True if full house, False otherwise.
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Count total matching pairs (including duplicates) in the hand.

        :return: An integer representing how many matches exist among ranks.
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Check if the hand has exactly one pair.

        :return: True if the hand has one pair, False otherwise.
        """
        if self.number_matches == 2: # simple
            return True
        return False

    @property
    def is_two_pair(self):
        """
        Check if the hand has exactly two pairs.

        :return: True if two pairs, False otherwise.
        """
        return self.number_matches == 4 # more advanced

    @property
    def is_trips(self):
        """
        Check if the hand has three cards of the same rank.

        :return: True if three-of-a-kind, False otherwise.
        """
        if self.number_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        """
        Check if the hand has four cards of the same rank.

        :return: True if four-of-a-kind, False otherwise.
        """
        if self.number_matches == 12:
            return True
        return False

    @property
    def is_straight(self):
        """
        Check if the hand is a straight (5 consecutive ranks).

        :return: True if straight, False otherwise.
        """
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4

# Simulation to estimate the probability of getting a straight
count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight:
        matches += 1
        print(hand)
    count += 1

print(f"probability of a full house is {100*matches/count}%")
