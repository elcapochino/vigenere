import string
import time


charlist = string.ascii_uppercase

class CryptModes:
    encrypt = 1
    decrypt = 2


def crypt(text_source, key, mode, charlist=None, space=None):

    # input validation
    # note: if not [string] checks for empty string
    if not text_source or type(text_source) is not str:
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
    
    # replace spaces with space char if encrypting
    if mode == CryptModes.encrypt:
        text_source = text_source.replace(" ", space if space else '')

    # ensure that all chars are in charlist
    invalid_chars = set()
    for char_ in text_source:
        if char_ not in charlist and char_ not in invalid_chars:
            invalid_chars.add(char_)
            print(f"WARNING: text char '{char_}' is not in the charlist and will be removed")
    for char_ in key:
        if char_ not in charlist:
            raise ValueError(f"Key char '{char_}' not in charlist")
    if space and space not in charlist:
        raise ValueError('Space char not in charlist')
    
    # text may only contain chars available in charlist
    text_source = ''.join(filter(charlist.__contains__, text_source))
    

    # actual encryption/decryption
    text_result = ""
    for i, char_source in enumerate(text_source):
        char_key = key[i % len(key)]
        index_key = charlist.index(char_key)
        
        index_source = charlist.index(char_source)
        
        if mode == CryptModes.encrypt:
            index_result = (index_source + index_key) % len(charlist)
        elif mode == CryptModes.decrypt:
            index_result = (index_source - index_key) % len(charlist)
        else:
            raise ValueError("Invalid crypt mode")
            
        text_result += charlist[index_result]
    
    
    # replace space chars with spaces if decrypting
    if space and mode == CryptModes.decrypt:
        text_result = text_result.replace(space, ' ')
        
    return text_result
        

def get_charlist(input_):
    REPLACE = {
        "A-Z": string.ascii_uppercase,
        "a-z": string.ascii_lowercase,
        "0-9": string.digits
    }

    # input_ = input_.upper()
    
    charlist = ""
    i = 0
    while i < len(input_):
        # scan if there are any REPLACE keys starting from index i
        for j in range(i+1, len(input_)+1):
            key = input_[i:j]
            if key in REPLACE:
                charlist += ''.join([a for a in REPLACE[key] if a not in charlist])
                i += len(key)
                break
        # if no REPLACE keys found, add single char
        else:
            charlist += input_[i] if input_[i] not in charlist else ''
            i += 1
            
    return charlist
    

if __name__ == "__main__":
    msg = input("Text: ")
    key = input("Key: ")
    charlist = get_charlist(input("Charlist (optional): "))
    space = input("Space char (optional): ")
    mode_input = input("(1) encrypt   (2) decrypt     : ")
    mode = CryptModes.encrypt if mode_input == "1" else CryptModes.decrypt
    
    print(crypt(msg, key, mode, charlist=charlist, space=space))

    