"""
Copyright (C) 2021 Mayank Vats
See license.txt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License v3
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__author__ = "Mayank Vats"
__email__ = "testpass.py@gmail.com"
__Description__ = "Encrypt0r: A package to manage Encryption"
__version__ = "0.1a"


class Encrypt0r:

    def __init__(self, cipher):
        self.cipher = cipher
        self.supportedEncrypt0rs = []

    def encrypt(self, plain_text):
        if self.cipher.lower() == "reverse_cipher":
            cipher_text = plain_text[::-1]
            return cipher_text
        elif "substitution_cipher" in self.cipher.lower():
            #  ASCII Capital characters (A-Z) -> 65 - 90
            #  ASCII lowercase characters (a-z) -> 97 - 122
            # General substitution cipher, caesar's (shift value = 3) and ROT13(shift value = 13)
            # ciphers are special cases of this.

            try:
                n = int(self.cipher.split(":")[1])
            except IndexError as e:
                import warnings
                warnings.warn("You did not provide a shift value! Defaults to 13.")
                n = 13
            cipher_text = ""
            if 0 <= n <= 26:
                for i in plain_text:
                    new_pos = ord(i) + n
                    if i.isupper():
                        if new_pos <= 90:
                            cipher_text += chr(new_pos)
                        else:
                            overflow = new_pos - 90
                            cipher_text += chr(65 + overflow - 1)
                    elif i.islower():
                        if new_pos <= 122:
                            cipher_text += chr(new_pos)
                        else:
                            overflow = new_pos - 122
                            cipher_text += chr(97 + overflow - 1)
                    else:
                        raise TypeError("Only enter ASCII characters!")
            else:
                cipher_text = "Invalid shift value!"
            return cipher_text

        elif "columnar_transposition_cipher" in self.cipher.lower():
            cipher_text = ""
            try:
                n = int(self.cipher.split(":")[1])
            except IndexError as e:
                import warnings
                warnings.warn("You did not provide a row size! Defaults to 4.")
                n = 4
            plain_text = plain_text.replace(" ", "_")
            lst_plain = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
            if len(plain_text) % n != 0:
                for k in lst_plain:
                    if len(k) != n:
                        new_val = k + ("_" * (n - len(k)))
                        plain_text += "_" * (n - len(k))
                        lst_plain[lst_plain.index(k)] = new_val
            import numpy as np
            cipher_matrix = []
            for _ in lst_plain:
                cipher_matrix.append([ii for ii in _])
            cipher_matrix = np.array(cipher_matrix)
            for jj in range(0, n):
                cipher_text += "".join(cipher_matrix[:, jj].tolist())
            return cipher_text

    def decrypt(self, cipher_text):
        if self.cipher.lower() == "reverse_cipher":
            plain_text = cipher_text[::-1]
            return plain_text

        elif "substitution_cipher" in self.cipher.lower():
            plain_text = ""
            try:
                n = int(self.cipher.split(":")[1])
            except IndexError as e:
                import warnings
                warnings.warn("You did not provide a shift value! Defaults to 13.")
                n = 13
            for i in cipher_text:
                new_pos = ord(i) - n
                if i.isupper():
                    if new_pos >= 65:
                        plain_text += chr(new_pos)
                    else:
                        underflow = 65 - new_pos
                        plain_text += chr(90 - underflow + 1)
                elif i.islower():
                    if new_pos >= 97:
                        plain_text += chr(new_pos)
                    else:
                        underflow = 97 - new_pos
                        plain_text += chr(122 - underflow + 1)
                else:
                    print("Your text has some weird shit!")

            return plain_text

        elif "columnar_transposition_cipher" in self.cipher.lower():
            plain_text = ""
            try:
                n = int(self.cipher.split(":")[1])
            except IndexError as e:
                import warnings
                warnings.warn("You did not provide a row size! Defaults to 4.")
                n = 4
            JUMP_VALUE = int(len(cipher_text) / n)
            j = 0
            while len(plain_text) != len(cipher_text):
                for i in range(j, len(cipher_text), JUMP_VALUE):
                    plain_text += cipher_text[i]
                j += 1
            return plain_text.replace("_", " ").strip()
