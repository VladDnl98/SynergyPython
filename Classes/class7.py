t = 'abzr'

for c in t:
    code = ord(c)+3
    if code > 122:
        print(chr(97 + code - 122), end = '')
    else:
        print(chr(code), end = '')