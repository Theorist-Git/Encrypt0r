"""
Copyright (C) 2021 Mayank Vats
See license.txt
"""
from Encrypt0r import Encrypt0r

encrypt0r = Encrypt0r("Reverse_Cipher")

rev_cipher = encrypt0r.encrypt("Secret")
print("Reverse Cipher Encryption ->", rev_cipher)
dec_rev_cipher = encrypt0r.decrypt(rev_cipher)
print("Reverse Cipher Decryption ->", dec_rev_cipher)
