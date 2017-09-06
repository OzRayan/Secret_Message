import csv
import os
from ciphers import Affine, Atbash, Keyword
# Read from a csv file the prompt
with open('promt.csv', newline='') as csvfile:
    t = csv.DictReader(csvfile, delimiter=',')
    txt = list(t)


def clear():
    """Clear the screen"""
    return os.system('cls' if os.name == 'nt' else 'clear')


def num_set(menu):
    """Sets to encrypt or decrypt"""
    if menu.lower() in ['encrypt', 'e']:
        return True
    if menu.lower() in ['decrypt', 'd']:
        return False


def choose_cipher(sub_menu, num):
    """Chooses the cipher encrypt or decrypt"""
    af = Affine()
    at = Atbash()
    kw = Keyword()
    if sub_menu.lower() in ['keyword', 'k']:
        clear()
        print(txt[0]['keyword_in'])
        text = input("Just alphabet characters: \n>").strip()
        print(txt[0]['key'])
        key = input("Just alphabet characters: \n>").strip()
        if num:
            print(txt[0]['encrypted'].format(kw.keyword(text, key, num)))
        else:
            print(txt[0]['decrypted'].format(kw.keyword(text, key, num)))
    if sub_menu.lower() in ['affine', 'a']:
        clear()
        print(txt[0]['message'])
        text = input("Just alphabet characters: \n>").strip()
        if num:
            print(txt[0]['encrypted'].format(af.affine(text, num)))
        else:
            print(txt[0]['decrypted'].format(af.affine(text, num)))
    if sub_menu.lower() in ['atbash', 'b']:
        clear()
        print(txt[0]['message'])
        text = input("Just alphabet characters: \n>").strip()
        if num:
            print(txt[0]['encrypted'].format(at.atbash(text, num)))
        else:
            print(txt[0]['decrypted'].format(at.atbash(text, num)))


def cipher(num):
    """Sub_menu loop"""
    while True:
        clear()
        print(txt[0]['cipher_menu'])
        sub_menu = input(txt[0]['cipher'])
        if sub_menu.lower() not in ['affine', 'atbash', 'keyword', 'a', 'b', 'k']:
            print(txt[0]['error'])
            continue
        if sub_menu.lower() in ["quit", 'q']:
            print("Bye! See You next time")
            break
        if sub_menu.lower() in ['affine', 'atbash', 'keyword', 'a', 'b', 'k']:
            choose_cipher(sub_menu, num)
            break


def command():
    """Menu loop"""
    while True:
        clear()
        print(txt[0]['welcome'])
        print(txt[0]['main_menu'])
        menu = input(txt[0]['action'])
        if menu.lower() in ["quit", 'q']:
            print("Bye! See You next time")
            break
        if menu.lower() not in ['encrypt', 'decrypt', 'e', 'd']:
            print(txt[0]['error'])
            continue
        elif menu.lower() in ['encrypt', 'decrypt', 'e', 'd']:
            num = num_set(menu)
            cipher(num)
            print(txt[0]['repeat'])
            y_n = input('> ')
            if y_n.lower() != 'n':
                continue
            else:
                print("Bye! See You next time")
                break
        else:
            raise print(ValueError)


if __name__ == '__main__':
    command()
    exit()
