import string
import time


def encrypt(plaintext, key, charlist=None, space=""):
    
    # input validation
    if not plaintext or type(plaintext) is not str:
        raise ValueError("Invalid plaintext")
    if not key or type(key) is not str:
        raise ValueError("Invalid key")
    if charlist and type(charlist) is not str:
        raise ValueError("Invalid charlist")
    if space:
        if type(space) is not str:
            raise ValueError("Invalid space char")
        if len(space) > 1:
            raise ValueError('Too many space chars')
    
    # if no valid charlist defined, choose default charlist (i.e. A-Z)
    if not charlist:
        charlist = string.ascii_uppercase
        # print("default charlist")
    
    # ensure that all chars are uppercase
    plaintext = plaintext.upper()
    key = key.upper()
    charlist = charlist.upper()
    space = space.upper()
        
    print("charlist: " + charlist + "\n")
    
    # replace spaces with space char or remove them
    if space:
        plaintext = plaintext.replace(" ", space)
        
    # ensure that all chars are in charlist
    invalid_plain_chars = set()
    for i in plaintext:
        if i not in charlist and i not in invalid_plain_chars:
            invalid_plain_chars.add(i)
            print("WARN: plaintext char '%s' is not in the charlist and will be removed" % i)
    for i in key:
        if i not in charlist:
            raise ValueError("Key char '%s' not in charlist" % i)
    if space and space not in charlist:
        raise ValueError('Space char not in charlist')
    
    # plaintext may only contain chars available in charlist
    plaintext = ''.join(filter(charlist.__contains__, plaintext))
    
    # encrypt
    ciphertext = ""
    for i, _char in enumerate(plaintext):
        char_shift = key[i % len(key)]
        index_shift = charlist.index(char_shift)
        
        index_plain = charlist.index(_char)
        index_cipher = (index_plain + index_shift) % len(charlist)
        ciphertext += charlist[index_cipher]
    
    return ciphertext


def decrypt(ciphertext, key, charlist=None, space=""):

    # input validation
    if not ciphertext or type(ciphertext) is not str:
        raise ValueError("Invalid plaintext")
    if not key or type(key) is not str:
        raise ValueError("Invalid key")
    if charlist and type(charlist) is not str:
        raise ValueError("Invalid charlist")
    if space:
        if type(space) is not str:
            raise ValueError("Invalid space char")
        if len(space) > 1:
            raise ValueError('Too many space chars')
    
    # if no valid charlist defined, choose default charlist (i.e. A-Z)
    if not charlist:
        charlist = string.ascii_uppercase
        # print("default charlist")
    
    # ensure that all chars are uppercase
    ciphertext = ciphertext.upper()
    key = key.upper()
    charlist = charlist.upper()
    space = space.upper()
        
    print("charlist: " + charlist + "\n")
    
    # decrypt
    plaintext = ""
    for i, _char in enumerate(ciphertext):
        char_shift = key[i % len(key)]
        index_shift = charlist.index(char_shift)
        
        index_cipher = charlist.index(_char)
        index_plain = (index_cipher - index_shift) % len(charlist)
        plaintext += charlist[index_plain]
    
    # replace space char with actual space
    if space:
        plaintext = plaintext.replace(space, " ")
        
    return plaintext
    

# example input: "a-z0-9öü-"
def get_charlist(_input):
    _input = _input.upper()
    
    charlist = ""
    for i in range(len(_input)):
        if _input[i:i+3] == "A-Z":
            _input = _input.replace("A-Z", "***")
            charlist += ''.join([a for a in string.ascii_uppercase if a not in charlist])
            
        elif _input[i:i+3] == "0-9":
            _input = _input.replace("0-9", "***")
            charlist += ''.join([a for a in string.digits if a not in charlist])
            
        elif _input[i] not in "* " and _input[i] not in charlist:
            charlist += _input[i]
    
    return charlist #  if len(charlist) > 0 else None
    
    
if __name__ == "__main__":
    msg = input("Plaintext: ")
    key = input("Key: ")
    charlist = get_charlist(input("Charlist (optional): "))
    space = input("Space char (optional): ")
    ciphermsg = encrypt(msg, key, charlist=charlist, space=space)
    print("Ciphertext:", ciphermsg)
    print("press enter to decrypt")
    input()
    
    msg = input("Ciphertext: ")
    key = input("Key: ")
    charlist = get_charlist(input("Charlist (optional): "))
    space = input("Space char (optional): ")
    print(decrypt(msg, key, charlist=charlist, space=space))
    
    