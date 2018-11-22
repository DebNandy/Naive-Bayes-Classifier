# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:06:03 2018

@author: shuva
"""

# -*- coding: utf-8 -*-


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


combined_vocab = con_vocab+lib_vocab

stats = {}
for i in combined_vocab:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1
N = int(sys.argv[3])
top_N = sorted(stats,key = stats.get,reverse= True)[:N]
#print('removing: ')
#for i in top_N:
#    print(i)

complete_vocab = list(set(combined_vocab))
complete_vocab = [x for x in complete_vocab if x not in top_N]
n_vocab = len(complete_vocab)
P_con = count_con/(count_con+count_lib)
P_lib = 1-P_con
con_vocab = [x for x in con_vocab if x not in top_N]
lib_vocab = [x for x in lib_vocab if x not in top_N]
n_con = len(con_vocab)
n_lib = len(lib_vocab)
con_counter = Counter(con_vocab)
lib_counter = Counter(lib_vocab)

log_P_w_con = {t:np.log((con_counter[t]+1)/(n_con+n_vocab)) for t in complete_vocab}
log_P_w_lib = {t:np.log((lib_counter[t]+1)/(n_lib+n_vocab)) for t in complete_vocab}

    
tst = open(sys.argv[2],'r')
test_files = [line.rstrip('\n') for line in tst]

test_vocab = list()
#print('starting tests')
accuracy = 0
for i in test_files:
    f = open(i, 'r',encoding='latin1')
    texts = [line.rstrip('\n') for line in f]
    texts = [line.lower() for line in texts]
    if 'con' in i:
        true_class = 'C'
    else :
        true_class = 'L'
    log_con_probab = np.log(P_con)
    log_lib_probab = np.log(P_lib)
    for word in texts:
        log_con_probab = log_con_probab + log_P_w_con.get(word,0)
        log_lib_probab = log_lib_probab + log_P_w_lib.get(word,0)
    if log_con_probab > log_lib_probab:
        predicted_class = 'C'
    else:
        predicted_class = 'L'
    print(predicted_class)
    if predicted_class == true_class:
        accuracy = accuracy + 1

accuracy = accuracy / len(test_files)
print( 'Accuracy:','%.04f' % accuracy)



#N = 0, 0.8056
#N = 10, 0.8056
#N = 25, 0.8333
#N = 50, 0.8611
#N = 100, 0.8611
#N = 200, 0.8611