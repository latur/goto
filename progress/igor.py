#!/usr/bin/python
# -*- coding: utf-8 -*-
# cd Public/goto/
# ./progress/igor.py 2

import os, sys
from sys import argv
from math import log

K = int(argv[1])

# Reverse complement
def Rev(s) :
	rev = ''; com = {'A' : 'T', 'G' : 'C', 'T' : 'A', 'C' : 'G'}
	for k in range(0,len(s)) : rev = com[s[k]] + rev
	return rev


# Читаем тренировочный файл
OB = {'E' : [], 'C' : []}; name = ''
f = open('data/X1/train.fa')
for line in f.xreadlines():
  if line == '' : continue
  if line[0] == '>' : 
    name = line[1:].replace('\n','')
  else :
    OB[name[0]].append(line.replace('\n',''))
f.close()


# Строим MM
def MakeModel(data) :
  M = {}; MX = {}
  for read in data :
    for i in range(0, len(read) - K) :
      v = read[i:(i+K)]
      if v not in M : M[v] = 0
      M[v] += 1
    for i in range(0, len(read) - K + 1) :
      v = read[i:(i+K-1)]
      if v not in MX : MX[v] = 0
      MX[v] += 1
  # Нормировка
  for e in M :
    M[e] = float(M[e])/MX[e[0:(K-1)]]
  return M

MME = MakeModel(OB['E'])
MMC = MakeModel(OB['C'])

def TestModel(M, read) :
  prob = 0
  for i in range(0,len(read) - K) :
    kmer = read[i:(i+K)]
    if kmer not in M : 
      prob -= 99999
      continue
    prob += log(M[kmer])
  return prob


f = open('data/X1/test.fa')
for line in f.xreadlines():
  if line == '' : continue
  if line[0] == '>' : continue
  xread = line.replace('\n','')
  # Проверка обоих моделей
  if TestModel(MME, xread) >= TestModel(MMC, xread) :
    print 'E'
  else :
    print 'C'
f.close()
