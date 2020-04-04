from cards import Deck

class CardBot():
    
    def __init__(self, send_func=None):
        self.deck = Deck()
        if send_func is not None:
            self.send_func = send_func
        else:
            self.send_func = print


    def handle_input(self, in_string, player_name=None):
        if len(in_string) == 0 or in_string[0] != '!': 
            return
        else:
            split_in = in_string.lower().split(' ')
            command = split_in[0][1:]
            if command == 'help':
                print(self.help_list())
            elif command == 'deal':
                print('Dealing cards')
            elif command == 'deck':
                print('Chaning deck type')
            elif command == 'shuffle':
                print('Shuffling the deck')
                bot.shuffle()
            elif command == 'roll' or command == 'dice':
                print('Placeholder for rolling!')
            elif len(command.split('d')) == 2:
                print('Using ?d? format')
                t = command.split('d')
                print(t[0], t[1])
                if not(t[0].isdigit() and t[1].isdigit):
                    print('but they weren\'t digits!')
                    return
                print('Rolling', t[0], 'of', t[1], 'sided dice')

    def roll_dice(self, number, sides=6):
        pass

    def help_list(self):
        text = ('Use the following options:\n'
        '!help - show this list\n'
        '!deal <number> - deals <number> cards to each player\n' 
        '!shuffle - collect all cards and shuffle the deck\n'
        '!deck <decktype> - change the deck to <decktype>.  Options for types are:\n'
        '\tstandard, euchre, clubs, clubs4, pinochle\n'
        '!roll <number> <sides> - roll <number> <sides>-sided dice\n'
        '\t(also works with !4d6 format)\n')

        return text
        







def main():
    bot = CardBot()
    print(bot.help_list())
    quit_bot = False
    while not quit_bot:
        text = input('>')
        if text.lower() == 'quit':
            quit_bot = True
        bot.handle_input(text)


if __name__ == "__main__":
    main()