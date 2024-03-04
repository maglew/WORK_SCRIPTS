import codecs

f = codecs.open('input', 'r', 'utf-8')
inp = f.read()

output = open('output', 'w')

tables = ['GEOGRAFY','MSUACC','MSUBOOK','MSUHABI','MSULAND','MSUMEMBADDR','MSUHABICH','MSULANDCH','MSUOUTSRCINFH']


for tab in tables:
    tmp=inp



inp.replace('_TABLENAME_','')
inp.replace('_ITERATOR_','')
inp.replace('_CATNAME_','')
inp.replace('_DOCNAME_','')

#_TABLENAME_
#_ITERATOR_
#_CATNAME_
#_DOCNAME_
#

lines = inp.split("\r\n")