attres=["KOEFV","OBM","CORR","OTK"]
cells=["CELL_KV","CELL_OB","CELL_PR","CELL_OT"]

output = open('output', 'w')

#output.write("  \n")  #
tmp1 = "if X.XXX != 0 then"
tmp2 = " PRSG_EXCEL.CELL_VALUE_WRITE(CELL_XXX, 0, ILINE, X.XXX);"
tmp3 = "PRSG_EXCEL.CELL_ATTRIBUTE_SET(CELL_XXX,0,iLINE,'Font.FontStyle','bold');"
tmp4 = "else"
tmp5 = "PRSG_EXCEL.CELL_VALUE_WRITE(CELL_XXX, 0, ILINE, '');"
tmp6 = "end if;"

def printLines(type,iter):
    if type == 1:
        for i in range(len(attres) ):
            for j in range (3):
                tj=str(j)
                if j == 0:
                    tj = ''
                output.write(tmp1.replace("X.XXX",iter+"."+(attres[i]+tj )) +"\n")  #
                tmp22=tmp2.replace("CELL_XXX", (cells[i] + tj))
                tmp22 = tmp22.replace("X.XXX", iter+"."+(attres[i]+tj))
                output.write(tmp22 + "\n")  #
                output.write(tmp3.replace("CELL_XXX", (cells[i] + tj)) + "\n")  #
                output.write(tmp4+ "\n")  #
                output.write(tmp5.replace("CELL_XXX", (cells[i] + tj)) + "\n")  #
                output.write(tmp6 + "\n")  #
                output.write( "\n")  #
            output.write("\n")  #
    elif type == 2:
        for i in range(len(attres) ):
            for j in range (3):
                if j == 0:
                    tj = ''
                output.write(tmp1.replace("X.XXX", iter + "." + (attres[i] + tj)) + "\n")  #
                tmp22 = tmp2.replace("CELL_XXX", (cells[i] + tj))
                tmp22 = tmp22.replace("X.XXX", iter + "." + (attres[i] + tj))
                output.write(tmp22 + "\n")  #
                output.write(tmp4 + "\n")  #
                output.write(tmp5.replace("CELL_XXX", (cells[i] + tj)) + "\n")  #
                output.write(tmp6 + "\n")  #
                output.write("\n")  #
    #elif type == 3:


printLines(2,"RT")


'''
 if R.XXX != 0 then
      PRSG_EXCEL.CELL_VALUE_WRITE(CELL_XXX, 0, ILINE, R.XXX);
      PRSG_EXCEL.CELL_ATTRIBUTE_SET(CELL_XXX,0,iLINE,'Font.FontStyle','bold');
    else
      PRSG_EXCEL.CELL_VALUE_WRITE(CELL_KV1, 0, ILINE, '');
    end if;

    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_KV, 0, ILINE, RT.KOEFV);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_KV1, 0, ILINE, RT.KOEFV1);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_KV2, 0, ILINE, RT.KOEFV2);

    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_OB, 0, ILINE, RT.OBM);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_OB1, 0, ILINE, RT.OBM1);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_OB2, 0, ILINE, RT.OBM2);

    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_PR, 0, ILINE, RT.CORR);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_PR1, 0, ILINE, RT.CORR1);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_PR2, 0, ILINE, RT.CORR2);

    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_OT, 0, ILINE, RT.OTK);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_OT1, 0, ILINE, RT.OTK1);
    PRSG_EXCEL.CELL_VALUE_WRITE(CELL_OT2, 0, ILINE, RT.OTK2);
'''