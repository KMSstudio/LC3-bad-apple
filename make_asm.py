import pickle
with open('fflop.pickle', 'rb') as fr:
    arr = pickle.load(fr)

res = ''; cnt = 0
flag = 0; data=0
for line in arr:
    if not flag: flag=1; data=len(line)
    else: flag=0; res += '\t.fill\tx%04x ;frame %06d\n' % (data*256+len(line), cnt)
    for item in line:
        if not flag: flag=1; data=item[0]*16+item[1]
        else: flag=0; res += '\t.fill\tx%04x\n' % (data*256+(item[0]*16+item[1]))
    cnt = cnt+1
if not flag: res += '\t.fill\tx%04x ;terminate' % (255*256)
else: res += '\t.fill\tx%04x ;terminate' % (data*256+255)

with open('./asm.txt', 'w') as fw:
    fw.write(res)