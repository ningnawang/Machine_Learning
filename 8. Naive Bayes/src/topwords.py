import sys
import math

dicC = {}
dicL = {}
nC = 0 #total number of words in con
nL = 0
vocabulary = {} # total number of distinct words in all documents

filename = sys.argv[1]
with open(filename, 'r') as inputFileObj:
    for cate in inputFileObj:
        cate = cate.splitlines()[0] #get rid of /n at the end of each line
        with open(cate, 'r') as inputCate:
            for word in inputCate:
                word = word.splitlines()[0]
                word = word.lower()
                if vocabulary.has_key(word) == True:
                    vocabulary[word] = vocabulary.get(word) + 1
                else:
                    vocabulary[word] = 1
                if "con" in cate:
                    nC += 1
                    if dicC.has_key(word) == True:
                        dicC[word] = dicC.get(word) + 1
                    else:
                        dicC[word] = 1
                elif "lib" in cate:
                    nL += 1
                    if dicL.has_key(word) == True:
                        dicL[word] = dicL.get(word) + 1
                    else:
                        dicL[word] = 1

dicC_P = {} #dictionary for (word, smoothed probability)
dicL_P = {}
for w in vocabulary:
    if dicC.has_key(w) is False:
        dicC[w] = 0
    p = math.log((dicC[w] + 1.0) / (nC + len(vocabulary)))
    dicC_P[w] = p

for w in vocabulary:
    if dicL.has_key(w) is False:
        dicL[w] = 0
    p = math.log((dicL[w] + 1.0) / (nL + len(vocabulary)))
    dicL_P[w] = p
    
dicC_sorted = sorted(dicC_P, key = dicC.get, reverse = True)
dicL_sorted = sorted(dicL_P, key = dicL.get, reverse = True)

count = 0      
for w in dicL_sorted:
    if count < 20:
        print str(w) + " " + str(("%.4f" % math.exp(dicL_P.get(w)))[1:])
        count += 1
print "\r"
count = 0      
for w in dicC_sorted:
    if count < 20:
        print str(w) + " " + str(("%.4f" % math.exp(dicC_P.get(w)))[1:])
        count += 1

