"""
Copyright (C) 2021 Mayank Vats
See license.txt
"""

from Encrypt0r import Encrypt0r

encrypt0r = Encrypt0r("XOR_cipher")
print("Encryption of a string using XOR: ", encrypt0r.encrypt("Mayank Vats"))
# {'Cipher': b'\xca\xb7"\xeb_\xce\x1bM\x9da\xf8', 'Key': b'\x87\xd6[\x8a1\xa5;\x1b\xfc\x15\x8b'}

# Now, the above comment is an example of what your output will look like
# Keep the key safe if you want to decrypt the Cipher text.  You can do so, like this:

print("Decryption of XOR cipher: ", encrypt0r.decrypt(b'\xca\xb7"\xeb_\xce\x1bM\x9da\xf8',
                                                      key=b'\x87\xd6[\x8a1\xa5;\x1b\xfc\x15\x8b').decode("utf-8"))
