import sys
import math


#------------------------------------------training-------------------------------------
dicC = {}
dicL = {}
nC = 0 #total number of words in con
nL = 0
vocabulary_train = {} # total number of distinct words in all documents

docC = 0 # the subset of documents from Examples for which the target value is C
docL = 0
example = 0 # the num of Examples

filename = sys.argv[1]
with open(filename, 'r') as inputFileObj:
    for cate in inputFileObj:
        cate = cate.splitlines()[0] #get rid of /n at the end of each line
        example += 1
        if "con" in cate:
            docC += 1
        else:
            docL += 1
 
        with open(cate, 'r') as inputCate:
            # store word frequency
            for word in inputCate:
                word = word.splitlines()[0]
                word = word.lower()
                if vocabulary_train.has_key(word) == True:
                    vocabulary_train[word] = vocabulary_train.get(word) + 1
                else:
                    vocabulary_train[word] = 1
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

# p(v)
pC = math.log(docC * 1.0 / example * 1.0)
pL = math.log(docL * 1.0 / example * 1.0)


# p(w|v)
dicC_P = {} #dictionary for (word, smoothed probability)
dicL_P = {}
for w in vocabulary_train:
    if dicC.has_key(w) is False:
        dicC[w] = 0
    p = math.log((dicC[w] + 1.0) / (nC + len(vocabulary_train)))
    dicC_P[w] = p

for w in vocabulary_train:
    if dicL.has_key(w) is False:
        dicL[w] = 0
    p = math.log((dicL[w] + 1.0) / (nL + len(vocabulary_train)))
    dicL_P[w] = p
    

#------------------------------------------testing-------------------------------------

example_test = 0 # all test labels
accuracy = 0 # labeled error

filename1 = sys.argv[2]
with open(filename1, 'r') as inputFileObj:
    for cate in inputFileObj:
        vNB_C = pC # v_NB
        vNB_L = pC
        cate = cate.splitlines()[0] #get rid of /n at the end of each line
        example_test += 1
        answer = ""
        if "con" in cate:
            answer = "C"
        else:
            answer = "L"

        with open(cate, 'r') as inputCate:
            for word in inputCate:
                word = word.splitlines()[0]
                word = word.lower()

                # v_NB
                if vocabulary_train.has_key(word) is True:
                    vNB_C += dicC_P[word]
                    vNB_L += dicL_P[word]
#         vNB_C += pC
#         vNB_L += pL
        
        # classification
        labe = " "
#         print vNB_C
#         print vNB_L
        if vNB_C > vNB_L:
            label = "C"
        else:
            label = "L"
            
        print label
        if label == answer:
            accuracy += 1
print "Accuracy: " + str(("%.4f" % (accuracy * 1.0 / example_test))[1:])