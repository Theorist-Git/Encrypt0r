from Encrypt0r import Encrypt0r

# If you do not provide a key for encryption,
# A random 6-Letter key will be generated, 6-letters
# Imply 26^6 (308915776) possible keys.

encrypt0r = Encrypt0r("Vigenere_Cipher")
print("Encrypted: ", encrypt0r.encrypt("testpass.py@gmail.com"))

# Encrypted:  {'Cipher': 'gmcviofa.za@zanqv.eha', 'Key': 'NIKCTONIKCTONIKCTONIK'}

# Now, the above comment is an example of what your encrypted output will look like
# Keep the key safe if you want to decrypt the Cipher text.  You can do so, like this:

print("Decrypted: ", encrypt0r.decrypt('gmcviofa.za@zanqv.eha', key='NIKCTONIKCTONIKCTONIK'))
# Decrypted:  testpass.py@gmail.com

# You can also provide your own key:
# NOTE: Please provide a key whose length is <= the length of your plain_text
# If not, the key will be truncated, the key can only have as many possible
# combinations as the plain_text.

# Providing Longer key:

print("Encryption with truncated key", encrypt0r.encrypt("Theorist", key="QWERTYUIOP"))  # Will raise a WARNING
# Encrypted {'Cipher': 'cwcrgi', 'Key': 'QWERTYUI'}

print("Encryption with provided key", encrypt0r.encrypt("Theorist", key="QWERTYUI"))
