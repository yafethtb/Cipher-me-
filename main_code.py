import cipher_codes as cc

#----INITIALIZE----#
'''
Initialize file names and shift value.
'''

plain = input("Enter file name:  ") + ".txt"

while True:
    shift = input("Enter shift code:   ")
    
    if ' ' in shift:
        # Checking if the code contain whitespace or not.
        print("No space or tab allowed in code.\n")
        continue
    elif len(shift) == 5:
        # All characters are turned into unicode number
        factor = sum([ord(chara) for chara in shift])//2
        # The numbers are summed and floor divided with 2
        break
    else:
        print("The code should be 5 characters and not include any space or tab.\n")

cipher = input("Enter output file name:   ") + "_" + shift + ".txt"

process_type = input("Choose one process type: encode or decode?   ").lower()


#----PROCESS----#
'''
Checking what process the user need.
'''

while True:
    if process_type == "encode":
        # Encoding process
        with open(plain, 'r') as enter, open(cipher, 'a+') as out:
            base_code = enter.readlines()
            for line in base_code:
                encode = cc.ciphering(line, factor)
                out.write(encode)
            print("Encoding finished.")
            break
    elif process_type == "decode":
        # Decoding process
        with open(plain, 'r') as enter, open(cipher, 'a+') as out:
            base_code = enter.readlines()
            for line in base_code:
                decode = cc.deciphering(line, factor)
                out.write(decode)
            print("Decoding finished.")
            break
    else:
        print("Please choose only encode or decode.\n")
            
            
        


