import codecs

import xml.etree.ElementTree as ET

f = codecs.open('input', 'r', 'utf-8')
output = open('output.txt', 'w')
inp = f.read()
#lines = inp.split('\n')

inp = inp.replace('\n','')
inp = inp.replace('\r','')

root = ET.fromstring(inp)

attrs = []

#output.write("sdads")
'''
for child in root:
    #print('Element:', child.tag)
    #print('Text:', child.tail)
    output.write(str(child.tail)+'.'+str(child.tag)+'\n')
'''

#output = open('output.txt', 'w')

def gettags(prn,tag):
    for child in tag:
        couple = str(prn) + '.' + str(child.tag)
        if (attrs.count(couple)==0):
            attrs.append(couple)
            #output.write(couple+'\n')
            gettags(child.tag,child)



gettags('root',root)

#print(attrs.count('root.Datas'))


for attr in attrs:
    output.write('XML_'+str(attr[attr.find('.')+1:]) + '    VARCHAR2(4000),\n')

