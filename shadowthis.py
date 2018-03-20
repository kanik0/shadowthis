#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_spaces import unicode_spaces
from re import sub

ONE = unicode_spaces["ZERO WIDTH SPACE"]
ZERO = unicode_spaces["ZERO WIDTH NO-BREAK SPACE"]

def shadow(msg, userid):                                      # Inserts an hidden userid after
    binary_id = bin(userid)[2:]                               # the first word in a string
    secret = u""
    for i in binary_id:
        if i == '0':
            secret += ZERO
        else:
            secret += ONE

    splitted = msg.split()
    num_spaces = len(splitted) - 1
    if num_spaces > 0:                                        # Standard case, msg contains more
        bits_per_space = 1 + len(binary_id) // num_spaces     # than one word
        if bits_per_space == 0:
            bits_per_space = 1
        output = []
        index = 0

        for word in splitted:
            if index<len(secret):
                    output += [word] + [" "] + [secret[index:index + bits_per_space]]
                    index += bits_per_space
            else:
                    output += [word] + [" "]

        output = u"".join(output)
    else:                                                     # Case where msg contains only one word
        output = msg + secret
    return output
  
def deshadow(msg):                                            # Gets the hidden userid back
    secret = sub(r"[^\u200B\uFEFF]+", "", msg)                # from a previously encoded message

    secret = secret.replace(ONE, "1")
    secret = secret.replace(ZERO, "0")
    return int(secret, 2)


if __name__ == '__main__':
    encoded = shadow("Hello, hope everything is going great overthere!", 9666)    # Example: hides the code '9666'
    print(encoded)                                                                # into a string and gets the code
    print(deshadow(encoded))                                                      # back from the encoded string
