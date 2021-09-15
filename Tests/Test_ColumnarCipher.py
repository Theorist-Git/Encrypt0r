"""
Copyright (C) 2021 Mayank Vats
See license.txt
"""
from Encrypt0r import Encrypt0r

encrypt0r = Encrypt0r("Columnar_Transposition_Cipher")

# If you do not provide a shift value, it defaults to 4
column_cipher = encrypt0r.encrypt("My name is Mayank Vats")
print("Columnar substitution cipher (encryption) for block size 4 -> ", column_cipher)
print("Columnar substitution cipher (decryption) for block size 4 -> ", encrypt0r.decrypt(column_cipher), "\n")

# Providing custom shift value:
# It is recommended that you not choose a block size > len(plain_text)

encrypt0r = Encrypt0r("Columnar_Transposition_Cipher:6")
column_cipher = encrypt0r.encrypt("My name is The0rist")
print("Columnar substitution cipher (encryption) for block size 6 -> ", column_cipher)
print("Columnar substitution cipher (decryption) for block size 6 -> ", encrypt0r.decrypt(column_cipher))