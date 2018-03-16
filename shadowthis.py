#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicode_spaces import unicode_spaces

ONE = unicode_spaces["ZERO WIDTH SPACE"]
ZERO = unicode_spaces["ZERO WIDTH NO-BREAK SPACE"]

def shadow(msg, userid):
    binary_id = bin(userid)[2:]
    secret = u""
    for i in binary_id:
        if i == '0':
            secret += ZERO
        else:
            secret += ONE

    output = msg.split()[0:1] + [secret] + msg.split()[1:]
    output = u" ".join(output)
    return output
  
def deshadow(msg):
    secret = msg.split()[1]
    secret = secret.replace(ONE, "1")
    secret = secret.replace(ZERO, "0")
    return int(secret, 2)


if __name__ == '__main__':
    encoded = shadow('ciao, come stai?', 9666)
    print(encoded)
    print(deshadow(encoded))
