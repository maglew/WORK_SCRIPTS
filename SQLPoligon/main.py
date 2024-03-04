import codecs

f = codecs.open('text', 'r', 'utf-8')
text = f.read()

#f = open('text','r')
#text=f.read();
#print()
#print(f)
alllines = text.split("\n")



def attrexp():
    line=""
    line=alllines[1]
    #print(line)
    attrs=line.split(", ")
    return attrs

def linesexp():
    lines=alllines[2:]

    return lines

lines=linesexp()

attrs=attrexp()

def pripis():
    listr=[]
    for i in range(len(lines)):
        if lines[i].find("--")==-1:
            bb=lines[i]
            ss = "--" + attrs[i]
            aa=bb.replace("\r",ss+"")
            listr.append(aa)
        else:
            listr.append(lines[i])
        print(listr[i])
pripis()
