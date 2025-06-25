from src.text_to_morse import text_to_morse
from src.morse_to_text import morse_to_text
from constants.bots import bot_1, bot_2
from src.initiate_conversation import initiate_conversation
from src.play_morse import play_morse

import argparse

def main(turns):
    last_speach = initiate_conversation()
    encoded_speach = text_to_morse(last_speach)
    # print("0000000000000")
    # print(last_speach)
    for turn in range (turns*2):
        if turn % 2:
            print("-------- chatbot 2 ---------------------")
            decoded_speach =  morse_to_text(encoded_speach)
            answer = bot_2.ask(decoded_speach)
            encoded_speach = text_to_morse(answer)
            print("said: " + encoded_speach)
            play_morse(encoded_speach)
            print("which means: " + answer)
        else:
            print("-------- chatbot 1 ---------------------")
            decoded_speach = morse_to_text(encoded_speach)
            answer = bot_1.ask(decoded_speach)
            encoded_speach = text_to_morse(answer)
            print("said: " + encoded_speach)
            play_morse(encoded_speach)
            print("which means: " + answer)

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run interactive bot conversation with Morse code.")
    parser.add_argument('--turns', type=int, default=3, help="Number of conversation turns")
    args = parser.parse_args()

    main(args.turns)