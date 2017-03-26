#!/usr/bin/env python

import vobject

NAMES = [i.strip() for i in open('names.txt', 'r', 'utf-8').readlines()]
NUMBERS = [i.strip() for i in open('numbers.txt', 'r', 'utf-8').readlines()]

def main():
    for i in range(len(NAMES)):
        vcard = vobject.vCard()

        o = vcard.add('n')
        o.value = vobject.vcard.Name(NAMES[i])

        o = vcard.add('fn')
        o.value = NAMES[i]

        for number in NUMBERS[i].split('.'):
            o = vcard.add('tel')
            if number.startswith('2'):
                o.type_param = 'home'
            else:
                o.type_param = 'cell'
            o.value = number

        print(vcard.serialize())


if __name__  == '__main__':
    main()
