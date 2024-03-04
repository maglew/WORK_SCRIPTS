import codecs
'''
в файл attrlist записывать имена входных переменных, 
имена ячеек и линий там они расположены попорядку,
 группы разделены знаком --
после этого соберется простенький шаблон 

'''
f = codecs.open('maket', 'r', 'utf-8')
maket = f.read()

f = codecs.open('attrlist', 'r', 'utf-8')
attrlist = f.read()

output = open('output.txt', 'w')

nrazd=0

lines = maket.split("\r\n")
attrlines = attrlist.split("\r\n")

procname = attrlines[0]

inoutres=[]
cellatr=[]
linsatr=[]
atres=[]

def inotresImport():
    n=2
    for i in range(n,len(attrlines)):
        n = n + 1
        if attrlines[i] == "--cells":
            return n
        else:
            inoutres.append(attrlines[i])
    return n

n=inotresImport()

def cellsInsert(n):
    a=n
    for i in range(a,len(attrlines)):
        n = n + 1
        if attrlines[i] == "--lines":
            return n
        else:
            cellatr.append(attrlines[i])
    return n




n=cellsInsert(n)

def linesInsert(n):
    a = n
    for i in range(a, len(attrlines)):
        n = n + 1
        if attrlines[i] == "--attres":
            return n
        else:
            linsatr.append(attrlines[i])
    return n


n=linesInsert(n)

def atresInsert(n):
    for i in range(n, len(attrlines)):
        atres.append(attrlines[i])

atresInsert(n)


def printINS():
    for i in inoutres:
        if i[0]=="s" :
            output.write(i +" in varchar2, --\n")#
        elif i[0]=="d":
            output.write(i +" in date, --\n")#
        elif i[0]=="n"or i[0]=="b":
            output.write(i +" in number, --\n")#

def printCELLS():
    for i in cellatr:
        output.write("CELL_"+i +"       constant PKG_STD.tSTRING := '"+i+"';--\n")  #

def printLINES():
    for i in linsatr:
        output.write("LINE_"+i +"       constant PKG_STD.tSTRING := '"+i+"';--\n")  #

def printVARS():
    for i in cellatr:
        output.write("s"+i+"     PKG_STD.tSTRING := ' '; --\n")  #

    for i in atres:
        output.write("s"+i+"     PKG_STD.tSTRING := ' '; --\n")  #

def printDESCR():
    for i in cellatr:
        output.write("  PRSG_EXCEL.CELL_DESCRIBE(CELL_"+i+"); --\n")  #

def printDESCRLINE():
    for i in linsatr:
        output.write("  PRSG_EXCEL.LINE_DESCRIBE(LINE_"+i+"); --\n")  #


def printVARSZERO():
    for i in cellatr:
        output.write("      s"+i+":= ' '; --\n")  #

    for i in atres:
        output.write("      s"+i+":= ' '; --\n")  #

def print_VALUE_WRITE():
    for i in cellatr:
        output.write("      PRSG_EXCEL.CELL_VALUE_WRITE(CELL_" + i + ", s"+i+"); --\n")  #

def print_LINE_DEL_COND():
    for i in linsatr:
        output.write("  if  _COND_ then --\n")  #
        output.write("  PRSG_EXCEL.LINE_DELETE(LINE_" + i + "); --\n")  #
        output.write("  end if; --\n")  #

def print_LINE_DEL():
    for i in linsatr:
        output.write("  PRSG_EXCEL.LINE_DELETE(LINE_"+i+"); --\n")  #

def printSPECLOOP():
    output.write("          for rRECS in\n")  #
    output.write("          (\n")  # (
    output.write("          select\n")  # )
    output.write("          S.*\n")  # )
    output.write("          from\n")  # )
    output.write("          _TABBLENAME_ S\n")  # )
    output.write("          where\n")  # )
    output.write("          rREC.RN = S.PRN\n")  # )
    output.write("          )\n")  # )
    output.write("          loop\n")  # )
    output.write("\n")  #
    output.write("          end loop;\n")  #

def printmaket():
    output.write("create or replace procedure "+procname+"\n")
    output.write("(\n")#(
    printINS()
    output.write(")\n")#)
    output.write("as\n")#as
    output.write("LIST                    constant PKG_STD.tSTRING := 'Лист1';\n")#
    output.write("\n")  #
    printCELLS()
    output.write("\n")  #
    printLINES()
    output.write("\n")  #
    printVARS()
    output.write("\n")  #
    output.write("begin\n")  #
    output.write("  PRSG_EXCEL.PREPARE;\n")  #
    output.write("  PRSG_EXCEL.SHEET_SELECT( LIST );\n")  #
    printDESCR()
    output.write("\n")  #
    printDESCRLINE()
    output.write("\n")  #
    output.write("  for rREC in\n")  #
    output.write("  (\n")  # (
    output.write("  select\n")  # )
    output.write("  T.*\n")  # )
    output.write("  from\n")  # )
    output.write("  _TABBLENAME_ T\n")  # )
    output.write("  where\n")  # )
    output.write("  S.IDENT = nIDENT\n")  # )
    output.write("  and S.DOCUMENT = T.RN\n")  # )
    output.write("  )\n")  # )
    output.write("  loop\n")  # )
    printVARSZERO()
    output.write("\n")  #
    print_VALUE_WRITE()
    output.write("\n")  #
    printSPECLOOP()
    output.write("\n")  #
    print_LINE_DEL_COND()
    output.write("\n")  #
    output.write("  end loop;\n")  #
    output.write("end;")  #

printmaket()


f.close()
output.close()