import pickle
with open('raw_array.pickle', 'rb') as fr:
    arr = pickle.load(fr)

sze = len(arr[0])

res = []
cur = '0'*sze
for arrIdx in range(0, len(arr)-1, 3):
    line = arr[arrIdx]
    xor = ''
    for idx in range(sze):
        xor += '1' if cur[idx]!=line[idx] else '0'
    res.append(xor)
    cur=line[:]

with open('xor_array.pickle', 'wb') as fw:
    pickle.dump(res, fw)