import codecs


f = codecs.open('input.txt', 'r', 'utf-8')
inp = f.read()
lines = inp.split('\n')

output = open('output.txt', 'w')
#str = ''

'''
for i in lines:
    str = i.replace('\r','')
    output.write("if "+str+" is not null then\n")
    output.write("update AGNLIST A set A."+str[1:]+" = "+str+" where A.RN = rRHT.AGENT;\n")
    output.write("end if;\n")
    output.write("\n")


for i in lines:
    str = i.replace('\r','')
    output.write("  DD." + str + "  as "+ str+ ",\n")
    #output.write("\n")
'''
#ZP_NORM_2YEAR   as COEFF_C03,
'''
num = 0
iter = 0
letter = ['A','B','C','D']
compl = ''

for i in lines:
    sstr = i.replace('\r','')
    num = num +1
    if (num == 9):
        num = 1
        iter = iter +1
    if(num < 10):
        compl = letter[iter] + '0' +  str(num)
    else:
        compl = letter[iter] + str(num)
    output.write("  " + sstr + "  as COEFF_" + compl + ",\n")
    #output.write("\n")


#COEFF_B10, -- ZP_DC_1YEAR
num = 0
iter = 0
letter = ['A','B','C','D']
compl = ''

for i in lines:
    sstr = i.replace('\r','')
    num = num +1
    if (num == 9):
        num = 1
        iter = iter +1
    if(num < 10):
        compl = letter[iter] + '0' +  str(num)
    else:
        compl = letter[iter] + str(num)

    output.write("  COEFF_" + compl + ",  -- " + sstr + ",\n")
'''

'''
case PKG_CALCTAB_EXT.GET_IMAGE_SHEET_NAME()
           when SHEET_ZP2_YEAR_ then
            NVL(COEFF_A01, 0)
           when SHEET_ZP2_1YEAR_ then
            NVL(COEFF_B01, 0)
           when SHEET_ZP2_2YEAR_ then
            NVL(COEFF_C01, 0)
         end, -- PAY_GZ


attrs = []
coeffs = []

for line in lines:
    sstr = line.replace('\r','')

    if (sstr.find('--') == -1):
        attrs.append(sstr)
    else:
        coeffs.append(sstr)

for attr in attrs:
    #print(attr)
  

attrs = []

for line in lines:
    sstr = line.replace('\r','')
    attrs.append(sstr)
i = 0
for attr in attrs:
    i = i +1
    output.write("  case PKG_CALCTAB_EXT.GET_IMAGE_SHEET_NAME()\n")
    output.write("      when SHEET_ZP2_YEAR_ then\n")
    output.write("          NVL(COEFF_A0"+str(i)+", 0)\n")
    output.write("      when SHEET_ZP2_1YEAR_ then\n")
    output.write("          NVL(COEFF_B0"+str(i)+", 0)\n")
    output.write("      when SHEET_ZP2_2YEAR_ then\n")
    output.write("          NVL(COEFF_C0"+str(i)+", 0)\n")
    output.write("  end, --"+attr+"\n")
    output.write("\n") 
     

for line in lines:
    sstr = line.replace('\r','')
    snum = (sstr[5:sstr.find(':')])
    nom = int(snum.replace(' ',''))
    scol = sstr[sstr.find('(')+1:sstr.find(',')]
    #print(nom)
    if (nom in(5,6,8,9,10,11,12,13)):
        output.write("-- "+str(nom)+"\n")
        output.write("GET_FORMULA_WRK_OGRD_0(TROW_ORGD, NCOL_"+str(nom)+", SFORMULA_ITOG_WRK);\n")
        output.write("PRSG_CALCTAB_IMAGE.WRITE_ROW_NUM(RCURSOR      => RROW_WRK_TYPE_0,\n")
        output.write("                                 SCOLUMN_NAME => "+scol+",\n")
        output.write("                                  NVALUE       => null,\n")
        output.write("                                  BPROTECT     => BPROTECT,\n")
        output.write("                                  SATTRIBUTE   => case\n")
        output.write("                                                  when NROW_TYPE in (0, 1) then\n")
        output.write("                                                          SATTRIBUTE1\n")
        output.write("                                                  else\n")
        output.write("                                                          null\n")
        output.write("                                                  end,\n")
        output.write("                                  SFORMULA     => SFORMULA_ITOG_WRK);\n")
        output.write("\n")

     
spref =''
for i in range(0,3):

    if (i in (1,2)):
        spref = str(i)
    output.write("if PKG_CALCTAB_EXT.GET_IMAGE_SHEET_NAME() = SHEET_DD1_YEAR_ then\n")
    for line in lines:
        sstr = line.replace('\r', '')
        output.write("RZP.Z_DD1_"+sstr+"_"+spref+"YEAR := RSW."+sstr+";\n")

    output.write("\n")


for line in lines:
        sstr = line.replace('\r', '')
        sstr = sstr.upper()
        output.write("  "+sstr+"   =>  RZPTP."+sstr[1:]+",\n")



for line in lines:
        sstr = line.replace('\r', '')
        sstr = sstr.replace('\t', '')
        output.write("  RNODE_VAL := PKG_XPATH.SINGLE_NODE(RNODE_Datas, '" + sstr + "');\n")
        output.write("  rESTIMPJOURNINVRGS.XML_" + sstr + " := PKG_XPATH.VALUE(RNODE_VAL); \n")

        output.write("\n")



for line in lines:
        sstr = line.replace('\r', '')
        #output.write( sstr + ",\n")
        output.write("  rESTIMPJOURNINVRGS." + sstr + ",\n")


for line in lines:
        sstr = line.replace('\r', '')
        #output.write( sstr + ",\n")

        output.write("  s"+sstr + " in varchar2,\n")

for line in lines:
        sstr = line.replace('\r', '')
        #output.write( sstr + ",\n")
        output.write("  " + sstr + " => rESTIMPJOURNINVRGS." + sstr[1:] + ",\n")

for line in lines:
        sstr = line.replace('\r', '')
        #output.write( sstr + ",\n")

        output.write("  "+sstr + " =>  "+sstr + ",\n")'''
