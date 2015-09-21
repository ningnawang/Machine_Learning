import sys
import math
from math import *

#computes log sum of two exponentiated log numbers efficiently
def log_sum(left,right):
    if right < left:
        return left + log1p(exp(right - left))
    elif left < right:
        return right + log1p(exp(left - right));
    else:
        return left + log1p(1)
    

# initial transition probabilities dict
def readTrains(filename):
    trans_dict = {}
    temp = {}
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip()
            line = line.split(" ")
            for i in range(1, len(line)):
                p = line[i].split(":")
                temp[p[0]] = (float(p[1]))
            trans_dict[line[0]] = temp
            temp = {}
#             print trans_dict
    return trans_dict




# initial emit probabilities dict
def readEmit(filename):
    emit_dict = {}
    temp = {}
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip()
            line = line.split(" ")
            for i in range(1, len(line)):
                p = line[i].split(":")
                temp[p[0]] = (float(p[1]))
            emit_dict[line[0]] = temp
            temp = {}
#     print emit_dict
    return emit_dict


# initial prior probabilities dict
def readPrior(filename):
    prior_dict = {}
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip()
            line = line.split(" ")
            prior_dict[line[0]] = (float(line[1]))
#     print prior_dict
    return prior_dict



# load parameters
trains_dict = readTrains(sys.argv[2])
emit_dict = readEmit(sys.argv[3])
prior_dict = readPrior(sys.argv[4])
N = len(prior_dict) # length of state, row

# number to state
numToState = ["PR", "VB", "RB", "NN", "PC", "JJ", "DT", "OT"]


backward_dict = {}
prev_dict = {}
result = 0.0
filename = sys.argv[1]
with open(filename, 'r') as inputFileObj:
    for line in inputFileObj:
        line = line.strip()
        line = line.split(" ")
        T = len(line) # length of observation, col
        # number to observation(word): i to line[i]       
        for col in xrange(T-1, -1, -1):
            if col == T-1: # set initial state probability
                for row in xrange(0, N):
                    iniState = numToState[row]
                    prev_dict[iniState] = math.log(1.0)
#                 print prev_dict
#                 print "--------------" + line[col]
            else:
                for row in xrange(0,N):
                    currState = numToState[row]
                    for pre_row in xrange(0,N):
                        preState = numToState[pre_row]
                        if pre_row == 0:
                            backward_dict[currState] = (prev_dict[preState]) + math.log(trains_dict[currState][preState]) + math.log(emit_dict[preState][line[col+1]])
                        else:
                            backward_dict[currState] = log_sum(backward_dict[currState], (prev_dict[preState]) + math.log(trains_dict[currState][preState]) + math.log(emit_dict[preState][line[col+1]])) 
                prev_dict = backward_dict
#                 print backward_dict
#                 print "--------------" + line[col]
                backward_dict = {}
        
        for i in xrange(0, N):
            state = numToState[i]
            if i == 0:
                result = math.log(prior_dict[state]) + math.log(emit_dict[state][line[0]]) + prev_dict[state]
            else:
                result = log_sum(result, math.log(prior_dict[state]) + math.log(emit_dict[state][line[0]]) + prev_dict[state])
        print result

