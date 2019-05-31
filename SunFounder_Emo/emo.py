# Patch by Tomasz Bialas (2019)
# https://github.com/ledangaravi/slink/blob/master/SLINK/
# Forked by Raphaël Renaudon

class Alphabet(object):
    _normal = {
        'A': [
            '0110',
            '1001',
            '1001',
            '1111',
            '1001',
            '1001',
            '0000',],
        'B': [
            '1110',
            '1001',
            '1110',
            '1001',
            '1001',
            '1110',
            '0000',],
        'C': [
            '0110',
            '1001',
            '1000',
            '1000',
            '1001',
            '0110',
            '0000',],
        'D': [
            '1110',
            '1001',
            '1001',
            '1001',
            '1001',
            '1110',
            '0000',],
        'E': [
            '1111',
            '1000',
            '1110',
            '1000',
            '1000',
            '1111',
            '0000',],
        'F': [
            '1111',
            '1000',
            '1110',
            '1000',
            '1000',
            '1000',
            '0000',],
        'G': [
            '0110',
            '1001',
            '1000',
            '1011',
            '1001',
            '0110',
            '0000',],
        'H': [
            '1001',
            '1001',
            '1111',
            '1001',
            '1001',
            '1001',
            '0000',],
        'I': [
            '111',
            '010',
            '010',
            '010',
            '010',
            '111',
            '000',],
        'J': [
            '0001',
            '0001',
            '0001',
            '1001',
            '1001',
            '0110',
            '0000',],
        'K': [
            '1001',
            '1010',
            '1010',
            '1100',
            '1010',
            '1001',
            '0000',],
        'L': [
            '1000',
            '1000',
            '1000',
            '1000',
            '1000',
            '1111',
            '0000',],
        'M': [
            '10001',
            '11011',
            '10101',
            '10001',
            '10001',
            '10001',
            '00000',],
        'N': [
            '1001',
            '1001',
            '1101',
            '1011',
            '1001',
            '1001',
            '0000',],
        'O': [
            '0110',
            '1001',
            '1001',
            '1001',
            '1001',
            '0110',
            '0000',],
        'P': [
            '1110',
            '1001',
            '1001',
            '1110',
            '1000',
            '1000',
            '0000',],
        'Q': [
            '01110',
            '10001',
            '10001',
            '10001',
            '10101',
            '01110',
            '00001',],
        'R': [
            '1110',
            '1001',
            '1001',
            '1110',
            '1010',
            '1001',
            '0000',],
        'S': [
            '0110',
            '1001',
            '0100',
            '0010',
            '1001',
            '0110',
            '0000',],
        'T': [
            '11111',
            '00100',
            '00100',
            '00100',
            '00100',
            '00100',
            '00000',],
        'U': [
            '1001',
            '1001',
            '1001',
            '1001',
            '1001',
            '0110',
            '0000',],
        'V': [
            '1001',
            '1001',
            '1001',
            '1001',
            '1010',
            '0100',
            '0000',],
        'W': [
            '10001',
            '10001',
            '10001',
            '10101',
            '10101',
            '01010',
            '00000',],
        'X': [
            '1001',
            '1001',
            '0110',
            '1001',
            '1001',
            '1001',
            '0000',],
        'Y': [
            '10001',
            '10001',
            '01010',
            '00100',
            '00100',
            '00100',
            '00000',],
        'Z': [
            '1111',
            '0001',
            '0010',
            '0100',
            '1000',
            '1111',
            '0000',],
        'a': [
            '0111',
            '1001',
            '1001',
            '0111',
            '0000',],
        'b': [
            '1000',
            '1110',
            '1001',
            '1001',
            '1110',
            '0000',],
        'c': [
            '011',
            '100',
            '100',
            '011',
            '000',],
        'd': [
            '0001',
            '0111',
            '1001',
            '1001',
            '0111',
            '0000',],
        'e': [
            '0110',
            '1011',
            '1100',
            '0110',
            '0000',],
        'é': [
            '0110',
            '1011',
            '1100',
            '0110',
            '0000',],
        'f': [
            '001',
            '010',
            '111',
            '010',
            '010',
            '000',],
        'g': [
            '0111',
            '1001',
            '1001',
            '0111',
            '0001',
            '0110',],
        'h': [
            '1000',
            '1110',
            '1001',
            '1001',
            '1001',
            '0000',],
        'i': [
            '1',
            '0',
            '1',
            '1',
            '1',
            '0',],
        'j': [
            '01',
            '00',
            '01',
            '01',
            '01',
            '10',
            '00',],
        'k': [
            '1000',
            '1001',
            '1010',
            '1110',
            '1001',
            '0000',],
        'l': [
            '1',
            '1',
            '1',
            '1',
            '1',
            '0',],
        'm': [
            '11110',
            '10101',
            '10101',
            '10101',
            '00000',],
        'n': [
            '1110',
            '1001',
            '1001',
            '1001',
            '0000',],
        'o': [
            '0110',
            '1001',
            '1001',
            '0110',
            '0000',],
        'p': [
            '0110',
            '1001',
            '1001',
            '1110',
            '1000',],
        'q': [
            '0110',
            '1001',
            '1001',
            '0111',
            '0001',],
        'r': [
            '101',
            '110',
            '100',
            '100',
            '000',],
        's': [
            '0111',
            '1100',
            '0011',
            '1110',
            '0000',],
        't': [
            '010',
            '111',
            '010',
            '010',
            '001',
            '000',],
        'u': [
            '1001',
            '1001',
            '1001',
            '0111',
            '0000',],
        'v': [
            '1001',
            '1001',
            '1010',
            '0100',
            '0000',],
        'w': [
            '10101',
            '10101',
            '01010',
            '01010',
            '00000',],
        'x': [
            '101',
            '010',
            '010',
            '101',
            '000',],
        'y': [
            '1001',
            '1001',
            '0111',
            '0001',
            '0110',
            '0000',],
        'z': [
            '1111',
            '0010',
            '0100',
            '1111',
            '0000',],
        'ERROR_CHAR': [
            '1111',
            '1001',
            '1001',
            '1001',
            '1001',
            '1111',
            '0000',],
        ' ': [
            '00',
            '00',
            '00',
            '00',
            '00',],
        '!': [
            '1',
            '1',
            '1',
            '1',
            '0',
            '1',
            '0',],
        '?': [
            '110',
            '001',
            '010',
            '010',
            '000',
            '010',
            '000',],
        ',': [
            '01',
            '10',],
        '.': [
            '1',
            '0',],
        ':': [
            '1',
            '0',
            '0',
            '1',
            '0',
            '0',],
        ';': [
            '01',
            '00',
            '00',
            '01',
            '10',
            '00',],
        "'": [
            '1',
            '1',
            '0',
            '0',
            '0',
            '0',
            '0',],
        '"': [
            '101',
            '101',
            '000',
            '000',
            '000',
            '000',
            '000',],
        '(': [
            '01',
            '10',
            '10',
            '10',
            '10',
            '01',
            '00',],
        ')': [
            '10',
            '01',
            '01',
            '01',
            '01',
            '10',
            '00',],
        '`': [
            '10',
            '01',
            '00',
            '00',
            '00',
            '00',
            '00',],
        '°': [
            '1',
            '0',
            '0',
            '0',
            '0',
            '0',
            '0',],
        '1': [
            '010',
            '110',
            '010',
            '010',
            '010',
            '010',
            '000',],
        '0': [
            '010',
            '101',
            '101',
            '101',
            '101',
            '010',
            '000',],
        '2': [
            '110',
            '001',
            '010',
            '100',
            '100',
            '111',
            '000',],
        '3': [
            '110',
            '001',
            '110',
            '001',
            '001',
            '110',
            '000',],
        '4': [
            '101',
            '101',
            '111',
            '001',
            '001',
            '001',
            '000',],
        '5': [
            '111',
            '100',
            '110',
            '001',
            '001',
            '110',
            '000',],
        '6': [
            '011',
            '100',
            '111',
            '101',
            '101',
            '010',
            '000',],
        '7': [
            '110',
            '001',
            '001',
            '001',
            '001',
            '001',
            '000',],
        '8': [
            '010',
            '101',
            '010',
            '101',
            '101',
            '010',
            '000',],
        '9': [
            '010',
            '101',
            '111',
            '001',
            '001',
            '110',
            '000',],
        '|': [
            '010',
            '010',
            '010',
            '010',
            '010',
            '010',
            '000',],

        '/': [
            '0000001',
            '0000010',
            '0000100',
            '0001000',
            '0010000',
            '0100000',
            '1000000',],
    }
    all_on = [
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF,
        0xFF,0xFF,0xFF]


    def __init__(self):
        pass

    def normal(self, s):
        if s not in self._normal:
            s = 'ERROR_CHAR'
        return self._normal[s]

