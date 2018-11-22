# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 00:22:00 2018

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

complete_vocab = con_vocab+lib_vocab
complete_vocab = list(set(complete_vocab))
n_vocab = len(complete_vocab)
P_con = count_con/(count_con+count_lib)
P_lib = 1-P_con
n_con = len(con_vocab)
n_lib = len(lib_vocab)
q = float(sys.argv[3])

con_counter = Counter(con_vocab)
lib_counter = Counter(lib_vocab)

log_P_w_con = {t:np.log((con_counter[t]+q)/(n_con+q*n_vocab)) for t in complete_vocab}
log_P_w_lib = {t:np.log((lib_counter[t]+q)/(n_lib+q*n_vocab)) for t in complete_vocab}

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
#print(len(train_files))

#q = 0, 0.7778
#q = 0.1, 0.8333
#q = 0.5, 0.8056