import time
import pygame
import numpy as np

from constants.morse_code_dict import MORSE_CODE_DICT

FREQUENCY = 700  # Hz
UNIT = 0.15      # seconds per Morse unit
SAMPLE_RATE = 44100

# Initialize pygame mixer
pygame.mixer.pre_init(SAMPLE_RATE, -16, 1, 512)
pygame.init()

def generate_tone(frequency, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # volume 50%
    wave_ints = np.int16(wave * 32767)
    sound = pygame.sndarray.make_sound(wave_ints)
    return sound

# Pre-generate dot and dash sounds
dot_sound = generate_tone(FREQUENCY, UNIT)
dash_sound = generate_tone(FREQUENCY, UNIT * 3)

def play_beep(duration_type):
    if duration_type == 'dot':
        dot_sound.play()
        time.sleep(UNIT)
    elif duration_type == 'dash':
        dash_sound.play()
        time.sleep(UNIT * 3)

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        morse_code.append(MORSE_CODE_DICT.get(char, ''))
    return ' '.join(morse_code)

def play_morse(morse_code):
    valid_symbols = {'.', '-', ' ', '/'}
    for symbol in morse_code:
        if symbol not in valid_symbols:
            continue
        if symbol == '.':
            play_beep('dot')
            time.sleep(UNIT)         # gap between parts of same letter
        elif symbol == '-':
            play_beep('dash')
            time.sleep(UNIT)
        elif symbol == ' ':
            time.sleep(UNIT * 3)    # gap between letters
        elif symbol == '/':
            time.sleep(UNIT * 7)    # gap between words