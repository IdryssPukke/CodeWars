"""https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python"""

import re

def validate_pin(pin):
    return True if re.search('^\d{4}\Z|^\d{6}\Z', pin) else False