'''n = 0
linesoutp = []
for line in lines:
        sstr = line.replace('\r', '')
        if (sstr.find('in') != -1):
                sstr = sstr.replace('in','=> null, in'+ ",\n")
                linesoutp.append(sstr)
                n=n+1
                output.write(sstr)
        if (sstr.find('in') == -1):
                linesoutp[n] = linesoutp[n].replace('--','default null, --')
                linesoutp[n] = linesoutp[n].replace('in', '--in')'''
'''
f = codecs.open('template', 'r', 'utf-8')
inp = f.read()

stemplate = ''

for line in lines:
        sstr = line.replace('\r', '')
        scolname = sstr[sstr.index('COLUMN'):sstr.index(' ')]
        stext = sstr[sstr.index("t'")+2:sstr.index("' n")]
        snumber = sstr[sstr.index(" n[")+3:sstr.index("] P")]
        sprn = sstr[sstr.index("RN[")+3:sstr.index("_]")+1]

        stemplate = inp.replace('_COLNAME_',scolname)
        stemplate = stemplate.replace('_POS_', snumber)
        stemplate = stemplate.replace('_PRN_',sprn)
        stemplate = stemplate.replace('_TEXT_',stext )
        stemplate = stemplate.replace('\r', '')
        output.write(stemplate+'\n\n')
        #print(sprn)
'''

