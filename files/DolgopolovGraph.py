class Graph():
    mdict = {}
    id_set = set()
    arr_ins = {}

    def add(self, start, end, weight):
        if start in self.mdict:
            self.mdict[start].append((end, weight))
        else:
            self.mdict[start] = [(end, weight)]
        self.id_set.add(start)
        self.id_set.add(end)

        if end in self.arr_ins:
            self.arr_ins[end] += 1
        else:
            self.arr_ins[end] = 1


    def __str__(self):
        res = ''
        for k,v in self.mdict.items():
            res += k + ' ' + str(v) + '\n'
		# return str(self.mdict)
        return(res)

    def get_ends(self, start):
        return self.mdict[start]

	# func gets number of stripes coming in point
    def get_in_num(self, end):
        s = 0
        for k,v in self.mdict.items():
            for i in v:
                if i[0] == end:
                    s += 1
                    break
        return s

	# func gets number of stripes coming out of point
    def get_out_num(self, start):
        if start in self.mdict:
            return len(self.mdict[start])
        else: 
            return 0


g = Graph()

f = open('../data/HumanNet.txt')
while True:
    s = f.readline()
    if s == '': break
    s2 = s.split(' ')
    g.add(s2[0], s2[1], s2[2][:len(s2[2])-1])
f.close()

''' CHECKPOINT '''
print('file is read')

# print(g)
arr_ins = []
arr_outs = []

for i in g.id_set:
    arr_outs.append(g.get_out_num(i))

''' CHECKPOINT '''
print('массив1 посчитан')

# for i in g.id_set:
    # arr_ins.append(g.get_in_num(i))

''' CHECKPOINT '''
print('массивы посчитаны')

import numpy as np
import matplotlib.pyplot as plt

''' CHECKPOINT '''
print('заимпортили пиплот')
for k,v in g.arr_ins.items():
    arr_ins.append(v)

print('arr_ins: ', len(g.arr_ins))
print('id_set: ', len(g.id_set))

arr_ins += [0 for i in range(len(g.id_set) - len(arr_ins))]

# plt.hist(arr_ins + [0 for i in range(len(g.id_set) - len(arr_ins))], bins=600)
# plt.show()

# plt.hist(arr_outs, bins=700)
# plt.show()

''' thr for ins '''
mu = np.mean(arr_ins)

from math import sqrt
msum = 0
for i in arr_ins:
    msum += (i - mu)**2
sigma = sqrt(msum/len(arr_ins))
thr = mu + 2*sigma
print('ins: ', thr)


''' thr for outs '''
mu = np.mean(arr_outs)

msum = 0
for i in arr_outs:
    msum += (i - mu)**2
sigma = sqrt(msum/len(arr_outs))
thr = mu + 2*sigma
print('outs: ', thr)

