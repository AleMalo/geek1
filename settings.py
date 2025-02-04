PLAYER1COLOR1 = '#aaaaaa'
PLAYER1COLOR2 = '#7f7f7f'
PLAYER1COLOR3 = '#555555'

# #69E599, #246363, #4DABC7, #FFA2BD, #5B4E77

INFO = '''Your password should contain at least 1 in each category:
small letters, big letters, numbers, symbols'''

FONT1 = ('Comic Sans MS', 30, 'bold')
FONT2 = ('Comic Sans MS', 15)

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