'''
columns = []
rows = []
ntr = 0
#stemplate = "-- '_NAME_'\nPRSG_CALCTAB_IMAGE.WRITE_STR(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(_COLUMN_),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(_ROWW_),\nSVALUE       => '',\nBPROTECT     => BTRUE,\nSATTRIBUTE   => SATTRIBUTE);\n"
stemplate = "-- '_NAME_'\nPRSG_CALCTAB_IMAGE.WRITE_NUM(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(_COLUMN_),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(_ROWW_),\nNVALUE       => 0,\nBPROTECT     => BTRUE,\nSATTRIBUTE   => SATTRIBUTE);\n"

stmp=""
for line in lines:
        sstr = line.replace('\r', '')
        if (sstr == '--'):
                ntr = 1
        if(ntr == 0):
                columns.append(sstr)
        else:
                if (sstr != '--'):
                        rows.append(sstr)

print(rows)
spref = ''
for row in rows:
        output.write('---------------------------------------' + row + '----------------------------------------------\n\n')
        for col in columns:
                if (row == 'SCOLNAME' or row == 'SCOLNAMEIZM'):
                        spref = 'SWRECS(I).'
                else:
                        spref = 'TERRECS(j).'
                stmp = stemplate.replace("_NAME_",row+"."+col)
                stmp = stmp.replace("_COLUMN_",col)
                stmp = stmp.replace("_ROWW_", spref+row)
                output.write(stmp + '\n\n')


for line in lines:
        sstr = line.replace('\r', '')
        if (sstr.find('=>') != -1 and sstr.find('--') != -1):
                output.write(sstr[:sstr.find('--')] + '\n')
        else:
                output.write(sstr + '\n')


columns = []
vals = []
ntr = 0
#stemplate = "PRSG_CALCTAB_IMAGE.WRITE_ROW_NUM(RCURSOR => RROW,\nSCOLUMN_NAME => XXX,\nNVALUE       => YYY,\nBPROTECT     => BPROTECT,\nSATTRIBUTE   => SATTRIBUTE3,\nSFORMULA     => SFORMULA22);"

#stemplate = "GET_FORMULA_WRK_OGRD_0(TROW_ORGD, NCOL_NNN, SFORMULA_ITOG_WRK);\nPRSG_CALCTAB_IMAGE.WRITE_ROW_NUM(RCURSOR => RROW_WRK_TYPE_0,\nSCOLUMN_NAME => XXX,\nNVALUE       => null,\nBPROTECT     => BTRUE,\nSATTRIBUTE   => case when NROW_TYPE in (0, 1) then SATTRIBUTE3 else null end,\nSFORMULA     => SFORMULA_ITOG_WRK);\n"

stemplate = "GET_FORMULA_WRK_OGRD_0(TROW_ALL_WORK, PRSG_CALCTAB_IMAGE.COLUMN_ID(XXX), SFORMULA);\nPRSG_CALCTAB_IMAGE.WRITE_NUM(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(XXX),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(ROW_WORK_ALL),\nNVALUE     => null,\nBPROTECT     => BTRUE,\nSATTRIBUTE => SATTRIBUTE1,\nSFORMULA   => SFORMULA);\n"

stmp=""
for line in lines:
        sstr = line.replace('\r', '')
        if (sstr == '--'):
                ntr = 1
        if(ntr == 0):
                columns.append(sstr)
        else:
                if (sstr != '--'):
                        vals.append(sstr)

spref = ''
for i in range(len(columns)):
        col = columns[i]
        val = vals[i]
        output.write('---------------------------------------' + col + '----------------------------------------------\n\n')
        stmp = stemplate
        stmp = stmp.replace("XXX", col)
        stmp = stmp.replace("NNN", str(i+5))
        
        #if (val != "0"):
        #        stmp = stmp.replace("YYY", "RSW."+val)
        #else:
        #        stmp = stmp.replace("YYY", val)
        output.write(stmp + '\n\n')

f = codecs.open('input2', 'r', 'utf-8')
inp = f.read()
lines2 = inp.split('\n')

i = 1

for line in lines2:
        i = i+1
        line = line.replace('\r','')
        output.write('elsif NROWNUMBER = '+str(i+3)+' then\n')
        output.write("SFORMULA := 'ОКРУГЛ({"+line+"@СтрокаУслугиВсего}+{"+line+" @СтрокаРаботыВсего};5)';\n")
        output.write('\n')


stemplate = "PRSG_CALCTAB_IMAGE.READ_ROW_NUM(RCURSOR      => RROW,\nSCOLUMN_NAME => XXX,\nNVALUE       => RSW.YYY);\n"
f = codecs.open('input2', 'r', 'utf-8')
inp = f.read()
lines2 = inp.split('\n')

for line in lines2:
        line = line.replace('\r', '')
        stmp = stemplate
        stmp = stmp.replace("XXX", "COLUMN_" + line[2:])
        stmp = stmp.replace("YYY",  line)
        output.write(stmp + '\n')'''
