import random
oldLen = len
oldBytes = bytes
def tostring(num):
    if num:
        return str(num)
def tonumber(string):
    if string:
        return int(string)
class math:
    def random(a, b):
        return random.randint(a, b)
class string:
    def split(a, b):
        return a.split(b)
    def upper(a):
        return a.upper()
    def lower(a):
        return a.lower()
    def reverse(a):
        return a [::-1]
    def len(a):
        return len(a)
    def gsub(a, b, c):
        return a.replace(b, c)
    def byte(a):
        return bytes(a, 'utf-8')
