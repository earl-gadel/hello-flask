from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    rotated_list = ""
    encrypt_list = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha.upper()
    final_encrypt = ""
    m = len(rot)
    n = 0
    for i in range(len(text)):
        if text[i] == " ":
            n = n - 1
            final_encrypt = final_encrypt + " "

        elif text[i] not in alpha and text[i] not in alpha_upper:
            n = n - 1
            final_encrypt = final_encrypt + text[i]
        else:
            rotated_list = alphabet_position(rot[(i % m) + n])
            final_encrypt = final_encrypt + rotate_character(text[i], rotated_list)

    return final_encrypt

def main():
    print(encrypt("The crow flies!", "boom"))

if __name__ == "__main__":
    main()