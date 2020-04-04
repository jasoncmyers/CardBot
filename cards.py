import enum
import random

class Rank(enum.Enum):
    two = ('2', 2)
    three = ('3', 3)
    four = ('4', 4)
    five = ('5', 5)
    six = ('6', 6)
    seven = ('7', 7)
    eight = ('8', 8)
    nine = ('9', 9)
    ten = ('10', 10)
    jack = ('J', 11)
    queen = ('Q', 12)
    king = ('K', 13)
    ace = ('A', 14)
    joker = ('Joker', 99)

    def __str__(self):
        return self.value[0]

class Suit(enum.Enum):
    spades = '♠️'
    hearts = '♥️'
    diamonds = '♦️'
    clubs = '♣️'
    suitless = ''

    def __str__(self):
        return self.value

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + str(self.suit)

    def __repr__(self):
        return self.__str__()

    @property
    def card_name(self):
        if self.suit == Suit.suitless:
            return str(self.rank)
        return str(self.rank) + ' of ' + str(self.suit.name) 

class Deck():
    def __init__(self, deck_type='standard'):
        self.change_type(deck_type)

    def __str__(self):
        string = ''
        for card in self.cards:
            string += str(card) + '\n'
        return string

    @property
    def card_count(self):
        return len(self.cards)

    def add_jokers(self, num):
        for _ in range(num):
            self.cards.append(Card(Rank.joker, Suit.suitless))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num=1):
        hand = []
        if num > len(self.cards):
            return []
        for _ in range(num):
            card = self.cards.pop()
            hand.append(card)
        return hand


    def change_type(self, deck_type, num_jokers=0):
        self.cards = []

        if deck_type == 'euchre':
            self.type = 'euchre'
            for suit in (Suit.spades, Suit.hearts, Suit.diamonds, Suit.clubs):
                for rank in (Rank.nine, Rank.ten, Rank.jack, Rank.queen, Rank.king, Rank.ace):
                    self.cards.append(Card(rank, suit))
        elif deck_type == 'clubs' or deck_type == 'clubs3':
            self.type = 'clubs'
            for suit in (Suit.spades, Suit.hearts, Suit.diamonds, Suit.clubs):
                for rank in (Rank.ten, Rank.jack, Rank.queen, Rank.king, Rank.ace):
                    self.cards.append(Card(rank, suit))
        elif deck_type == 'clubs4':
            self.change_type('euchre')
            self.type = 'clubs4'
        elif deck_type == 'clubs5':
            self.type = 'clubs5'
            for suit in (Suit.spades, Suit.hearts, Suit.diamonds, Suit.clubs):
                for rank in (Rank.eight, Rank.nine, Rank.ten, Rank.jack, Rank.queen, Rank.king, Rank.ace):
                    self.cards.append(Card(rank, suit))
        elif deck_type == 'clubs6':
            self.type = 'clubs6'
            for suit in (Suit.spades, Suit.hearts, Suit.diamonds, Suit.clubs):
                for rank in (Rank.seven, Rank.eight, Rank.nine, Rank.ten, Rank.jack, Rank.queen, Rank.king, Rank.ace):
                    self.cards.append(Card(rank, suit))
        elif deck_type == 'pinochle':
            self.change_type('euchre')
            self.type = 'pinochle'
            self.cards *= 2
        else:
            self.type = 'standard'
            for suit in (Suit.spades, Suit.hearts, Suit.diamonds, Suit.clubs):
                for rank in (Rank.two, Rank.three, Rank.four, Rank.five, Rank.six, Rank.seven, Rank.eight, Rank.nine, Rank.ten, Rank.jack, Rank.queen, Rank.king, Rank.ace):
                    self.cards.append(Card(rank, suit))

        self.add_jokers(num_jokers)
        self.shuffle()




if __name__ == "__main__":
    #print (Rank.__members__)

    #c = Card(Rank.ace, Suit.clubs)
    #print(c)

    d = Deck('clubs')
    d.add_jokers(1)
    #for card in d.cards:
    #    print(card.card_name)
    print(d)
    print(d.card_count)
    print(d.type)
    test = d.deal(5)
    print(test)
    
    '''print(Suit.spades)
    print(Suit.spades.name)
    print(Rank.ace)
    print(Rank.ace.value)
    print(Suit)

    for s in Suit:
        print(s)
    
    for c in Rank[1:3]:
        print(c)'''