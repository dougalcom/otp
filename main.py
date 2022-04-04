import random
charTable = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", ",", "!", "?")
encodedString = ""
decodedString = ""
keyString = ""
quitFlag = False

def enSubstitute(stringy):
    stringy = stringy.replace(" ", "@")
    stringy = stringy.replace(".", "%")
    stringy = stringy.replace(",", "#")
    return stringy

def deSubstitute(stringy):
    stringy = stringy.replace("@", " ")
    stringy = stringy.replace("%", ".")
    stringy = stringy.replace("#", ",")
    return stringy

print("-- otp 1.21 --")

while (quitFlag == False):
    # inputs
    inputMode = input("\n[E]ncrypt, [D]ecrypt?, [G]enerate Keys, [H]elp, or [Q]uit -> ").upper()

    if inputMode == "Q":
        quitFlag = True

    elif inputMode == "E":
        print("[E]ncrypt mode active.")
        inputString = input("Input clear message -> ").upper()
        inputKeyOption = input("[G]enerate a random key, or [P]rovide one? -> ").upper()
        if inputKeyOption == "G":
            for char in inputString:
                randChar = charTable[random.randrange(len(charTable))]
                keyString = keyString + randChar
        elif inputKeyOption == "P":
            keyString = input("          Input key -> ").upper()
        else:
            print("Error: Invalid response.")
        posi = 0
        inputStringLen = len(inputString)
        keyStringLen = len(keyString)
        if keyStringLen >= inputStringLen:
            for char in inputString:
                try:
                    charCode = charTable.index(char)
                except:
                    print("Error: The clear message contains an unrecognized character.")
                    charCode = 0
                try:
                    keyStringCode = charTable.index(keyString[posi])
                except:
                    print("Error: The key contains an invalid character.")
                    keyStringCode = 0
                resultCharCode = charCode + keyStringCode
                if (resultCharCode > 27):
                    resultCharCode = resultCharCode - len(charTable)
                encodedString = encodedString + charTable[resultCharCode]
                posi = posi + 1
            encodedString = enSubstitute(encodedString)
            keyString = enSubstitute(keyString)
            print("Encrypted message: " + encodedString)
            if inputKeyOption == "G":
                print("              Key: " + keyString)
        else:
            print("Error: The key is too short.")

    elif inputMode == "D":
        print("[D]ecrypt mode active.")
        inputString = input("Input encrypted message -> ").upper()
        inputString = deSubstitute(inputString)
        keyString = input("              Input key -> ").upper()
        keyString = deSubstitute(keyString)
        posi = 0
        inputStringLen = len(inputString)
        keyStringLen = len(keyString)
        if keyStringLen >= inputStringLen:
            for char in inputString:
                try:
                    charCode = charTable.index(char)
                except:
                    print("Error: The encrypted message contains an unrecognized character.")
                    charCode = 0
                try:
                    keyStringCode = charTable.index(keyString[posi])
                except:
                    print("Error: The key contains an invalid character.")
                    keyStringCode = 0
                resultCharCode = int(charCode) - int(keyStringCode)
                if (resultCharCode < 0):
                    resultCharCode = resultCharCode + len(charTable)
                decodedString = decodedString + charTable[resultCharCode]
                posi = posi + 1
            print("Decoded message: " + decodedString)
        else:
            print("Error: The key is too short.")

    elif inputMode == "H":
        print("[H]elp mode active.")
        print("This software will encrypt or decrypt a text message.\nThis software utilizes an encryption technique that, if used properly, cannot be cracked.\n   Use Guide:\n - The message and the key may only contain letters, numbers, spaces, periods, exclaimation marks, and question marks.\n - The key must be at least as long as the message.\n - If you don't have a key, the program will generate a random key.\n - The message will be converted to upper case.\n - Never transmit keys by the same method as the encrypted message.\n - Destroy key promptly after decoding.\n - Never re-use a key.")

    elif inputMode == "G":
        print("[G]enerate Keys mode active.")
        numKeysInput = int(input("Number of keys to create? -> "))
        keysLenInput = int(input("      Length of each key? -> "))
        posi = 1
        genKey = ""
        while(posi <= numKeysInput):
            charIndex = 0
            while(charIndex <= keysLenInput):
                randChar = charTable[random.randrange(len(charTable))]
                genKey = genKey + randChar
                charIndex = charIndex + 1
            print(str(posi) + ": " + enSubstitute(str(genKey)))
            posi = posi + 1
            genKey = ""

    else:
        print("Unrecognized command.")

    encodedString = ""
    decodedString = ""
    keyString = ""

print("\n-- Program terminated --")
