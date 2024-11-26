"""
This program emulates the classic Caesar Cipher.
"""

import os
from art import logo

ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
             "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(input_text, shift_amount, shift_direction):
    cipher_text = ''
    shift_amount %= 26

    if shift_direction == 'decode':
        shift_amount *= -1

    for char in input_text:
        if char in ALPHABETS:
            cipher_text += ALPHABETS[ALPHABETS.index(char) + shift_amount]
        else:
            cipher_text += char

    return cipher_text


cipher_on = True
while cipher_on:
    os.system("clear")
    print(logo)

    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))

    print(f"Here's the {user_choice}d result: {caesar_cipher(input_text=user_text, shift_amount=user_shift, shift_direction=user_choice)}")

    to_continue = input("Type 'yes' to go again. Otherwise type 'no'.\n").lower()
    if to_continue == 'no':
        cipher_on = False
        print("Goodbye")
