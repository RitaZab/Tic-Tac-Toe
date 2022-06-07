morse_code = {' ': '_', "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-',
              '/': '-..-.', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...','8': '---..', '9': '----.', ':': '---...', ';': '-.-.-.', '?': '..--..',
              'A': '.-', 'B': '-...', 'C': '-.-.','D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '_': '..--.-'}

again=True

def con_to_morse(given_text):
    '''Converting function from text to morse code'''
    morse_text=[]
    for symbol in given_text:
        morse_text.append(morse_code[symbol])
    return " ".join(morse_text)

def play_again():
    global again
    global translate_again
    translate_again = input("Do you want to translate more text? Type Y or N ").lower()
    if translate_again == "y":
        again = True
    elif translate_again == "n":
        again = False
    else:
        print("Wrong input.You need to type Y or N...")
        translate_again = input("Do you want to translate more text? Type Y or N ").lower()



while again:
    given_text = input("Type text you want to translate (use only symbols from latin alphabet):\n").upper()
    morse=con_to_morse(given_text)
    print(morse)
    play_again()

