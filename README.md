# Caesar Cipher
## Description
The Caesar Cipher program is a Python implementation of the classic encryption technique. It allows users to encode or decode messages by shifting the letters of the alphabet by a specified number of positions. This interactive program is simple to use and showcases fundamental concepts of cryptography.

---

## Features
* **Encode and Decode**: Encrypt messages or decrypt encoded text with ease.
* **Customizable Shift**: Users can specify any shift value for encoding or decoding.
* **Handles Non-Alphabet Characters**: Non-alphabetic characters (e.g., spaces, numbers, punctuation) are preserved without alteration.
* **Interactive and Repeatable**: The program allows multiple rounds of encoding or decoding in one session.

---

## Files Included
* `caesar_cipher.py`: The main script implementing the Caesar Cipher logic.
* `art.py`: Contains the ASCII art logo displayed at the start of the program.

---

## Prerequisites
* Python 3.x installed on your system.

---

## How to Run
1. Clone or download this repository to your local machine:
    ```shell
    git clone https://github.com/shrabhay/Caesar-Cipher.git
    cd caesar-cipher
    ```

2. Run the script:
    ```shell
    python3 caesar_cipher.py
    ```

---

## How to Use
1. Launch the program, and you'll see the Caesar Cipher logo.
2. Select an action:
   * Type `encode` to encrypt a message.
   * Type `decode` to decrypt an encoded message.
3. Enter your message.
4. Specify the shift number (the number of positions to shift the letters).
5. View the result of the encoding or decoding.
6. Decide whether to continue or exit the program.

---

## Example Usage
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here's the encoded result: mjqqt btwqi

Type 'yes' to go again. Otherwise type 'no':
no
Goodbye
```

---

## Future Enhancements
* Add support for uppercase letters without converting to lowercase.
* Allow for negative shifts directly in the user input.
* Implement an auto-decrypt mode to brute-force all possible shift values for deciphering unknown messages.
* Provide a GUI for easier interaction.

---

## License
This project is open-source and available under the MIT License.

---

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## Acknowledgments
This project was inspired by the classic Caesar Cipher encryption method, a fundamental concept in cryptography. Special thanks to the Python community for resources and support.