class Emotions(object):
    """docstring for emotions"""
    _emotions = {
        "blink1" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0',
            '0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0',
            '0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0',
            '0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0',
            '0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "blink2" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],

        "look1" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0',
            '0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "look2" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0',
            '0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "look3" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0',
            '0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "look4" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0',
            '0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],

        "sleepy1" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0',
            '0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "sleepy2" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0',
            '0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "sleepy3" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0',
            '0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "love" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
    }
    def __init__(self):
        pass

    def emotion(self, motion):
        try:
            return self._emotions[motion]
        except:
            return "This emotion not found"

class Pictures(object):
    """docstring for pictures"""
    _pictures = {
        "pac_man1" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0',
            '0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "pac_man2" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0',
            '0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],
        "pac_man3" : [
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',],

    }
    def __init__(self):
        pass

    def picture(self, pic):
        try:
            return self._pictures[pic]
        except:
            return "This picture not found"



class _Basic_class(object):
    import logging

    _class_name = '_Basic_class'
    _DEBUG = 'error'
    DEBUG_LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL,
              }
    DEBUG_NAMES = ['critical', 'error', 'warning', 'info', 'debug']

    def __init__(self):
        pass

    def logger_setup(self):
        self.logger = self.logging.getLogger(self._class_name)
        self.ch = self.logging.StreamHandler()
        form = "%(asctime)s [%(levelname)s] %(message)s"
        self.formatter = self.logging.Formatter(form)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)
        self._debug    = self.logger.debug
        self._info     = self.logger.info
        self._warning  = self.logger.warning
        self._error    = self.logger.error
        self._critical = self.logger.critical

    @property
    def DEBUG(self):
        return self._DEBUG

    @DEBUG.setter
    def DEBUG(self, debug):
        if debug in range(5):
            self._DEBUG = self.DEBUG_NAMES[debug]
        elif debug in self.DEBUG_NAMES:
            self._DEBUG = debug
        else:
            raise ValueError('Debug value must be 0(critical), 1(error), 2(warning), 3(info) or 4(debug), not \"{0}\".'.format(debug))  
        self.logger.setLevel(self.DEBUG_LEVELS[self._DEBUG])
        self.ch.setLevel(self.DEBUG_LEVELS[self._DEBUG])
        self._debug('Set logging level to [%s]' % self._DEBUG)

    def end(self):
        pass

