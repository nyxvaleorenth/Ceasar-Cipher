try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("The Ceasar cipher encrypts letters by shifting them over a")
print("key number. For example a key of 2 means the letter A is")
print("encrypted into C, the letter B encrypted into D, and so on.")
print()

# let the user enter if they are encrypting or decrypting:
# keep asking until they enter e or d.
while True:
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter the letter e or d.")


# let the user enter the key to use:
# keep asking until they enter a valid key
while True:
    maxKey = len(SYMBOLS) - 1
    print(f"Please enter the key (0 to {maxKey})")
    response = input("> ").upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) <= len(SYMBOLS):
        key = int(response)
        break

# let the user enter the message to encrypt/decrypt
print(f"Enter the message to {mode}")
message = input("> ")

# Ceaser cipher only works on uppercase letters:
message = message.upper()

# stores the encrypted/decrypted form of the message
translated = ""

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)  # get the number of the symbol
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key
        # handle the wrap around if num is larger than the length of
        # SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # add encrypted/decrypted number's symbol to translated:
        translated += SYMBOLS[num]

    else:
        # Just add the symbol without encrypting/decrypting
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f"Full {mode}ed text copied to clipboard")
except:
    pass
