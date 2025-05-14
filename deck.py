import random

class Card:
    """
    A class representing a playing card with a suit and a rank.
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, suit, rank):
        """
        Initialize a Card object with a suit and rank.

        :param suit: One of the four card suits (♣, ♦, ♥, ♠).
        :param rank: One of the valid ranks ("2" through "A").
        :raises ValueError: If the suit or rank is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Compare two cards for equality based on their rank.

        :param other: Another Card object.
        :return: True if ranks are equal.
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compare two cards to determine which has the higher rank.

        :param other: Another Card object.
        :return: True if this card's rank is greater than the other's.
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Return a string representation of the card.

        :return: A string like 'K♠' or '10♥'.
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Return an official string representation of the card.

        :return: Same as __str__.
        """
        return self.__str__()

    @property
    def suit(self):
        """
        Get the suit of the card.

        :return: The card's suit.
        """
        return self._suit

    @property
    def rank(self):
        """
        Get the rank of the card.

        :return: The card's rank.
        """
        return self._rank

class Deck:
    """
    A class representing a full deck of 52 playing cards.
    """

    def __init__(self):
        """
        Initialize a new deck containing 52 unique cards.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        Return a string representation of the deck.

        :return: A string listing all cards in the deck.
        """
        return str(self._deck)

    def shuffle(self):
        """
        Shuffle the cards in the deck randomly.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deal (remove and return) the top card from the deck.

        :return: A Card object.
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
