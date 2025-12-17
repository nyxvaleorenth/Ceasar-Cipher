# setup constants
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# get the mode
while True:
    print("chose what to do, (e)ncrypt or (d)ecrypt")
    response = input("> ").lower()

    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter e or d")

# get the key
# the key is between 0 and len(LETTERS)
while True:
    print("Enter the key")
    key = input("> ")

    if not key.isdecimal():
        print("Please enter a valid number")
        continue

    if 0 <= int(key) <= len(LETTERS):
        key = int(key)
