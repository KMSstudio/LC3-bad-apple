import pickle
with open('xor_array.pickle', 'rb') as fr:
    arr = pickle.load(fr)

sze = len(arr[0])
res = []
for line in arr:
    fflop = []
    for idx in range(sze):
        if line[idx]=='0': continue
        fflop.append((idx//16, idx%16))
    res.append(fflop)

with open('fflop.pickle', 'wb') as fw:
    pickle.dump(res, fw)