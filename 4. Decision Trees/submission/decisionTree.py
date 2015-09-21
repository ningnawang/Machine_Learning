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

# formate:[-, +]
attr1Value = None # store the values of attribute 1
attr2LeftValue = None # store the values of attribute 2 left
attr2RightValue = None # store the values of attribute 2 right
resultValue = None # store hte values of result

filename = sys.argv[1]
countLine = 0
trainError = 0
with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip().split(",")
    #         print type(line)
            if countLine == 0: 
                allAttrName = line
#                 print allAttrName 
                countLine += 1
                
class TreeNode:
    def __init__(self, attr, entro, list, valueSum, leftNode, rightNode):
        self.attr = attr
        self.entro = entro
        self.list = list
        self.valueSum = valueSum
        self.leftNode = leftNode
        self.rightNode = rightNode
    description = "This is the tree node that we want to build"
    author = "Nina Wang"
    
    def __str__(self):
#         s = "attribute: " + str(self.attr) + ", entropy: " + str(self.entro) +\
#             ", list: " + str(self.list) + ", Value Sum: " + str(self.valueSum) + "\n"
#         if self.leftNode is None:
#             s += ""
#         else:
#             s += " leftNode: " + str(self.leftNode)
#         if self.rightNode is None:
#             s += ""
#         else:
#             s += " leftNode: " + str(self.rightNode)
        global trainError
        s = "[" + str(self.list[1]) + "+/" + str(self.list[0]) + "-]" + "\n"
           
        if self.leftNode is None:
            if self.list[1] > self.list[0]:
                trainError += self.list[0]
            else:
                trainError += self.list[1]
        else:
            s += str(self.attr) + " = " + attr1Value[1] +": " + "[" + str(self.rightNode.list[1]) + "+/" + str(self.rightNode.list[0]) + "-]" + "\n"
            if self.rightNode.rightNode is None:
                if self.rightNode.list[1] > self.rightNode.list[0]:
                    trainError += self.rightNode.list[0]
                else:
                    trainError += self.rightNode.list[1]
            else:
                s += "| " + str(self.rightNode.attr) + " = " + attr2RightValue[1] +": " + "[" + str(self.rightNode.rightNode.list[1]) + "+/" + str(self.rightNode.rightNode.list[0]) + "-]" + "\n"
                s += "| " + str(self.rightNode.attr) + " = " + attr2RightValue[0] +": " + "[" + str(self.rightNode.leftNode.list[1]) + "+/" + str(self.rightNode.leftNode.list[0]) + "-]" + "\n"
                if self.rightNode.rightNode.list[1] > self.rightNode.rightNode.list[0]:
                    trainError += self.rightNode.rightNode.list[0]
                else:
                    trainError += self.rightNode.rightNode.list[1]
                       
                if self.rightNode.leftNode.list[1] > self.rightNode.leftNode.list[0]:
                    trainError += self.rightNode.leftNode.list[0]
                else:
                    trainError += self.rightNode.leftNode.list[1]
                       
            if self.rightNode is not None:
                s += str(self.attr) + " = " + attr1Value[0] +": " + "[" + str(self.leftNode.list[1]) + "+/" + str(self.leftNode.list[0]) + "-]" + "\n"
            if self.leftNode.rightNode is None:
                if self.leftNode.list[1] > self.leftNode.list[0]:
                    trainError += self.leftNode.list[0]
                else:
                    trainError += self.leftNode.list[1]
            else:
                s += "| " + str(self.leftNode.attr) + " = " + attr2LeftValue[1] +": " + "[" + str(self.leftNode.rightNode.list[1]) + "+/" + str(self.leftNode.rightNode.list[0]) + "-]" + "\n"
                s += "| " + str(self.leftNode.attr) + " = " + attr2LeftValue[0] +": " + "[" + str(self.leftNode.leftNode.list[1]) + "+/" + str(self.leftNode.leftNode.list[0]) + "-]" + "\n"
                if self.leftNode.rightNode.list[1] > self.leftNode.rightNode.list[0]:
                    trainError += self.leftNode.rightNode.list[0]
                else:
                    trainError += self.leftNode.rightNode.list[1]
                       
                if self.leftNode.leftNode.list[1] > self.leftNode.leftNode.list[0]:
                    trainError += self.leftNode.leftNode.list[0]
                else:
                    trainError += self.leftNode.leftNode.list[1]
        s += "error(train): " + str(trainError * 1.0 / self.valueSum)
        return  s
            
    
    def setAttr(self, attr):
        self.attr = attr
    def setEntro(self, entro):
        self.entro = entro 
    def setList(self, list):
        self.list = list 
    def setValueSum(self, valueSum):
        self.valueSum = valueSum
    def setLeftNode(self, leftNode):
        self.leftNode = leftNode
    def setRightNode(self, rightNode):
        self.rightNode = rightNode
        
    def getAttr(self):
        return self.attr
    def getEntro(self):
        return self.entro
    def getList(self):
        return self.list
    def getValueSum(self):
        return self.valueSum
    def getLeftNode(self):
        return self.leftNode
    def getRightNode(self):
        return self.rightNode

