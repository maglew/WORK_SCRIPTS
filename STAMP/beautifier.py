import codecs

f = codecs.open('input.txt', 'r', 'utf-8')
inp = f.read()
lines = inp.split('\n')

output = open('output.txt', 'w')
i = 0
inparams = 0
indeclare = 0
incode =0

inlvlparams = 0
inlvldeclare = 0
inlvlcode =0

incomment = 0
instrcomment = 0
'''
for line in lines:
        i = i+1
        
        if (line.find('-----')>0):
                output.write('\n')
        else:
                output.write(line)
        '''
# проверка на длину строк
for line in lines:
        i = i + 1
        if (len(line) > 180):
                print(i)

i = 0
for line in lines:
        i = i + 1