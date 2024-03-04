import codecs


f = codecs.open('input.txt', 'r', 'utf-8')
inp = f.read()
lines = inp.split('\n')

f = codecs.open('template', 'r', 'utf-8')
template = f.read()

output = open('output.txt', 'w')

names = []
texts = []

tmp = ''

for line in lines:
    tmp = ''
    sstr = line.replace('\r','')
    name = sstr[:sstr.find(' ')]
    text = sstr[sstr.find('--')+2:]
    #names.append(name)
    #texts.append(text)
    tmp = template.replace('UDO_F_XXX',name)
    tmp = tmp.replace('TEXT_XXX', text)
    tmp = tmp.replace('  ', ' ')
    tmp = tmp.replace('\r','')
    output.write('\n-------------------------------\n')
    output.write(tmp)
    print('grant execute on '+name+' to public;')
#print(names)
#print(texts)