'''
f = codecs.open('input2', 'r', 'utf-8')
inp = f.read()
lines2 = inp.split('\n')
i = 0

for line in lines2:
        i = i+1
        if (len(line)>180):
                print(i)


for line in lines2:
        i = i+1
        
        if (line.find('-----')>0):
                output.write('\n')
        else:
                output.write(line)
        
        for line in lines2:
                i = i + 1
                if (len(line) > 180):
                        print(i)


'''
'''
stemplates = "/* _NAME_ */\nPRSG_CALCTAB_IMAGE.WRITE_STR(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(_COLUMN_),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(_ROWW_),\nSVALUE       => _VALUE_,\nBPROTECT     => _BPROTECT_,\nSATTRIBUTE   => _SATTRIBUTE_);\n"
stemplaten = "/* _NAME_ */\nPRSG_CALCTAB_IMAGE.WRITE_NUM(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(_COLUMN_),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(_ROWW_),\nNVALUE       => _VALUE_,\nBPROTECT     => _BPROTECT_,\nSATTRIBUTE   => _SATTRIBUTE_);\n"

i = 0
tmp = ""

#цикл для DO_BEFORE_ALL
for line in lines:
        i = i +1
        COLNAME = line[0:line.index(' ')]
        #print(COLNAME)
        COMMENT = "Колонка "+line[line.index(":=")+4:line.index(";")-1]
        print(COMMENT)
        if (i < 13):
                tmp = stemplates.replace('_NAME_',COMMENT)
                tmp = tmp.replace('_VALUE_', "'X'")
        else:
                tmp = stemplaten.replace('_NAME_', COMMENT)
                tmp = tmp.replace('_VALUE_', "0")
        tmp = tmp.replace('_COLUMN_', COLNAME)
        tmp = tmp.replace('_ROWW_', "ROW_ITG_")
        if (i == 1 ):
                tmp = tmp.replace('_SATTRIBUTE_', 'SATTRIBUTE1')
        elif ( i < 13 and i > 1):
                tmp = tmp.replace('_SATTRIBUTE_', 'SATTRIBUTE2')
        else:
                tmp = tmp.replace('_SATTRIBUTE_', 'SATTRIBUTE3')
        tmp = tmp.replace('_BPROTECT_', 'BTRUE')
        output.write(tmp + '\n')

#цикл для DO_BEFORE_DET
for line in lines:
        i = i +1
        COLNAME = line[0:line.index(' ')]
        #print(COLNAME)
        COMMENT = "Колонка "+line[line.index(":=")+4:line.index(";")-1]
        print(COMMENT)
        if (i in (1,13,14,15)):
                tmp = stemplates.replace('_NAME_',COMMENT)
                tmp = tmp.replace('_VALUE_', "'X'")
        else:
                tmp = stemplaten.replace('_NAME_', COMMENT)
                tmp = tmp.replace('_VALUE_', "0")
        tmp = tmp.replace('_COLUMN_', COLNAME)
        tmp = tmp.replace('_ROWW_', "RSOCDIDET.SROW")
        if (i == 1 ):
                tmp = tmp.replace('_SATTRIBUTE_', 'SATTRIBUTE1')
        elif ( i < 13 and i > 1):
                tmp = tmp.replace('_SATTRIBUTE_', 'SATTRIBUTE2')
        else:
                tmp = tmp.replace('_SATTRIBUTE_', 'SATTRIBUTE3')
        if (i in (1,13,14,15)):
                tmp = tmp.replace('_BPROTECT_', 'BTRUE')
        else:
                tmp = tmp.replace('_BPROTECT_', 'BPROTECT')
        output.write(tmp + '\n')
stemplates = "/* _NAME_ */\nPRSG_CALCTAB_IMAGE.READ_STR(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(_COLUMN_),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(_ROWW_),\nSVALUE       => _VALUE_);\n"
stemplaten = "/* _NAME_ */\nPRSG_CALCTAB_IMAGE.READ_NUM(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(_COLUMN_),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(_ROWW_),\nNVALUE       => _VALUE_);\n"

i = 0
tmp = ""
#цикл для DO_AFTER_DET
for line in lines:
    i = i + 1
    COLNAME = line[0:line.index(' ')]
    COMMENT = "Считывание колонки " + line[line.index(":=") + 4:line.index(";") - 1]
    PARAM = line[line.index(";")+1:]
    if (i < 5 or i > 10):
        tmp = stemplates.replace('_NAME_', COMMENT)
        #tmp = tmp.replace('_VALUE_', "'X'")
    else:
        tmp = stemplaten.replace('_NAME_', COMMENT)
        #tmp = tmp.replace('_VALUE_', "0")
    tmp = tmp.replace('_COLUMN_', COLNAME)
    tmp = tmp.replace('_ROWW_', "RSOCDIDET.SROW")
    tmp = tmp.replace('_VALUE_', "RSOCDIDET."+PARAM)
    output.write(tmp + '\n')

for line in lines:
    sstr = line.replace('\r', '')
    output.write("SMACROS := SMACROS || '"+sstr +"' || CHR(13);"+ '\n')'''
