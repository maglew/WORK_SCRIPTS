import codecs

f = codecs.open('text', 'r', 'utf-8')
file = f.read()

output = open('output', 'w')
#f = codecs.open('text2', 'r', 'utf-8')
#file2 = f.read()


lines = file.split("\r\n")

for i in range(len(lines)):
    if lines[i].find(" if not UDO_PKG_CONV$ppc$vars.ppc$loaded then") !=-1:
        lines[i]=lines[i].replace("if not UDO_PKG_CONV$ppc$vars.ppc$loaded then","/*if not UDO_PKG_CONV$ppc$vars.ppc$loaded then")
        lines[i+2]=lines[i+2].replace("end if;","end if;*/")
    output.write(lines[i]+"\n")



f.close()
output.close()