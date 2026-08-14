space = 'i'

def encode(word: str):
    encoded = ''
    for letter in word:
        encoded += str(ord(letter)) + space
    return encoded

def decode(cypher: str):
    decoded = ''
    cypher: list = cypher.split(space)
    cypher.pop() # '' в конце
    for val in cypher:
        decoded += chr(int(val))
    return decoded