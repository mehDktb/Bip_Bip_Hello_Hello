from constants.morse_code_dict import MORSE_CODE_DICT
def text_to_morse(text):
    text = text.upper()
    morse_code = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Unknown character

    return ' '.join(morse_code)