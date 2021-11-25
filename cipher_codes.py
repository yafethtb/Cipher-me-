from string import whitespace as space

def ciphering(text, step):
''' Shifting characters to the right '''
    ciphertext = ''   
    for i in text:
        if i in space:
            ciphertext += i
        else:
            ciphertext += chr((ord(i) + step - 32) % 94 + 32)
    return ciphertext

def deciphering(text, step):
''' Shifting character to the left '''
    plaintext = ''
    for i in text:
        if i in space:
            plaintext += i
        else:
            plaintext += chr((ord(i) - step - 32) % 94 + 32)
    return plaintext