class Emo(_Basic_class):
    import spidev
    import time

    OFF = [
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00]

    _start_signal = [0x01]
    _begin_data   = [0x02]

    _class_name = 'Emo'

    def __init__(self, ce=0):
        self.ce = ce
        self.logger_setup()
        self.spi = self.spidev.SpiDev()
        self.spi.open(0,ce)

        self.spi.max_speed_hz=800000 # REQUIRED to operate display
        self.alphabet = Alphabet()
        self.emotions = Emotions()
        self.pictures = Pictures()

    def show_bytes(self, _bytes):
        if not self.get_start():
            return False
        self.spi.writebytes(self._begin_data)  # If emo get 0x02, it begin to store the HEX data
        self.spi.writebytes(_bytes)
        return True

    def string_bits_to_bytes(self, _bits_list):
        _bytes = []
        if len(_bits_list) != 8:
            self._error("arguement should be list of 8 lines of strings")
        for _bits in _bits_list:
            _bits = _bits.replace(',', '').replace(' ', '')
            if len(_bits) != 24:
                self._error('every item in the list should be string with exact 24 "0" and "1" representing "off" and "on"')
            _byte0 = _bits[:8]
            _byte0 = int(_byte0, base=2)
            _bytes.append(_byte0)
            _byte1 = _bits[8:16]
            _byte1 = int(_byte1, base=2)
            _bytes.append(_byte1)
            _byte2 = _bits[16:]
            _byte2 = int(_byte2, base=2)
            _bytes.append(_byte2)
        return _bytes

    def string_to_string_bits(self, s):
        smap = []
        for i in range(8):
            bits = ''
            for letter in s:
                try:
                    bits += self.alphabet.normal(letter)[-i-1]
                except:
                    for j in range(len(self.alphabet.normal(letter)[0])):
                        bits += '0'
                bits += '0'
            smap.append(bits)
        smap.reverse()
        #print(smap)
        #print(len(smap[0]))
        return smap


    def string_to_bytes(self, s, pos=0):
        smap = self.string_to_string_bits(s)
        bits_list = []
        for i in range(8):
            temp = ''
            if pos <= 0:
                for j in range(-pos,24-pos):
                    try:
                        temp += smap[i][j]
                    except:
                        temp += '0'
            else:
            # add 0 at front
                for j in range(pos):
                    temp += '0'
                for j in range(24-pos):
                    try:
                        temp += smap[i][j]
                    except:
                        temp += '0'
            bits_list.append(temp)
        return self.string_bits_to_bytes(bits_list)

    def map_len(self, s):
        smap = self.string_to_string_bits(s)
        return len(smap[0])

    def off(self):
        #send_bytes(self.OFF)
        self.show_bytes(self.OFF)

    def show_string(self, s, pos=0):
        _bytes = self.string_to_bytes(s, pos)
        self.show_bytes(_bytes)

    def show_string_bits(self, bits):
        _bytes = self.string_bits_to_bytes(bits)
        self.show_bytes(_bytes)

    def show_emo(self, emo):
        if emo in self.emotions._emotions.keys():
            self.show_string_bits(self.emotions.emotion(emo))

        if emo in self.pictures._pictures.keys():
            self.show_string_bits(self.pictures.picture(emo))

    def get_start(self):
        count = 0
        #print("sending start")
        #print("starting signal is")
        #print(self._start_signal)
        while True:
            self.spi.writebytes(self._start_signal) # send start signel 0x01 and get respond
            a_status = self.spi.readbytes(1)
            #print("a_status:")
            #print(a_status)
            if (a_status == self._start_signal): # If emo get 0x01, and get start, it respond 0x01
                break;
            count = count + 1
            if (count>23): # emo not get start, and over time
                return False
            #if (True):
            #    break;
        return True

    @property
    def supported_character(self):
        self._supported_character = ''
        for key in self.alphabet._normal.keys():
            if key != 'ERROR_CHAR':
                self._supported_character += key
        return self._supported_character

    @property
    def supported_emotions(self):
        self._supported_emotions = ''
        for key in self.emotions._emotions.keys():
            self._supported_emotions += key
            self._supported_emotions += '  '
        return self._supported_emotions

    @property
    def supported_pictures(self):
        self._supported_pictures = ''
        for key in self.pictures._pictures.keys():
            self._supported_pictures += key
            self._supported_pictures += '  '
        return self._supported_pictures

    def print_supported(self):
        print ("supported character:\n  %s \n"%self.supported_character)
        print ("supported emotions:\n  %s \n"%self.supported_emotions)
        print ("supported pictures:\n  %s \n"%self.supported_pictures)

    def scroll_text(self, value):
        value = value + "        "
        value_len = self.map_len(value)
        for i in range(value_len):
            self.show_string(value, -i+24)
            self.time.sleep(0.035)



