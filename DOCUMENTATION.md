================
PROGRAM DOCUMENTATION
================

PROGRAM'S NAME: CIPHER ME
LANGUAGE      : PYTHON 3x
DEVELOPER     : YAFETH TANDI BENDON

================

A. What is this?
----------------
Short explanation: this is a SIMPLE message encryption program.
It's simple because it's based on caesar cipher, an oldest type encrypting algorithm.
But making someting too simple is simply boring, right?
So then I add some extra steps to make it interesting... hopefully.

B. How this stuff works?
----------------
This program will do these steps in order to encrypt your message:
1. Accept and read your text file input.
2. Accept your ciphering code input (five string characters) as shift factor. This program will process this input into int.
3. Processing all characters in your inputs into unicode codes and applying shift value according to the ciphering code you give.
4. Translate the output in point 3 back into unicode characters.
5. Send out an output file containing encrypted strings from point 4.

And here are the extra steps:
Each character in your ciphering code will be translated into unicode code numbers. All numbers then summed and floor divided with 2. The result will be the shift factor used in the function.

This program can also be used to decipher text made with this program. You just have to have the encrypted text and the ciphering code.

Hint: The code is appended in the result file name (output_code.txt).

C. What file(s) inside?
----------------
This program have two files:
1. main_code.py
This is the front face of the program. You'll interact with this program from this file.
2. cipher_codes.py
This file contain two functions: ciphering() and deciphering().
As the name implied, ciphering() contain all codes used to encrypt the text, and deciphering() contain all codes used to reverse the encrypt.

D. Input/Output
----------------
This program ONLY accept text file in .txt extension. 
This program will ONLY save the result in .txt extension too.

================
