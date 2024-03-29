"""
Copyright (C) 2021-2022 Mayank Vats
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


class Encrypt0r:

    def __init__(self, cipher):
        self.cipher = cipher
        self.supportedEncrypt0rs = [
            "reverse_cipher",
            "substitution_cipher",
            "columnar_transposition_cipher",
            "XOR_cipher"
        ]

    def encrypt(self, plain_text, key=None):
        if self.cipher.lower() == "reverse_cipher":
            cipher_text = plain_text[::-1]
            return cipher_text
        elif "substitution_cipher" in self.cipher.lower():
            """
            ASCII Capital characters (A-Z) -> 65 - 90
            ASCII lowercase characters (a-z) -> 97 - 122
            General substitution cipher, caesar's cipher(shift value = 3) and ROT13(shift value = 13)
            ciphers are special cases of this.
            """

            if key:
                n = key
            else:
                import warnings
                warnings.warn("You did not provide a shift value! Defaults to 13.")
                n = 13
            cipher_text = ""
            if 0 <= n <= 26:
                for i in plain_text:
                    # For EG: ord('A') = 65, its new position will be 65 + n[specified shift]
                    new_pos = ord(i) + n

                    # Generating cipher for capital letters
                    if i.isupper():
                        if new_pos <= 90:  # if new_pos <= 90, chr(new_pos) gives its corresponding cipher alphabet.
                            cipher_text += chr(new_pos)
                        else:
                            """
                            Say if new_pos is 91 i.e A is to be encoded with a shift value of 26,
                            chr(91) corresponds to '[', but we want a character ∈ [65-90].
                            In this case an overflow is generated which is added to 65 and 1 is subtracted from it.
                            i.e new_pos = 91 is equivalent to going to 90 and then looping back to 65.
                            """
                            overflow = new_pos - 90
                            cipher_text += chr(65 + overflow - 1)

                    # Generating cipher for lowercase letters
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
            if key:
                n = key
            else:
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

        elif self.cipher.lower() == "xor_cipher":
            def keygen(length: int) -> bytes:
                from os import urandom
                return urandom(length)

            if key:
                if not isinstance(key, bytes):
                    KEY = key.encode("utf-8")
                else:
                    KEY = key
            else:
                KEY = keygen(len(plain_text))
            if not isinstance(plain_text, bytes):
                plain_text = plain_text.encode("utf-8")
            if len(plain_text) == 1:
                return {"Cipher": "".join(chr(i ^ j) for i, j in zip(plain_text, KEY)),
                        "Key": KEY}
            else:
                # Python 3 bytes objects contain integer values in the range 0-255
                return {"Cipher": bytes([a ^ b for a, b in zip(plain_text, KEY)]),
                        "Key": KEY}

        elif self.cipher.lower() == "vigenere_cipher":
            cipher_text = ""
            from string import ascii_uppercase as ascii_up
            from secrets import SystemRandom
            header = [j for j in ascii_up]
            cipher_table = [ascii_up[i:] + ascii_up[:i] for i in range(len(ascii_up))]
            VIGENERE_TABLEAU = dict(zip(header, cipher_table))
            DEFAULT_KEY_LENGTH = 6

            if key:
                if len(key) <= len(plain_text):
                    KEY = key.upper()
                else:
                    KEY = key[:len(plain_text)].upper()
                    import warnings
                    warnings.warn(f"You provided a key of length > len(plain_text).\nKey has been truncated: {KEY}")
            else:
                KEY = ''.join(SystemRandom().choice(ascii_up) for _ in range(DEFAULT_KEY_LENGTH))
            it = 0
            while len(plain_text) != len(KEY):
                if it == 0 or len(KEY) - 1 / it != 1.0:
                    KEY += KEY[it]
                    it += 1
                else:
                    it = 0
                    KEY += KEY[it]
                    it += 1
            CIPHER_KEY_TABLEAU = list(zip(plain_text, KEY))
            index = 0
            for k in plain_text:
                if k.isalpha():
                    if k.isupper():
                        cipher_text += VIGENERE_TABLEAU[CIPHER_KEY_TABLEAU[index][1]][ascii_up.index(k.upper())]
                        index += 1
                    else:
                        cipher_text += VIGENERE_TABLEAU[CIPHER_KEY_TABLEAU[index][1]][ascii_up.index(k.upper())].lower()
                        index += 1
                else:
                    cipher_text += k
            return {"Cipher": cipher_text, "Key": KEY}

    def decrypt(self, cipher_text, key=None):
        if self.cipher.lower() == "reverse_cipher":
            plain_text = cipher_text[::-1]
            return plain_text

        elif "substitution_cipher" in self.cipher.lower():
            plain_text = ""
            if key:
                n = key
            else:
                import warnings
                warnings.warn("You did not provide a shift value! Defaults to 13.")
                n = 13
            for i in cipher_text:
                new_pos = ord(i) - n
                if i.isupper():
                    if new_pos >= 65:
                        plain_text += chr(new_pos)
                    else:
                        """
                        Say the new_pos is 64 but we want a character ∈ [65-90].
                        In this case an underflow is generated which is subtracted from 90
                        i.e new_pos = 64 is equivalent to going to 65 and then looping back to 90.
                        """
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
            if key:
                n = key
            else:
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

        elif self.cipher.lower() == "xor_cipher":
            return self.encrypt(cipher_text, key=key)["Cipher"]

        elif self.cipher.lower() == "vigenere_cipher":
            plain_text = ""
            from string import ascii_uppercase as ascii_up
            from secrets import SystemRandom
            header = [j for j in ascii_up]
            cipher_table = [ascii_up[i:] + ascii_up[:i] for i in range(len(ascii_up))]
            VIGENERE_TABLEAU = dict(zip(header, cipher_table))
            if key:
                KEY = key
            else:
                raise TypeError("Key cannot be 'None' for Vignere's Cipher Decryption")
            it = 0
            while len(cipher_text) != len(KEY):
                if it == 0 or len(KEY) - 1 / it != 1.0:
                    KEY += KEY[it]
                    it += 1
                else:
                    it = 0
                    KEY += KEY[it]
                    it += 1
            CIPHER_KEY_TABLEAU = list(zip(cipher_text, KEY))
            index = 0
            for k in cipher_text:
                if k.isalpha():
                    if k.isupper():
                        plain_text += ascii_up[VIGENERE_TABLEAU[CIPHER_KEY_TABLEAU[index][1]].index(k.upper())]
                        index += 1
                    else:
                        plain_text += ascii_up[VIGENERE_TABLEAU[CIPHER_KEY_TABLEAU[index][1]].index(k.upper())].lower()
                        index += 1
                else:
                    plain_text += k
            return plain_text


class Enc0der:

    def __init__(self, encoding):
        self.encoding = encoding
        self.supported_encoding = [
            "base64:b16",
            "base64:b32",
            "base64:b64",
            "base64:b85"
        ]

    def encode(self, plain_text, url_safe: bool = False) -> bytes:
        if "base64" in self.encoding.lower():
            algo = self.encoding.split(":")[1] + "encode"
            plain_text = plain_text.encode("utf-8")
            import importlib
            if url_safe:
                if algo == "b64encode":
                    from base64 import urlsafe_b64encode
                    return urlsafe_b64encode(plain_text)
                else:
                    raise TypeError("URL_SAFE encoding is only available for base64:b64")
            else:
                package = importlib.__import__("base64", fromlist=self.supported_encoding)
                encoder = getattr(package, algo)
                return encoder(plain_text)
        else:
            raise TypeError(f"No such encoding available\nSee supported encodings:\n{self.supported_encoding}")

    def decode(self, encoded_text, url_safe: bool = False) -> bytes:
        if "base64" in self.encoding.lower():
            algo = self.encoding.split(":")[1] + "decode"
            encoded_text = encoded_text.encode("utf-8")
            import importlib
            if url_safe:
                if algo == "b64decode":
                    from base64 import urlsafe_b64decode
                    return urlsafe_b64decode(encoded_text)
                else:
                    raise TypeError("URL_SAFE decoding is only available for base64:b64")
            else:
                package = importlib.__import__("base64", fromlist=self.supported_encoding)
                decoder = getattr(package, algo)
                return decoder(encoded_text)
        else:
            raise TypeError(f"No such decoding available\nSee supported de-codings:\n{self.supported_encoding}")
