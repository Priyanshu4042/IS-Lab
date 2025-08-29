from pycipher import Caesar, Vigenere, Playfair, Hill

def caesar_demo():
    text = input("Enter text (uppercase, no spaces): ").upper()
    key = int(input("Enter shift key (0-25): "))
    cipher = Caesar(key).encipher(text)
    print("Ciphertext:", cipher)
    print("Decrypted:", Caesar(key).decipher(cipher))

def vigenere_demo():
    text = input("Enter text (uppercase, no spaces): ").upper()
    key = input("Enter keyword: ").upper()
    cipher = Vigenere(key).encipher(text)
    print("Ciphertext:", cipher)
    print("Decrypted:", Vigenere(key).decipher(cipher))

def playfair_demo():
    text = input("Enter text (uppercase, no spaces): ").upper()
    key = input("Enter Playfair key: ").upper()
    cipher = Playfair(key).encipher(text)
    print("Ciphertext:", cipher)
    print("Decrypted:", Playfair(key).decipher(cipher))

def hill_demo():
    text = input("Enter text (uppercase, no spaces): ").upper()
    key = [[3,3],[2,7]]  # you can allow input if needed
    cipher = Hill(key).encipher(text)
    print("Ciphertext:", cipher)
    print("Decrypted:", Hill(key).decipher(cipher))

while True:
    print("\nChoose a cipher:")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Playfair Cipher")
    print("4. Hill Cipher")
    print("5. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        caesar_demo()
    elif choice == "2":
        vigenere_demo()
    elif choice == "3":
        playfair_demo()
    elif choice == "4":
        hill_demo()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
