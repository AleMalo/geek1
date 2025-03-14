import pygame.font

P1C1 = '#b687c9'
P1C2 = '#4bcbca'
P1C3 = '#353a4c'

P2C1 = '#f5abba'
P2C2 = '#f7799a'
P2C3 = '#90314b'

GC1 = '#414d3c'
GC2 = '#57838a'
GC3 = '#d0d0b6'

# #69E599, #246363, #4DABC7, #FFA2BD, #5B4E77

INFO = '''Your password should contain 15 characters with at least 1 in each category:
small letters, big letters, numbers, symbols'''

RULES = '''something
for
sure'''

FONT1 = ('Arial', 50, 'bold')
FONT2 = ('Arial', 35, 'bold')
FONT3 = ('Arial', 25)
FONT4 = ('Arial', 15)

def CHECK_WITH_RULES(password):
    if len(password) != 15:
        return False
    small, big, number, symbol = False, False, False, False
    for i in password:
        if 97 <= ord(i) <= 122:
            small = True
        elif 65 <= ord(i) <= 90:
            big = True
        elif 48 <= ord(i) <= 57:
            number = True
        elif 33 <= ord(i) <= 47 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 126:
            symbol = True
        if small and big and number and symbol:
            return True
    return False

print(CHECK_WITH_RULES('1234QWER!@#$qwe'))