import codecs

f = codecs.open('text', 'r', 'utf-8')
file = f.read()
lines = file.split("\r\n")

#first="if not UDO_PKG_CONV$ppc$vars.ppc$loaded then"
#second="/*if not UDO_PKG_CONV$ppc$vars.ppc$loaded then"

print(lines[0].replace(lines[0], "/*if not UDO_PKG_CONV$ppc$vars.ppc$loaded then"))