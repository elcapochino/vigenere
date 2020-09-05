import string
import time

def crypt():
    text_result = ""
    for i, _char in enumerate(text_source):
        char_shift = key[i % len(key)]
        index_shift = charlist.index(char_shift)
        
        index_source = charlist.index(_char)
        index_result = (index_source + index_shift) % len(charlist)
        text_result += charlist[index_result]
    