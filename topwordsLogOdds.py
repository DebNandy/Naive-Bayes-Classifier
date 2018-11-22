# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 00:54:57 2018

@author: shuva
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:31:41 2018

@author: shuva
"""


import numpy as np
import sys
from collections import Counter
t = open(sys.argv[1],'r')
train_files = [line.rstrip('\n') for line in t]
count_con = 0
count_lib = 0
con_vocab = list()
lib_vocab = list()
for i in train_files:
    f = open(i, 'r',encoding='latin1')
    texts = [line.rstrip('\n') for line in f]
    texts = [line.lower() for line in texts]
    if 'con' in i:
        count_con = count_con + 1
        con_vocab.extend(texts)
    else :
        count_lib = count_lib + 1
        lib_vocab.extend(texts)

complete_vocab = con_vocab+lib_vocab
complete_vocab = list(set(complete_vocab))
n_vocab = len(complete_vocab)
P_con = count_con/(count_con+count_lib)
P_lib = 1-P_con
n_con = len(con_vocab)
n_lib = len(lib_vocab)
con_counter = Counter(con_vocab)
lib_counter = Counter(lib_vocab)

log_odds = {t:np.log((con_counter[t]+1)/(n_con+n_vocab)) - np.log((lib_counter[t]+1)/(n_lib+n_vocab)) for t in complete_vocab}
sorted_log_odds = sorted(log_odds, key = log_odds.get)
for w in sorted_log_odds[:20]:
      print (w, '%.04f' % -log_odds[w])
  
sorted_log_odds.reverse()
print()
for w in sorted_log_odds[:20]:
      print (w, '%.04f' % log_odds[w])