def entropy(num1, num2):
    sum = num1 + num2
    p1 = num1 * 1.0 /sum
    p2 = num2 * 1.0 /sum
    if p1 == 1 or p2 == 1: return 0
    H = p1 * math.log(1 / p1, 2) + p2 * math.log(1 / p2, 2)
    return H

def gainInfo(parentEntro, parentSum, leftList, rightList):
    
    leftEntro = entropy(leftList[0], leftList[1])
    leftSum = leftList[0] + leftList[1]
#     print leftList
    if leftList[0] > leftList[1]: 
        leftNode = TreeNode(resultValue[0], leftEntro, leftList, leftSum, None, None)
    else:
        leftNode = TreeNode(resultValue[1], leftEntro, leftList, leftSum, None, None)
#     print leftNode
    rightEntro = entropy(rightList[0], rightList[1])
    rightSum = rightList[0] + rightList[1]
    if rightList[0] > rightList[1]: 
        rightNode = TreeNode(resultValue[0], rightEntro, rightList, rightSum, None, None)
    else:
        rightNode = TreeNode(resultValue[1], rightEntro, rightList, rightSum, None, None)
#     print rightNode
    gain = parentEntro - leftSum * 1.0 / parentSum * leftEntro - rightSum * 1.0 / parentSum * rightEntro 
    return {"gain": gain, "leftNode": leftNode, "rightNode": rightNode}
    
def listFuncRootPerLine(result):
    # format: [xx-, xx+]
    list = [0, 0]
    if result in negativeAttr:
        list[0] += 1
    if result in positiveAttr:
        list[1] += 1
    return list

def listFuncOneAttrPerLine(attr, result):
    # format: [xx-, xx+]
    dict = {'leftValue': [0, 0], 'rightValue':[0, 0]}
    if attr in negativeAttr:
        if result in negativeAttr:
            dict['leftValue'][0] += 1
#             print dict['leftValue'][0]
        if result in positiveAttr:
            dict['leftValue'][1] += 1
    if attr in positiveAttr:
        if result in negativeAttr:
            dict['rightValue'][0] += 1
        if result in positiveAttr:
            dict['rightValue'][1] += 1
    return dict

def listFuncTwoAttrPerLine(attr1, attr2, result):
    # format: [xx-, xx+]
    dict = {'llValue': [0, 0], 'lrValue':[0, 0], 'rlValue':[0, 0], 'rrValue':[0, 0]}
    if attr1 in negativeAttr:
        if attr2 in negativeAttr:
            if result in negativeAttr:
                dict['llValue'][0] += 1
#                 print dict['llValue'][0]
            if result in positiveAttr:
                dict['llValue'][1] += 1
        if attr2 in positiveAttr:
            if result in negativeAttr:
                dict['lrValue'][0] += 1
#                 print dict['lrValue'][0]
            if result in positiveAttr:
                dict['lrValue'][1] += 1
    if attr1 in positiveAttr:
        if attr2 in negativeAttr:
            if result in negativeAttr:
                dict['rlValue'][0] += 1
            if result in positiveAttr:
                dict['rlValue'][1] += 1
        if attr2 in positiveAttr:
            if result in negativeAttr:
                dict['rrValue'][0] += 1
            if result in positiveAttr:
                dict['rrValue'][1] += 1
    return dict



# calculate num of negatvie and positive instances of result colomn            
def listFuncRoot():
    listRoot = [0, 0]
    filename = sys.argv[1]
    countLine = 0
    global resultValue
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip().split(",")
    #         print type(line)
            if countLine == 0: 
                countLine += 1
#                 allAttrName = line
                continue
#             print line
            countLine += 1
            
            # calculate num of negatvie and positive instances of result colomn 
            tempRoot = listFuncRootPerLine(line[-1])
            listRoot[0] += tempRoot[0]
            listRoot[1] += tempRoot[1]
#     print allAttrName[-1]
    resultValue = valuePair.get(allAttrName[-1])
#     print resultValue
    #         print listRoot
    return listRoot
# print listFuncRoot()

# calculate num of negatvie and positive instances between colomn i(attribute) and colomn j(result) 
def ListFuncOneAttr(i, j):
    dict = {'leftValue': [0, 0], 'rightValue':[0, 0]}
    filename = sys.argv[1]
    countLine = 0    
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip()
    #         print type(line)
            if countLine == 0: 
                countLine += 1
                continue
            line = line.split(",")
