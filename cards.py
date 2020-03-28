import enum

class Rank(enum.Enum):
    two = (' 2', 2)
    three = (' 3', 3)
    four = (' 4', 4)
    five = (' 5', 5)
    six = (' 6', 6)
    seven = (' 7', 7)
    eight = (' 8', 8)
    nine = (' 9', 9)
    ten = ('10', 10)
    jack = (' J', 11)
    queen = (' Q', 12)
    king = (' K', 13)
    ace = (' A', 14)
    joker = ('Joker', 99)

    def __str__(self):
        return self.value[0]

class Suit(enum.Enum):
    spades = '♠️'
    hearts = '♥️'
    diamonds = '♦️'
    clubs = '♣️'

    def __str__(self):
        return self.value

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + str(self.suit)

class deck():
    def __init__(self):
        self.deck_type = 'standard'

    pass


if __name__ == "__main__":
    #print (Rank.__members__)

    c = Card(Rank.ace, Suit.clubs)
    print(c)
    
    '''print(Suit.spades)
    print(Suit.spades.name)
    print(Rank.ace)
    print(Rank.ace.value)
    print(Suit)

    for s in Suit:
        print(s)
    
    for c in Rank[1:3]:
        print(c)'''