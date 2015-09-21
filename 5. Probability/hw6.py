import math
import sys

X = []
Y = []

def expectation(X, Y):
    EX = 0.0
    EY = 0.0
    
    for x in X:
        EX += float(x)
    EX /= len(X) 
#     print EX
    
    for y in Y:
        EY += float(y)
    EY /= len(Y) 
#     print EY
    return [EX, EY]

def variance(X, Y):
    VarX = 0.0
    VarY = 0.0  
#     for x in X:
#         VarX += math.pow(float(x), 2)
#     VarX /= len(X)
#     VarX -= math.pow(expectation(X, Y)[0], 2)
#     for y in Y:
#         VarY += math.pow(float(y), 2)
#     VarY /= len(Y)
#     VarY -= math.pow(expectation(X, Y)[1], 2)
#     return [VarX, VarY]
    EX = expectation(X, Y)[0]
    EY = expectation(X, Y)[1]
    for x in X:
        VarX += math.pow(float(x) - EX, 2)
    VarX /= len(X) 
    for y in Y:
        VarY += math.pow(float(y) - EY, 2)
    VarY /= len(Y)
    return [VarX, VarY]


def covariance(X, Y):
    EX = expectation(X, Y)[0]
    EY = expectation(X, Y)[1]
    covXY = 0.0
    i = 0
    while i < len(X) and i < len(Y):
        covXY += (float(X[i]) - EX) * (float(Y[i]) - EY)
        i += 1 
    covXY /= i
    return covXY

def error(a, b, x, y):
    est = a * x + b
    error = est - y
    return abs(error)


filename = sys.argv[1]
with open(filename, 'r') as inputFileObj:
    for line in inputFileObj:
        line = line.strip().split('\t')
#         print line
        X.append(line[0])
        Y.append(line[1])
#     print X
    EX = expectation(X, Y)[0]
    EY = expectation(X, Y)[1]
    print "EX = " + str(EX)
    print "EY = " + str(EY)
    VarX = variance(X, Y)[0]
    VarY = variance(X, Y)[1]
    print "Var = " + str(VarX)
    print "Var + "+ str(VarY)
    covXY = covariance(X, Y)
#     print covXY
    a = round(covXY / VarX, 4)
    b = round(EY - a * EX, 4)
    r = round(covXY / (math.sqrt(VarX) * math.sqrt(VarY)), 4)
    
    print "a = " + str(a) + " (" + str(round(a, 1)) + ") " + \
          "b = " + str(b) + " (" + str(round(b)) + ") " + \
          "r = " + str(r) + " (" + str(round(r, 1)) + ") "
#     print a
#     print b
#     print r

    print error(a, b, 8.03, 6.9)
    print error(a, b, 8.03, 8.19)
    print error(a, b, 8.03, 7.45)
    print error(a, b, 8.03, 5.7)
