import os
with open ('mergedfile','r') as f:
    lines=f.readlines()

f.close()


fileinfo=[]
for line in lines:
    if line.startswith('startseparate'):
        fileinfo=[]
        splited=line.strip('').split(' ')
        fullpath=splited[1].strip('\n')
        root=os.path.split(fullpath)[0]
        fname=os.path.split(fullpath)[1]


    fileinfo.append(line)

    
    if line.startswith('endseparate'):
        fileinfo=fileinfo[1:-1]
        if not os.path.exists(root):
            os.makedirs(root)
        with open(f'{fullpath}','w') as fo:
            fo.writelines(fileinfo)
        fo.close()