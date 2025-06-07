def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'E':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    elif choice == 'D':
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted Message:", decrypted)
    else:
        print("Invalid choice. Please select E or D.")

if __name__ == "__main__":
    main()