#             print line
            countLine += 1    
            # calculate num of negatvie and positive instances of attr1 colomn 
            temp = listFuncOneAttrPerLine(line[i], line[j])
            
    #         print temp
            dict['leftValue'][0] += temp['leftValue'][0]
            dict['leftValue'][1] += temp['leftValue'][1]
            dict['rightValue'][0] += temp['rightValue'][0]
            dict['rightValue'][1] += temp['rightValue'][1]
#             print dict
    return dict    
# print ListFunc(0, -1)

def ListFuncTwoAttr(s, t, j):
    dict = {'llValue': [0, 0], 'lrValue':[0, 0], 'rlValue':[0, 0], 'rrValue':[0, 0]}
    filename = sys.argv[1]
    countLine = 0    
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip()
    #         print type(line)
            if countLine == 0: 
                countLine += 1
                continue
            line = line.split(",")
#             print line
            countLine += 1    
            # calculate num of negatvie and positive instances of attr1 colomn 
            temp = listFuncTwoAttrPerLine(line[s], line[t], line[j])
    #         print temp
            dict['llValue'][0] += temp['llValue'][0]
            dict['llValue'][1] += temp['llValue'][1]
            dict['lrValue'][0] += temp['lrValue'][0]
            dict['lrValue'][1] += temp['lrValue'][1]
            dict['rlValue'][0] += temp['rlValue'][0]
            dict['rlValue'][1] += temp['rlValue'][1]
            dict['rrValue'][0] += temp['rrValue'][0]
            dict['rrValue'][1] += temp['rrValue'][1]
#             print dict
    return dict  
# print ListFuncTwoAttr(0, 1, -1)

# trian a tree with only one level)
def stump():
    global attr1Value 
        
    listRoot = listFuncRoot()
#     print listRoot
    parentEntro = entropy(listRoot[0], listRoot[1])
    parentSum = listRoot[0] + listRoot[1]
    if listRoot[0] > listRoot[1]:
        root = TreeNode(resultValue[0], parentEntro, listRoot, parentSum, None, None)
    else:
        root = TreeNode(resultValue[1], parentEntro, listRoot, parentSum, None, None)
#     print str(root.attr)
    i = 0
    gainInfo1 = {"gain": 0.0, "leftNode": None, "rightNode": None} #attribute with highest gain
    gainInfo1ID = 0 

    while i < len(allAttrName) - 1:
        temp = gainInfo(parentEntro, parentSum, ListFuncOneAttr(i, -1)['leftValue'], ListFuncOneAttr(i, -1)['rightValue'])
        if temp["gain"] > gainInfo1["gain"]:
            gainInfo1 = temp
            gainInfo1ID = i
        i += 1
    
    # set values of first attribute
    attr1Value = valuePair.get(allAttrName[gainInfo1ID])
#     print attr1Value
    
    root.setAttr(allAttrName[gainInfo1ID])
    leftNode = gainInfo1["leftNode"]
#     leftNode.setAttr(allAttrName[gainInfo2ID])
    rightNode = gainInfo1["rightNode"]
#     rightNode.setAttr(allAttrName[gainInfo2ID])
    root.setLeftNode(gainInfo1["leftNode"])
    root.setRightNode(gainInfo1["rightNode"])
        
    return root

# print stump()
# print stump().leftNode
# print stump().rightNode


def trainTree():
    root = stump()
    global trainError
    global attr2LeftValue 
    global attr2RightValue
    
    # choose root's left node
    gainInfoLeft = {"gain": 0.0, "leftNode": None, "rightNode": None} #attribute with first highest gain
    gainInfoLeftID = 0     
    i = 0
    leftDict = None # store the negative or positive list of second attribute
    while i < len(allAttrName) - 1:
        if i != allAttrName.index(root.getAttr()):
            attr1 = allAttrName.index(root.getAttr())
            attr2 = allAttrName.index(allAttrName[i])
            dict = ListFuncTwoAttr(attr1, attr2, -1)
#             print dict
            tempLeft = gainInfo(root.leftNode.getEntro(), root.leftNode.getValueSum(), dict["llValue"], dict["lrValue"])
#             print allAttrName[i]
#             print tempLeft["gain"]
#             print "gain: " + str(gainInfoLeft["gain"])
            if (tempLeft["gain"] - gainInfoLeft["gain"]) > 0.00000001 :
#                 print "before"
#                 print allAttrName[i]
#                 print tempLeft["gain"]
#                 print "gain: " + str(gainInfoLeft["gain"])
                gainInfoLeft = tempLeft
                gainInfoLeftID = i
                leftDict = dict
#                 print "after"
#                 print allAttrName[i]
#                 print tempLeft["gain"]
#                 print "gain: " + str(gainInfoLeft["gain"])
        i += 1
