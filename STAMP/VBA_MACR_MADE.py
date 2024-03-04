import codecs

f = codecs.open('input.txt', 'r', 'utf-8')
inp = f.read()
lines = inp.split('\r\n')

output = open('output.txt', 'w')

stmp = ''

for line in lines:
    #stmp = line.replace('')
    stmp = line.strip()
    if (stmp != ''):
        #print(stmp)
        output.write("SMACROS := SMACROS || '"+stmp+"' || CHR(13);\n")