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


forward_dict = {}
prev_dict = {}
result = 0.0
filename = sys.argv[1]
with open(filename, 'r') as inputFileObj:
    for line in inputFileObj:
        line = line.strip()
        line = line.split(" ")
        T = len(line) # length of observation, col
        # number to observation(word): i to line[i]       
        for col in xrange(0, T):
            if col == 0: # set initial state probability
                for row in xrange(0, N):
                    iniState = numToState[row]
                    prev_dict[iniState] = math.log(prior_dict[iniState]) + math.log(emit_dict[iniState][line[col]])
#                 print prev_dict
#                 print "--------------" + line[col]
            else:
                for row in xrange(0,N):
                    currState = numToState[row]
                    for pre_row in xrange(0,N):
                        preState = numToState[pre_row]
                        if pre_row == 0:
                            forward_dict[currState] = (prev_dict[preState]) + math.log(trains_dict[preState][currState])
                        else:
                            forward_dict[currState] = log_sum(forward_dict[currState], (prev_dict[preState]) + math.log(trains_dict[preState][currState])) 
                    forward_dict[currState] = (forward_dict[currState] + math.log(emit_dict[currState][line[col]]))
                prev_dict = forward_dict
#                 print forward_dict
#                 print "--------------" + line[col]
                forward_dict = {}
        
        for i in xrange(0, N):
            if i == 0:
                result = prev_dict[numToState[i]]
            else:
                result = log_sum(result, prev_dict[numToState[i]])
        print result