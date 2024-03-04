import codecs

f = codecs.open('input', 'r', 'utf-8')
inp = f.read()
lines = inp.split('\n')
tags = []
tag = ''
sout = ''

output = open('output', 'w')

line = ''



for l in lines:
    #if (l.find('</') != -1):
    #    tag = l[l.index('</')+2:-2]
    #elif (l.find('/>') != -1):
    #    tag = l[1:-1]
    ##print(tag)

    #tags.append(tag.replace('/>',''))
    ##print("--"+tag)
    ##print("rNODE_CODE   := PKG_XPATH.SINGLE_NODE(rNODE_ROW,'"+tag+"');")
    ##print("s"+tag+" := PKG_XPATH.VALUE(rNODE_CODE);")
    #tag = tag.replace('/>','')
    tag = l.replace('\r','')
    output.write("--"+tag +"\n")  #
    output.write("rNODE_CODE   := PKG_XPATH.SINGLE_NODE(rNODE_ROW,'"+tag+"');" + "\n")
    output.write("RNODE_CODE :=PKG_XPATH.SINGLE_NODE(RNODE_CODE, 'PRN_NUMBER');" + "\n")
    output.write("FIND_ACCOUNT_BY_NUMBER(nCOMPANY, PKG_XPATH.VALUE(rNODE_CODE),nPRN_NUMBER);" + "\n")
    output.write("RNODE_CODE :=PKG_XPATH.SINGLE_NODE(RNODE_CODE, 'ANL_LEVEL');" + "\n")
    output.write("nANL_LEVEL := PKG_XPATH.VALUE(rNODE_CODE);" + "\n")
    output.write("RNODE_CODE :=PKG_XPATH.SINGLE_NODE(RNODE_CODE, 'ANL_NUMBER');" + "\n")
    output.write("FIND_ANALYTIC_BY_CODE(0,1,nPRN_NUMBER,nANL_LEVEL,PKG_XPATH.VALUE(RNODE_CODE), rSLOPERRULES."+tag+");" + "\n")


    #output.write("FIND_ACCOUNT_BY_NUMBER(nCOMPANY, PKG_XPATH.VALUE(rNODE_CODE),"+tag+");" + "\n")


    ##output.write("s" + tag + "      PKG_STD.tSTRING;" + "\n")  #



'''
for l in lines:
    line = l.replace('\r','')
    line = line.replace(' ', '')
    output.write('     '+line+'       => rSLOPERRULES.'+line[1:]+', --'+'\n')

    #output.write('     '+line+'       => null, --'+'\n')



for l in lines:
    line = l.replace('\r','')
    output.write('  rSLOPERRULES.'+line[1:]+' := coalesce( rSLOPERRULES.'+line[1:]+', 000) --\n')


for l in lines:
    line = l.replace('\r','')
    #output.write('FIND_NNN_CODE(0,1,nCOMPANY,PKG_XPATH.VALUE(RNODE_CODE), rSLOPERRULES.'+line+'); --\n')

    output.write('FIND_NNN_CODE(0,1,nACCNUMBER_'+line[-2:]+','+line[-1:]+',PKG_XPATH.VALUE(RNODE_CODE), rSLOPERRULES.' + line + '); --\n')

'''