#     print gainInfoLeftID
    # set values of second left attribute
    attr2LeftValue = valuePair.get(allAttrName[gainInfoLeftID])
    if gainInfoLeft["gain"] > 0.1:
#         print gainInfoLeft["gain"]
        root.leftNode.setAttr(allAttrName[gainInfoLeftID])
#         print gainInfoLeft
#         print leftDict
        if leftDict["llValue"][0] > leftDict["llValue"][1]:
            llNode = TreeNode(resultValue[0], None, leftDict["llValue"], None, None, None)
        else:
            llNode = TreeNode(resultValue[1], None, leftDict["llValue"], None, None, None)
        if leftDict["lrValue"][0] > leftDict["lrValue"][1]:
            lrNode = TreeNode(resultValue[0], None, leftDict["lrValue"], None, None, None)
        else:
            lrNode = TreeNode(resultValue[1], None, leftDict["lrValue"], None, None, None)
        root.leftNode.setLeftNode(llNode)
        root.leftNode.setRightNode(lrNode)

  
    # choose root's right node
    gainInfoRight = {"gain": 0.0, "leftNode": None, "rightNode": None} #attribute with second highest gain
    gainInfoRightID = 0
    i = 0
    rightDict = None # store the negative or positive list of second attribute
    while i < len(allAttrName) - 1:
        if i != allAttrName.index(root.getAttr()):
            attr1 = allAttrName.index(root.getAttr())
            attr2 = allAttrName.index(allAttrName[i])
            dict = ListFuncTwoAttr(attr1, attr2, -1)
            tempRight = gainInfo(root.rightNode.getEntro(), root.rightNode.getValueSum(), dict["rlValue"], dict["rrValue"])
            if (tempRight["gain"] - gainInfoRight["gain"]) > 0.00000001:
                gainInfoRight = tempRight
                gainInfoRightID = i
                rightDict = dict
        i += 1
    # set values of second right attribute
    attr2RightValue = valuePair.get(allAttrName[gainInfoRightID])
        
    if gainInfoRight["gain"] > 0.1:
#         print rightDict
        root.rightNode.setAttr(allAttrName[gainInfoRightID])
#         print gainInfoRight["gain"]
        if rightDict["rlValue"][0] > rightDict["rlValue"][1]:
            rlNode = TreeNode(resultValue[0], None, rightDict["rlValue"], None, None, None)
        else:
            rlNode = TreeNode(resultValue[1], None, rightDict["rlValue"], None, None, None)
        if rightDict["rrValue"][0] > rightDict["rrValue"][1]:
            rrNode = TreeNode(resultValue[0], None, rightDict["rrValue"], None, None, None)
        else:
            rrNode = TreeNode(resultValue[1], None, rightDict["rrValue"], None, None, None)
        root.rightNode.setLeftNode(rlNode)
        root.rightNode.setRightNode(rrNode)
    return root

def testError():
    root = trainTree()
    filename = sys.argv[2]
    testAttrName = None
    countLine = 0
    attr1 = None
    attr2Left = None
    attr2Right = None
    testError = 0
    with open(filename, 'r') as inputFileObj:
        for line in inputFileObj:
            line = line.strip().split(",")
#                 print line
            if countLine == 0: 
                testAttrName = line
#                 print allAttrName 
                countLine += 1
                attr1 = testAttrName.index(root.getAttr())
                if root.leftNode.leftNode is not None: # the tree has only one level(attribute)
                    attr2Left = testAttrName.index(root.leftNode.getAttr())
                if root.rightNode.leftNode is not None: # the tree has only one level(attribute)
                    attr2Right = testAttrName.index(root.rightNode.getAttr())
            else:
                countLine += 1 
                if root.leftNode.leftNode is None:
                    if line[attr1] in negativeAttr:
                        if line[-1] != root.leftNode.getAttr():
                            testError += 1
                elif line[attr1] in negativeAttr:
                    if line[attr2Left] in negativeAttr:
                        if line[-1] != root.leftNode.leftNode.getAttr():
                            testError += 1
                    if line[attr2Left] in positiveAttr:
                        if line[-1] != root.leftNode.rightNode.getAttr():
                            testError += 1
                
                if root.rightNode.leftNode is None:
                    if line[attr1] in positiveAttr:
                        if line[-1] != root.rightNode.getAttr():
                            testError += 1
                elif line[attr1] in positiveAttr:
                    if line[attr2Right] in negativeAttr:
                        if line[-1] != root.rightNode.leftNode.getAttr():
                            testError += 1
                    if line[attr2Right] in positiveAttr:
                        if line[-1] != root.rightNode.rightNode.getAttr():
                            testError += 1  
#     print countLine          
    return "error(test): " + str(testError * 1.0 / (countLine - 1))
print trainTree()
print testError()