from Encrypt0r import Enc0der

# URL un-safe encodings

supported_encoders = Enc0der("algo").supported_encoding
dummy_text = "Lorem ipsum dolor sit amet"
print("Supported encoders: ", supported_encoders, "\n")

for i in supported_encoders:
    print(f"Url-unsafe encoding {i} -> ", Enc0der(i).encode(dummy_text))

# URL safe encodings (Only availabe for b64)

print(f"\nUrl-safe encoding base64:b64 -> ", Enc0der("base64:b64").encode(dummy_text, url_safe=True), "\n")

# Decoding:

# Url-unsafe encoding base64:b16 ->  b'4C6F72656D20697073756D20646F6C6F722073697420616D6574'
# Url-unsafe encoding base64:b32 ->  b'JRXXEZLNEBUXA43VNUQGI33MN5ZCA43JOQQGC3LFOQ======'
# Url-unsafe encoding base64:b64 ->  b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQ='
# Url-unsafe encoding base64:b85 ->  b'OmA{!Z6IlIb9HSXWN&P5av*bQbRc1EWpn'

print(f"Decoding b16-> ", Enc0der("base64:b16").decode("4C6F72656D20697073756D20646F6C6F722073697420616D6574"))
print(f"Decoding b32-> ", Enc0der("base64:b32").decode("JRXXEZLNEBUXA43VNUQGI33MN5ZCA43JOQQGC3LFOQ======"))
print(f"Decoding b64-> ", Enc0der("base64:b64").decode("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQ="))
print(f"Decoding b85-> ", Enc0der("base64:b85").decode("OmA{!Z6IlIb9HSXWN&P5av*bQbRc1EWpn"))

# URL safe de-codings (Only availabe for b64)

print(f"\nUrl-safe decoding base64:b64 -> ", Enc0der("base64:b64").decode("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQ=",
                                                                          url_safe=True), "\n")
