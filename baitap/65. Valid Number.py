import re

class Solution:
    def isNumber(self, s):
        pattern = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$')
        return bool(pattern.match(s))