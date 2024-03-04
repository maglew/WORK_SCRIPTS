import codecs

f = codecs.open('text', 'r', 'utf-8')
text = f.read()


alllines = text.split("\n")



def attrexp():
    line = ""
    line = alllines[1].replace("(","")
    line = line.replace(")", "")
    attrs = line.split(", ")
    return attrs

def linesexp():
    lines=alllines[4:]

    return lines


attrs=attrexp()

for a in attrs:
    print(a)
print("--------------------------------------")
lines=linesexp()
#for a in lines:
#    print(a)

print("--------------------------------------")
print("длина атрибутов",len(attrs))

print("длина линий",len(lines))


print("--------------------------------------")
def pripis():
    listr=[]
    for i in range(len(lines)):
        if lines[i].find("--")==-1:
            bb=lines[i]
            #ss="--"+attrs[i]+"   \n"
            ss = "--" + attrs[i]
            aa=bb.replace("\r",ss+"")
            listr.append(aa)
        else:
            listr.append(lines[i])
        #print(i)
        print(listr[i])
pripis()