########################################################
# Added functions
#######################################################
    def show_progressbar(self, progress):
       # print("test")
        n_pixels = round(progress*24)
        line = ""
        for i in range(0, n_pixels):
            line = line + "1"
        for i in range(n_pixels, 24):
            line = line + "0"
        
        array = [line, line, line, line, line, line, line, line]
        databytes = self.string_bits_to_bytes(array)
        self.show_bytes(databytes)


    def show_progressbar_with_text(self, progress, text):
        textbits = self.string_to_string_bits(text)
        n_pixels = round(progress*24)

        line = ""
        for i in range(0, n_pixels):
            line = line + "1"
        for i in range(n_pixels, 24):
            line = line + "0"
        
        textbits[7] = line
        
        array = [textbits[1][:24], textbits[2][:24], textbits[3][:24], textbits[4][:24], textbits[5][:24], textbits[6][:24], textbits[0][:24], textbits[7][:24]]
        databytes = self.string_bits_to_bytes(array)
        self.show_bytes(databytes)

    def show_progressbar_on_text(self, progress, text):
        textbits = self.string_to_string_bits(text)
        n_pixels = int(progress*23)

        #print("BEGIN")
        #print(textbits)

        for i in range(len(textbits)):
            bitlist = list(textbits[i])
            #print(len(bitlist)) 
            for y in range(n_pixels):
                if (bitlist[y] == "1"):
                    bitlist[y] = "0"
                else:
                    bitlist[y] = "1"

            textbits[i] = ''.join(bitlist[:24])
        #print(textbits)

        databytes = self.string_bits_to_bytes(textbits)
        self.show_bytes(databytes)

