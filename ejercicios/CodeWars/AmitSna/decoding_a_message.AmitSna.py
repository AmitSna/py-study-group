decode = lambda message: "".join([chr(abs(ord(letter) - 219)) if 91 <= ord(letter) <= 122 else letter for letter in list(message)])

def decode(message):
    decoded = ""
    for letter in message:
        if 91 <= ord(letter) <= 122:
            decoded += chr(abs(ord(letter) - 219))
        else:
            decoded += letter
    return decoded
