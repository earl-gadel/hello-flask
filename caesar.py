#
#
#


from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    final_encrypt = ""

    for char in text:
        final_encrypt = final_encrypt + rotate_character(char, rot)

    return final_encrypt

def main():
    message = input("Type a message:")
    rotate = int(input("Rotate by:"))
    print(encrypt(message, rotate))

if __name__ == "__main__":
    main()

