import codecs

f = codecs.open('input.txt', 'r', 'utf-8')
inp = f.read()
lines = inp.split('\n')

output = open('output.txt', 'w')
param = ''
field = ''
txt = ''
table = ''


def params_get():
    for line in lines:
        field = line[line.find('.')+1:line.find(' ')]
        table = line[:line.find('.')]
        text = line[line.find('-'):line.find(';')]
        output.write("      /* Для поля "+text+" */\n")
        output.write("      elsif RREC.FIELD_NAME = '"+field+"' then \n")
        output.write("          R" + table + "."+field+" := RREC.NEW_VALUE;\n")
        output.write("\n")

    output.write("end if;\n")

#params_get()

srecord = ''

def build_func():
    srecord = lines[0].upper()
    srecord = srecord.replace('\r','')
    srecord = srecord[2:]
    for line in lines:
        param = line[:line.find('\r')].upper()
        #txt = line[line.find('-- '):]
        if (line.find('--') == -1 ):
            if (param[0] in ('n','d','s','N','D','S')):
                field = param[1:]
            else:
                field = param
            output.write("      "+param+"       => R"+srecord+"."+field+", \r")

#build_func()


master_text = ''
def params_get2():
    ncounter = 0
    for line in lines:
        table = line[line.find('•	')+2:line.find('.')]
        field= line[line.find('.')+1:line.find(' ')]
        text = line[line.find(' - '):].replace('\r','')
        if (line.find('--') != -1):
            master_text = line
            master_text = master_text.replace('--','')
            master_text = master_text.replace('\r', '')

            output.write("  if STABLE_NAME = '" +master_text+ "'  then\n")
            output.write("      for RREC_" + master_text + " in (select AU.*\n")
            output.write("                                      from AEXT_DML_AUDIT AU\n")
            output.write("                                      where AU.DATE_OPER = DDATE_OPER\n")
            output.write("                                      and AU.ID_SESSION = NID_SESSION\n")
            output.write("                                      and AU.TABLE_OWNER = STABLE_OWNER\n")
            output.write("                                      and AU.TABLE_NAME = STABLE_NAME\n")
            output.write("                                      and AU.OPER_KIND = NOPER_KIND\n")
            output.write("                                      and NOPER_KIND != -1\n")
            output.write("                                      and AU.REC_ID = NREC_ID)\n")

            output.write("      loop\n")

            output.write('      /* Для раздела "' + master_text + '" */\n')
        else:
            ncounter = ncounter + 1
            output.write("          /* Для поля "+text+" */\n")
            if (ncounter == 1):
                output.write("          if RREC_" + master_text + ".FIELD_NAME = '" + field + "' then \n")
            else:
                output.write("          elsif RREC_"+master_text+".FIELD_NAME = '"+field+"' then \n")
            output.write("              R" + table + "."+field+" := RREC_"+master_text+".NEW_VALUE;\n")
            output.write("\n")

    output.write("          end if;\n")
    output.write("        end loop;\n")
    output.write("      end if;\n")


#nnum = 0
tabsarr = []
arr = []
def create_insert():
    table = ''
    nnum = 0
    for line in lines:
        if (line[0:2]=='--'):
            table = line[2:]
            #print(table)
            #output.write(");\n")
            #output.write("insert into " + table)
            #output.write("(\n")
            nnum = 0
            tabsarr.append(table)
        else:
            nnum = nnum +1
            field = line[line.find('.')+1:line.find(' ')]
            #output.write(""+field+",\n")

            arr.append([table,field])

    for tab in tabsarr:
        output.write(");\n")
        output.write("insert into PARUS_PAY." + tab)
        output.write("(\n")
        for arrline in arr:
            if (arrline[0] == tab):
                field = arrline[1]
                output.write("  " + field + ",\n")
        output.write(")\n")
        output.write("values\n")
        output.write("(\n")
        for arrline in arr:
            if (arrline[0] == tab):
                field = arrline[1]
                output.write("  null,\n")
        output.write(");\n")

#params_get2()

build_func()
#create_insert()