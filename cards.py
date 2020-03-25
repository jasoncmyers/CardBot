import enum

class Rank(enum.Enum):
    two = ' 2'
    three = ' 3'
    four = ' 4'
    five = ' 5'
    six = ' 6'
    seven = ' 7'
    eight = ' 8'
    nine = ' 9'
    ten = '10'
    jack = ' J'
    queen = ' Q'
    king = ' K'
    ace = ' A'

    def __str__(self):
        return self.value

class Suit(enum.Enum):
    spades = '♠️'
    hearts = '♥️'
    diamonds = '♦️'
    clubs = '♣️'

    def __str__(self):
        return self.value

class deck():
    def __init__(self):
        self.deck_type = 'standard'

    pass


if __name__ == "__main__":
    print(Suit.spades)
    print(Suit.spades.name)
    print(Rank.ace)
    print(Rank.ace.value)
    print(Suit)