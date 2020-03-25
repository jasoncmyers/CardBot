import cards

def main():
    input_text = ''
    while(input_text != 'QUIT'):
        input_text = input()
        print('echo:', input_text)

    return True

def process_text(input_text):
    if input_text[0] == '!':
        print('Entered command:', input_text[1,:])
    return



if __name__ == "__main__":
    main()