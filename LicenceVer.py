import random as r
import re
arr00 = list("2EAMIN2D650IDL0V9H37")
arr01 = list("IKIJ9U488LLH44CBDY9M")
arr02 = list("M13E2Q4CHST49ULDWL2J")
arr03 = list("9T2H9RT175OZHL66YA4L")
arr04 = list("5V0HL3EIT3NZDF4CWJEY")
farr = [arr00, arr01, arr02, arr03, arr04, [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


def base36decode(number):
    return int(number, 36)

def ver(key, debug = True):
    seed = key[0:5]
    r.seed(base36decode(seed))
    serial = seed
    while len(serial) < 29:
        if(len(serial) % 6 == 5):
            serial += "-"
        else:
            a = r.randint(0, len(farr)-1)
            b = abs(11 - (r.randint(1, 10) + 6))
            try:
                serial += farr[a][b]
                if(debug): print("Array: " + str(a) + " Offset: " + str(b) + " Letter:\t" + farr[a][b])
            except IndexError:
                serial += "."
                if(debug): print("Array: " + str(a) + " Offset: " + str(b) + " Letter:\t.")
    if(debug): print("\r\n" + serial)
    if (re.match(serial, key)):
        return True
    else:
        return False

key = raw_input("Key to Test: ")
print(ver(key, debug=True))
