

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

output = open('output', 'w')

tmploop="sXXX => ooxml_util_pkg_n.get_xlsx_cell_value(bblob, sSHEETNAME,'aaa'||i),"
tmpinsert="sXXX=>sXXX,"
tmpline="sAAA => l_all_values(BBB),"

'''
def retLet(n):
    i = n // len(alphabet)
    if i == 0:
        return alphabet[n-1]
    elif i == 1:
        return "A"+alphabet[n-len(alphabet)*i-1]
    elif i == 2:
        return "B"+alphabet[n-len(alphabet)*i-1]
    elif i == 3:
        return "C"+alphabet[n-len(alphabet)*i-1]
    '''
def retLet(n):
    i = n // len(alphabet)
    if i == 0:
        return alphabet[n-1]
    elif i > 0:
        return alphabet[1]+""+alphabet[n-len(alphabet)*i-1]


def loopwrite():
    t=""
    for i in range(1,71):
        s=str(i)
        t = tmploop.replace("aaa", retLet(i))
        #t = tmploop
        if i < 10:
            t = t.replace("XXX", "0" + s)
        else:
            t = t.replace("XXX",  s)
        output.write(t + "\n")

def insertwrite():
    t=""
    for i in range(1,71):
        s=str(i)
        t=tmpinsert
        if i < 10:
            t = t.replace("XXX", "0" + s)
        else:
            t = t.replace("XXX",  s)
        output.write(t + "\n")


def tempwrite():
    t = ""
    for i in range(1, 71):
        s = str(i)
        t = tmpline.replace("BBB", s)
        # t = tmploop
        if i < 10:
            t = t.replace("AAA", "0" + s)
        else:
            t = t.replace("AAA", s)
        output.write(t + "\n")

#loopwrite()
tempwrite()
#insertwrite()
