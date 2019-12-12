import re;
p=re.compile('//',re.S);
fileContent=open('Pfam.hmm','r').read();
paraList=p.split(fileContent)
for para in paraList:
    with open('pfamID.txt') as IDlist:
        for ID in IDlist:
            if ID in para:
                f = open('pfamID.hmm','a')
                f.write(para + '//')
                f.close()

