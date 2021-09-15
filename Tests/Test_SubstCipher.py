"""
Copyright (C) 2021 Mayank Vats
See license.txt
"""

from Encrypt0r import Encrypt0r

encrypt0r = Encrypt0r("Substitution_Cipher")

# If you do not provide a shift value, it defaults to 13
subst_cipher = encrypt0r.encrypt("Secret")
print("Substitution Cipher Encryption ->", subst_cipher)
dec_subst_cipher = encrypt0r.decrypt(subst_cipher)
print("Substitution Reverse Cipher Decryption ->", dec_subst_cipher)

# Providing custom shift value:
# !!Remember that a shift of 26 will just return the string itself.!!

encrypt0r = Encrypt0r("Substitution_Cipher")
subst_cipher = encrypt0r.encrypt("Secret", key=12)
print("Substitution Cipher Encryption (Custom Shift) ->", subst_cipher)
dec_subst_cipher = encrypt0r.decrypt(subst_cipher, key=12)
print("Substitution Reverse Cipher Decryption (Custom Shift) ->", dec_subst_cipher)
