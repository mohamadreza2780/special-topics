
def caesar_cipher(text, key, mode):
    result = ""

    key = key % 26

    if mode == "decode":
        key = -key

    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result += new_char

        elif char.islower():
            new_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result += new_char

        else:
            result += char

    return result


print("===== Caesar Cipher =====")

text = input("Enter your text: ")
key = int(input("Enter the key (K): "))
mode = input("Choose operation (encode/decode): ").strip().lower()

if mode == "encode" or mode == "decode":
    result = caesar_cipher(text, key, mode)
    print("Result:", result)

else:
    print("Error: Invalid operation!")
