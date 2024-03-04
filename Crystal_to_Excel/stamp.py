'''''
PRSG_CALCTAB_IMAGE.WRITE_ROW_NUM
      (
        rCURSOR      => rROW,
        sCOLUMN_NAME => COLUMN_US_ACS_YEAR_,
        nVALUE       => rSW.US_ACS_YEAR,
        bPROTECT     => bTRUE,
        sATTRIBUTE   => sATTRIBUTE3
      );

'''''''''''


import codecs
'''
в файл attrlist записывать имена входных переменных, 
имена ячеек и линий там они расположены попорядку,
 группы разделены знаком --
после этого соберется простенький шаблон 

'''
f = codecs.open('inp', 'r', 'utf-8')
maket = f.read()

ss = maket.split('1')

print(ss)
