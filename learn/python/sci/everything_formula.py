import re
import time
import decimal
from math import floor

# this default is the number that plots the own formula
DEFAULT_N = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605626529915320311182856118951164066401426579727262440270286409619368825536815027849325692956320299303330714849102058741137034502
def everything_formula_f(x, y):
    xd = decimal.Decimal(x)
    yd = decimal.Decimal(y)
    arg = floor(yd/decimal.Decimal(17)) * decimal.Decimal(2)**(decimal.Decimal(-17)*xd - (yd %decimal.Decimal(17)))
    return floor((decimal.Decimal(arg) % decimal.Decimal(2)))

def falt(x, y):
    arg = (y//17) >> (17*x + (y % 17))
    return arg % 2
    #return ~arg & 0

# as seen in http://mathspp.blogspot.com/2019/04/the-formula-that-plots-itself.html
def everything_formula():
    start = time.time()
    # set the precision so that the decimal module can handle the calculations
    decimal.getcontext().prec = 1000
    n = DEFAULT_N
    rows = []
    # create a <table> object, row by row
    # assign the css color class by checking the everything_formula_f value
    for row in range(16, -1, -1):
        row_str = "<tr>\n\t"
        for col in range(106):
            clas = "black" if falt(col, row+n) > 0.5 else "white"
            row_str += "<td class='{}' />".format(clas)
        row_str += "</tr>"
        rows.append(row_str)
    return (time.time()-start)*1000

if __name__ == '__main__':
    r = []
    for i in range(100000):
        r.append(everything_formula())
    print(r) # Print times array
