import codecs

f = codecs.open('table.txt', 'r', 'utf-8')
table = f.read()

f = codecs.open('templateIMP.txt', 'r', 'utf-8')
imprt = f.read()

f = codecs.open('templateEXP.txt', 'r', 'utf-8')
exprt = f.read()

attrlist=[]

def cleartable():
    lines = table.split("\n")
    k=lines[1]
    tablename = k[k.find("table") + 6:-1]
    for i in lines:

        if i.find("/*")==-1 \
                and i.find("(")!=0  \
                and i.find("create")==-1 \
                and i.find(");")==-1 \
                and i.find("constraint")==-1 \
                and i.find("_")!=-1:
            attrlist.append(i[0:i.find(" ")])
    print("-----------------------------------------")
    print("tabble: ", tablename)
    print("num of attrs: ",len(attrlist))
    print("num of blocks: " , (len(attrlist)/3))
    print("-----------------------------------------")
    for j in attrlist:
        print(j)
    print("-----------------------------------------")
    return tablename

tableName = cleartable()


def printEXP(nodename,dopel):
    itername = tableName[-3:-1]
    #tmp=lp.replace("_TABLENAME_", tablename)
    print("")
    print("rNODE_%s := PKG_XMAKE.CONCAT(iCURSOR, rNODE_%s, PKG_XMAKE.ELEMENT(iCURSOR, '%s',"%(nodename,nodename,nodename))
    n=0#для подсчета количества атрибутов в конце
    for i in attrlist:
        if i.find("_YEAR") != -1 and i[-1]!="4" and i[-1]!="3" and i[-1]!="2":
            fulatr=i
            fulatr1=i.replace("_YEAR", "_1YEAR")
            fulatr2=i.replace("_YEAR", "_2YEAR")
            tmp = exprt.replace("_ITERATOR_", itername)
            tmp = tmp.replace("_CUTATR_", fulatr[0:-5])
            tmp = tmp.replace("_FULATR_", fulatr)
            tmp = tmp.replace("_FULATR1_", fulatr1)
            tmp = tmp.replace("_FULATR2_", fulatr2)
            print(tmp)
        elif i[-1]=="4":
            fulatr = i
            fulatr1 = i.replace("_4", "_3")
            fulatr2 = i.replace("_4", "_2")
            tmp = exprt.replace("_ITERATOR_", itername)
            tmp = tmp.replace("_CUTATR_", fulatr[0:-3])
            tmp = tmp.replace("_FULATR_", fulatr)
            tmp = tmp.replace("_FULATR1_", fulatr1)
            tmp = tmp.replace("_FULATR2_", fulatr2)
            print(tmp)
    if dopel>0:
        for i in range (len(dopel)):
            print("rNODE_%s_DOP%d,));"%(nodename,i))#будет лишняя запятая
        print("\n));")
    elif dopel==0:
        print("));")
    elif dopel==-1:
        print("));")

def printIMP(nodename,dop):# dop=-1 это мастер без допов, dop=0 это мастер с 1 допом, dop>0 это мастер с несколькими допами
    itername =tableName[-3:-1]
    if dop>0:
        print("--допов несколько")

    elif dop==0:
        for i in attrlist:
            attrs=[]
            isp=i.split("_")
            n=len(isp)

    elif dop==-1:
        #parentable=""
        tmp = imprt.replace("_TABLENAME_", tableName)
        tmp = tmp.replace("_BLOCKNAME_", nodename)
        tmp = tmp.replace("_FULLBLOCKNAME_", nodename)
        #tmp = tmp.replace("_FULLBLOCKNAME_", nodename+"ALL/"+nodename)#for not dop
        #tmp = tmp.replace("_PARENTABLE_", parentable)
        tmp = tmp.replace("_ITERNAME_", itername)

        tmp = tmp.split("\n")
        for i in range(0,6):
            print(tmp[i])
        #print(tmp[1])
        for i in attrlist:
            tp=tmp[7].replace("_ATRNAME_", i)
            tp=tp.replace("_VALNAME_", i)
            print(tp)
        for i in range(8, 21):
            print(tmp[i])
        for i in attrlist:
            print("             n"+i,"\t=>\tr"+tableName[3:]+"."+i+",")
        for i in range(22, 24):
            print(tmp[i])
        for i in attrlist:
            print("             n"+i, "\t =>\tr"+tableName[3:]+"."+i+",")
        for i in range(26, 30):
            print(tmp[i])


#printEXP("MZGSM","MZ","MZGSM",0)
#printEXP("MZ_DOP","MZD","MZ_DOP",1)
#printEXP("TU","TU","TU",0)
#printEXP("INZOKK_DOP","IDP",0)