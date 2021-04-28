#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        char = None
    else:
        char = sentence[0]
    strtup = (len(sentence), char)
    return(strtup)
