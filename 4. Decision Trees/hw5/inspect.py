import math
import sys

negativeAttr = ["no", "cheap", "low", "Two", "small", "lessthan3min", "slow", "before1950", "notA"]
positiveAttr = ["yes", "expensive", "high", "MoreThanTwo", "large", "morethan3min", "fast", "after1950", "A"]

valuePair = {"year": ["before1950", "after1950"], "solo": ["no", "yes"], "vocal": ["no", "yes"], "length": ["lessthan3min", "morethan3min"],\
             "original": ["no", "yes"], "tempo": ["slow", "fast"], "folk": ["no", "yes"], "classical": ["no", "yes"],\
             "rhythm": ["no", "yes"], "jazz": ["no", "yes"], "rock": ["no", "yes"], "hit": ["no", "yes"],\
             "love": ["no", "yes"], "debut": ["no", "yes"], \
             "M1": ["notA", "A"], "M2": ["notA", "A"], "M3": ["notA", "A"],"M4": ["notA", "A"], "M5": ["notA", "A"], "P1": ["notA", "A"], \
             "P2": ["notA", "A"], "P3": ["notA", "A"], "P4": ["notA", "A"], "F": ["notA", "A"], "grade": ["notA", "A"], \
             "class": ["no", "yes"], "buying": ["cheap", "expensive"], "maint": ["low", "high"], "doors": ["Two", "MoreThanTwo"],\
             "person": ["Two", "MoreThanTwo"], "boot": ["small", "large"], "safety": ["low", "high"]}


def entropy(num1, num2):
    sum = num1 + num2
    p1 = num1 * 1.0 /sum
    p2 = num2 * 1.0 /sum
    if p1 == 1 or p2 == 1: return 0
    H = p1 * math.log(1 / p1, 2) + p2 * math.log(1 / p2, 2)
    return H


countLine = 0
positive = 0
negative = 0
filename = sys.argv[1]
with open(filename, 'r') as inputFileObj:
    for line in inputFileObj:
        line = line.strip().split(",")
#         print type(line)
        if countLine == 0:
            countLine += 1 
            continue
#         print line
        countLine += 1
        
        if line[-1] in negativeAttr:
            negative += 1
        else:
            positive += 1
    
sum = positive + negative   
rootError = 0.0
if positive > negative: 
    rootError = negative
else: 
    rootError = positive
E = round(entropy((positive * 1.0) / (sum * 1.0) , (negative * 1.0) / (sum * 1.0)), 3)
print "entropy: " + str(E)
print "error: " + str(rootError * 1.0 / sum)
