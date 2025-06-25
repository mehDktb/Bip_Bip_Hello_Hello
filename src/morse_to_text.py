from constants.morse_code_dict import REVERSED_MORSE_DICT
def morse_to_text(morse_code: str) -> str:
    words = morse_code.strip().split(' / ')  # Split into words
    decoded_message = []

    for word in words:
        letters = word.split()
        decoded_word = ''
        for symbol in letters:
            decoded_letter = REVERSED_MORSE_DICT.get(symbol, '?')
            decoded_word += decoded_letter
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)