columns = []
rows = []
vals=[]
ntr = 0
#stemplate = "PRSG_CALCTAB_IMAGE.WRITE_ROW_NUM(RCURSOR => RROW,\nSCOLUMN_NAME => XXX,\nNVALUE       => YYY,\nBPROTECT     => BPROTECT,\nSATTRIBUTE   => SATTRIBUTE3,\nSFORMULA     => null);"

# stemplate = "GET_FORMULA_WRK_OGRD_0(TROW_ORGD, NCOL_NNN, SFORMULA_ITOG_WRK);\nPRSG_CALCTAB_IMAGE.WRITE_ROW_NUM(RCURSOR => RROW_WRK_TYPE_0,\nSCOLUMN_NAME => XXX,\nNVALUE       => null,\nBPROTECT     => BTRUE,\nSATTRIBUTE   => case when NROW_TYPE in (0, 1) then SATTRIBUTE3 else null end,\nSFORMULA     => SFORMULA_ITOG_WRK);\n"

#stemplate = "GET_FORMULA_WRK_OGRD_0(TROW_ALL_WORK, PRSG_CALCTAB_IMAGE.COLUMN_ID(XXX), SFORMULA);\nPRSG_CALCTAB_IMAGE.WRITE_NUM(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(XXX),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(ROW_WORK_ALL),\nNVALUE     => null,\nBPROTECT     => BTRUE,\nSATTRIBUTE => SATTRIBUTE1,\nSFORMULA   => SFORMULA);\n"

#stemplate = "/* _NAME_ */\nPRSG_CALCTAB_IMAGE.READ_NUM(NCOLUMN_ID => PRSG_CALCTAB_IMAGE.COLUMN_ID(XXX),\nNROW_ID    => PRSG_CALCTAB_IMAGE.ROW_ID(_ROWW_),\nNVALUE       => _VALUE_);\n"
#PRSG_CALCTAB_IMAGE.READ_ROW_NUM(RCURSOR => RROW, SCOLUMN_NAME => COLUMN_OTH_2YEAR, NVALUE => RSW.NZ_OTH_2YEAR);
stemplate = "PRSG_CALCTAB_IMAGE.READ_ROW_NUM(RCURSOR => RROW, SCOLUMN_NAME => XXX, NVALUE => YYY);\n"
stmp = ""
for line in lines:
    sstr = line.replace('\r', '')
    if (sstr == '--'):
        ntr = 1
    if (ntr == 0):
        columns.append(sstr)
    else:
        if (sstr != '--'):
            vals.append(sstr)

spref = ''
for i in range(len(columns)):
    col = columns[i]
    val = vals[i]
    output.write('/* Чтение значения из колонки ' + col + '*/\n')
    stmp = stemplate
    stmp = stmp.replace("XXX", col)
    stmp = stmp.replace("NNN", str(i + 5))
    stmp = stmp.replace("YYY", "RKU."+val)

    # if (val != "0"):
    #        stmp = stmp.replace("YYY", "RSW."+val)
    # else:
    #        stmp = stmp.replace("YYY", val)
    output.write(stmp + '\n\n')