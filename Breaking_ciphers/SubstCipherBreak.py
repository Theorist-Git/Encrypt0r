# Brute fore attack on subst. cipher

def brute(cipher):
    for i in range(1, 27):
        plain_text = ""
        for j in cipher:
            new_pos = ord(j) - i
            if j.isupper():
                if new_pos >= 65:
                    plain_text += chr(new_pos)
                else:
                    underflow = 65 - new_pos
                    plain_text += chr(90 - underflow + 1)
            elif j.islower():
                if new_pos >= 97:
                    plain_text += chr(new_pos)
                else:
                    underflow = 97 - new_pos
                    plain_text += chr(122 - underflow + 1)
            else:
                print("Your text has some weird shit!")

        print("Shift value #", i, ": ", plain_text)


if __name__ == '__main__':
    cipher_input = input("Enter cipher text: ")
    print("Initiating brute force attack...")
    brute(cipher_input)
