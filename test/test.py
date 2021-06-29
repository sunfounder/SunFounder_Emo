import time
from SunFounder_Emo import Emo

lm = Emo()
lm.DEBUG = "debug"

def look_around():
    for x in range(1,3):
        lm.show_emo("look1")
        time.sleep(0.3)

        lm.show_emo("look2")
        time.sleep(0.3)

        lm.show_emo("look3")
        time.sleep(0.3)

        lm.show_emo("look4")
        time.sleep(0.3)

def sleepy():
    lm.show_emo("sleepy1")
    time.sleep(1)

    lm.show_emo("sleepy2")
    time.sleep(3)

    lm.show_emo("sleepy3")
    time.sleep(5)

def pac_man():
    lm.show_emo("pac_man1")
    time.sleep(0.8)

    lm.show_emo("pac_man2")
    time.sleep(0.8)

    lm.show_emo("pac_man3")
    time.sleep(0.8)

def supported():
    print ("supported character:\n  %s \n"%lm.supported_character)
    print ("supported emotions:\n  %s \n"%lm.supported_emotions)
    print ("supported pictures:\n  %s \n"%lm.supported_pictures)

if __name__ == '__main__':
    supported()
    try:
        while True:
            print("pac_man")
            pac_man()
            print("sleepy")
            sleepy()
            print("look_around")
            look_around()
    except KeyboardInterrupt:
        pass
