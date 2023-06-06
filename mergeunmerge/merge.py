import os
import stat
current_dir=os.getcwd()
print(current_dir)

conffiles=[]
for root, dirs, files in os.walk(current_dir):
    for file in files:

        if file=='merge.py' or file=='mergedfile' or file.endswith('~') or file.startswith('.'):
            continue
        name,ext=os.path.splitext(file)
        if ext !='.spi':
            continue
        print(root)
        if not '/ppg/' in os.path.join(root,file) or '(copy)' in os.path.join(root,file):
            continue
        conffiles.append(os.path.join(root,file))

# print(conffiles)
with open ('mergedfile','w') as wf:
    for file in conffiles:
        with open (file,'r',encoding='utf-8') as f:
            lines=f.read()
        relative_path = os.path.relpath(file,current_dir)
        # print(relative_path)
        wf.write(f'\nstartseparate {relative_path}\n')
        wf.write(lines)
        wf.write(f'\nendseparate {relative_path}\n')
        f.close()
    
wf.close()