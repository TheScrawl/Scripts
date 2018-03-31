import time
import random as r

#Keys Should Look like [Seed-XXXXX-XXXXX-XXXXX-XXXXX]
arr00 = list("2EAMIN2D650IDL0V9H37")
arr01 = list("IKIJ9U488LLH44CBDY9M")
arr02 = list("M13E2Q4CHST49ULDWL2J")
arr03 = list("9T2H9RT175OZHL66YA4L")
arr04 = list("5V0HL3EIT3NZDF4CWJEY")
arr05 = list("FJMZPQIMC9CGXQUZ4A8H")
arr06 = list("TLUOJPLJXWW87YIQZBIE")
arr07 = list("ZCVNKXWW1OOKD8HCSC41")
arr08 = list("KCC3RPC2AF78FJJSL20D")
arr09 = list("4CDB4ELD7JSPXCPXIFPU")
arr10 = list("2OQYY662Z0Q6OA00NPVG")
arr11 = list("7M0F4MI5QO58BMF03LHK")
arr12 = list("C0O1UJ1I43WPP01DLKAT")
arr13 = list("62C8Q0V2J325WU01549F")
arr14 = list("WEM65A7TMW53JXI2CX9O")
arr15 = list("DSG2QU3C32RW279R6KPB")
arr16 = list("AP7VRA5JDT30NSBGJT2N")
arr17 = list("YMPSTTRD9JE919PQL4XU")
arr18 = list("7938L5YS2MUJ6NAE6RAC")
arr19 = list("JC5WUH5990CAG08HERP9")
farr = [arr00, arr01, arr02, arr03, arr04, arr05, arr06, arr07, arr08, arr09, arr10, arr11, arr12, arr13, arr14, arr15, arr16, arr17, arr18, arr09]

def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')
    base36 = ''
    sign = ''
    if number < 0:
        sign = '-'
        number = -number
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
    return sign + base36

def base36decode(number):
    return int(number, 36)

def gen(seed = "", debug = False):
    ms = lambda: int(round(time.time() * 1000))
    if (seed == ""):
        r.seed(ms())
        for i in range(5): seed += farr[r.randint(0, len(farr)-1)][r.randint(0, len(farr)-1)]
    r.seed(base36decode(seed))
    serial = seed
    while len(serial) < 29:
        if(len(serial) % 6 == 5):
            serial += "-"
        else:
            a = r.randint(0, len(farr)-1)
            b = abs(11 - (r.randint(1, 10) + 6))
            serial += farr[a][b]
            if(debug): print("Array: " + str(a) + " Offset: " + str(b) + " Letter:\t" + farr[a][b])
    return serial

print("\r\nLicence Key: " + gen(debug=True))
