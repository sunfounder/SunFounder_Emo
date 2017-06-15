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

    def __init__(self):v
        
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

class LED_Matrix(_Basic_class):
    import spidev
    import maps

    OFF = [
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00,
        0x00, 0x00, 0x00]

    _class_name = 'LED_Matrix'

    def __init__(self, ce=0):
        self.ce = ce
        self.logger_setup()
        self.spi = self.spidev.SpiDev()
        self.spi.open(0,0)
        self.alphabet = self.maps.alphabet()

    def show_bytes(self, _bytes):
        self.spi.writebytes(_bytes)

    def off(self):
        send_bytes(self.OFF)

    def show_bits(self, _bits_list):
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
        self.show_bytes(_bytes)

    def string_to_map(self, s):
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
        #for i in smap:
        #    print i
        return smap

    def map_len(self, s):
        smap = self.string_to_map(s)
        return len(smap[0])

    def show_string(self, s, pos=0):
        bits_list = []
        smap = self.string_to_map(s)
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
        self.show_bits(bits_list)
        #for i in bits_list:
        #    print i
        return len(smap[0])

    @property
    def supported_character(self):
        self._supported_character = ''
        for key in self.alphabet._normal.keys():
            if key != 'ERROR_CHAR':
                self._supported_character += key
        return self._supported_character

'''
while True:
    send_bit_map(blink1)
    print("blink1")
    time.sleep(2)
    send_bit_map(blink2)
    print("blink2")
    time.sleep(0.1)
    send_bit_map(blink1)
    print("blink1")
    time.sleep(0.1)
    send_bit_map(blink2)
    print("blink2")
    time.sleep(0.1)
'''