import time
from SunFounder_Emo import Emo

lm = Emo()

print("Words you can use:\n %s" % lm.supported_character)
value = 'Hello from SunFounder!'
value_len = lm.map_len(value)
for i in range(value_len):
    lm.show_string(value, -i+10)
    time.sleep(0.1)