import math
import numpy as np
import sys
import time

countLine = 0
prevError = 100.0
error = 0.0
learningRate = 0.05
weight_InputHidden = np.random.random((5, 5)).dot(0.001)
weight_HiddenOutput = np.random.random((5, 1)).dot(0.001)
new_weight_InputHidden = np.random.random((5, 5)).dot(0.001)
new_weight_HiddenOutput = np.random.random((5, 1)).dot(0.001)


def sigmoidFunc(x):
#     print x
#     print math.exp(x) 
#     print 1.0 + math.exp(-x)    
#     print 1.0 / (1.0 + math.exp(-x))
    return 1.0 / (1.0 + math.exp(-x))

def hiddenOutputTrain(targetValue, output, hiddenInput, weightHiddenOutput):
    for i in range(0, 5):
        new_weight_HiddenOutput[i,0] = weightHiddenOutput[i,0] \
                            + learningRate * (targetValue - output) * output * (1 - output) * hiddenInput[0,i]
#     print new_weight_HiddenOutput
    return new_weight_HiddenOutput
   
def inputHiddenTrain(targetValue, output, inputMatrix, weightHiddenOutput, weightInputHidden):
    for i in range(0, 5):
        for j in range(0,5):
            new_weight_InputHidden[i,j] = weightInputHidden[i,j] \
                            + learningRate * (targetValue - output) * output * (1 - output) \
                            * weightHiddenOutput[j, 0] * hiddenInput[0,j] * (1-hiddenInput[0,j]) * inputMatrix[0,i]
#     print new_weight_InputHidden
    return new_weight_InputHidden

steps = 0
startTime = time.clock()

while error == 0.0 or error > 0.1 and (time.clock() - startTime) < 80 and steps < 6000:
#     print "running time: " + str(time.clock() - startTime)
    error = 0.0
    filename = sys.argv[1]
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip().split(",")
    #         print type(line)
            if countLine == 0:
                countLine += 1 
                continue
#             print line
            
            x0 = 1.0
            x1 = (float(line[0]) - 1900.0) / (2000.0 - 1900.0)
        #         print x1
            x2 = float(line[1]) / 10.0
        #         print x2
            if line[2] == "yes":
                x3 = 1.0
            else:
                x3 = 0.0
            if line[3] == "yes":
                x4 = 1.0
            else:
                x4 = 0.0
            if line[4] == "yes":
                targetValue = 1
            else:
                targetValue = 0
            inputMatrix = np.matrix([x0, x1, x2, x3, x4])
        #   print inputMatrix   
             
    #         while error > 0.02:
            hiddenInput = inputMatrix.dot(weight_InputHidden)
    #         print hiddenInput
    #         print hiddenInput[0,1]
    #         print sigmoidFunc(hiddenInput[0,0])
            hiddenInput = np.mat([sigmoidFunc(hiddenInput[0,0]), sigmoidFunc(hiddenInput[0,1]),sigmoidFunc(hiddenInput[0,2]),\
                                sigmoidFunc(hiddenInput[0,3]), sigmoidFunc(hiddenInput[0,4])], dtype = float)
    #         print hiddenInput
            output = sigmoidFunc(hiddenInput.dot(weight_HiddenOutput))   
#             print "target value: " + str(output)
    #         print weight_HiddenOutput
            weight_HiddenOutput = hiddenOutputTrain(targetValue, output, hiddenInput,weight_HiddenOutput)
    #         print weight_HiddenOutput
            weight_InputHidden = inputHiddenTrain(targetValue, output, inputMatrix, weight_HiddenOutput, weight_InputHidden)
            error += math.pow((targetValue - output), 2) * 1/2 
        print error
#       print "error : " + str(error)
#       print "prevError : " +str(prevError)
        
        if prevError < error:
            break
        prevError = error
    countLine = 0
    steps += 1
#     error = 0.0
#     print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    #         break
print "TRAINING COMPLETED! NOW PREDICTING."
# print "iterate: " + str(steps)
  

countLine = 0
filename = sys.argv[2]
with open(filename, 'r') as inputFileObj:
    for line in inputFileObj:
        line = line.strip().split(",")
#             print type(line)
        if countLine == 0:
            countLine += 1 
            continue
#         print line
        
        x0 = 1.0
        x1 = (float(line[0]) - 1900.0) / (2000.0 - 1900.0)
    #         print x1
        x2 = float(line[1]) / 10.0
    #         print x2
        if line[2] == "yes":
            x3 = 1.0
        else:
            x3 = 0.0
        if line[3] == "yes":
            x4 = 1.0
        else:
            x4 = 0.0
            
        inputMatrix = np.matrix([x0, x1, x2, x3, x4])         
        hiddenInput = inputMatrix.dot(weight_InputHidden)
        hiddenInput = np.mat([sigmoidFunc(hiddenInput[0,0]), sigmoidFunc(hiddenInput[0,1]),sigmoidFunc(hiddenInput[0,2]),\
                            sigmoidFunc(hiddenInput[0,3]), sigmoidFunc(hiddenInput[0,4])], dtype = float)
        output = sigmoidFunc(hiddenInput.dot(weight_HiddenOutput))   
#         print "target value: " + str(output)
        if output > 0.6:
            print "yes"
        else:
            print "no"
    