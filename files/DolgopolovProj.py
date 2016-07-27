from DolgopolovGraph import Graph

class PathsGraph():
    mdict = {}
    id_set = set()
    arr_ins = {}

    def add(self, start, end):
        if start in self.mdict:
            self.mdict[start].append(end)
        else:
            self.mdict[start] = [end]
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
                if i == end:
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

#graphHealthy
gh = PathsGraph()

f = open('../../Cancer_LUAD_Network.txt')
while True:
    s = f.readline()
    if s == '': break
    s2 = s[:len(s)-1].split('\t')
    g.add(s2[0], s2[1], s2[2])
f.close()

print('the first file is read')

f = open('../../NewHumanNet.txt')
while True:
    s = f.readline()
    if s == '': break
    s2 = s[:len(s)-1].split('\t')
    gh.add(s2[0], s2[1])
f.close()

print('the second file is read')

repeated = g.id_set.intersection(gh.id_set)

print(len(repeated)/len(g.id_set))
print(len(repeated))
print(len(g.id_set), len(gh.id_set))

out_gh_minus_g = []

for i in repeated:
    if not i in gh.mdict and i in g.mdict:
        out_gh_minus_g.append(0 - len(g.mdict[i]))
    elif i in gh.mdict and not i in g.mdict:
        out_gh_minus_g.append(len(gh.mdict[i]) - 0)
    elif not (i in gh.mdict or i in g.mdict):
        out_gh_minus_g.append(0)
    else:
        out_gh_minus_g.append(len(gh.mdict[i]) - len(g.mdict[i]))

import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
# fig.suptitle('Histogram for repeated genes\' out dependences', fontsize=14, fontweight='bold')
# plt.hist(out_gh_minus_g, bins=100)
# plt.show()

''' thr for ins '''
mu = np.mean(out_gh_minus_g)

from math import sqrt
msum = 0
for i in out_gh_minus_g:
    msum += (i - mu)**2
sigma = sqrt(msum/len(out_gh_minus_g))
thr_min = mu - 2*sigma
print('thr_min: ', thr_min)
thr_max = mu + 2*sigma
print('thr_max: ', thr_max)


ids_more_max = []
ids_less_min = []

for i in repeated:
    diff = 0
    if not i in gh.mdict and i in g.mdict:
        diff = 0 - len(g.mdict[i])
    elif i in gh.mdict and not i in g.mdict:
        diff = len(gh.mdict[i]) - 0
    elif not (i in gh.mdict or i in g.mdict):
        diff = 0
    else:
        diff = len(gh.mdict[i]) - len(g.mdict[i])

    if diff > thr_max:
        ids_more_max.append((i, diff))
    elif diff < thr_min:
        ids_less_min.append((i, diff))

f = open('../progress/projects/Team0/diff_more_thr.txt','w+')
for k,v in ids_more_max:
    print(k,v,sep='\t', file=f)
f.close()
f = open('../progress/projects/Team0/diff_less_thr.txt','w+')
for k,v in ids_less_min:
    print(k,v,sep='\t', file=f)
f.close()
print('gocha')
