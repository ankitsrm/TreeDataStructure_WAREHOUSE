import time
class TruckNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
       

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
       
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
       
        print(prefix , self.data)
        ol2=str(prefix) + str(self.data)
        _writeToOutputPS2(ol2)
        #listContianer.append(self.data)

        if self.children:
            for child in self.children:
                child.print_tree()
        
    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def isUidExist(listOfUid, Uid):
        isExist=False
        for checkUid in listOfUid:
            if Uid== checkUid:
                isExist=True
                
        return isExist  

    def get_Value(self):
        listContianer.append(self.data)
        
        if self.children:
            for child in self.children:
                child.get_Value()

    
    
    def _printTruckRec(self):
        if self.children:
            print ("Total nnumber of vehicles entered in the warehouse : ", len (self.children))            
            _writeToOutputPS2("Total nnumber of vehicles entered in the warehouse : {}".format(str(len (self.children))) )
            for child in self.children:
                print("{}, {}".format(child.data , child.children[-1].data))
                _writeToOutputPS2("{}, {}".format(child.data , child.children[-1].data))
            


    def truckStricksWareHouse(self):
        parentNode =self.children
        print(len(parentNode))
        child = parentNode.children
        return len(child)

    def replaceNode(node, overWritevalue):
      
        # Base Case 
        if (node == None):
            return
    
        # Replace data with current depth 
        #
        
            for child in node.children:
                print(child.data)
                TruckNode.replaceNode(child.data, overWritevalue) 
    



    def _checkTruckRec(tNode, Uid):
        
        found = False
        for parent in tNode.children:

            if int(parent.data) == int(Uid):
                found = True
                break
            else:
                continue      

        if found == True:
            child= parent.children
            print("------------- checkTruckRec: {} ---------------" .format(Uid))
            _writeToOutputPS2("------------- checkTruckRec: {} ---------------" .format(Uid))

            countToStrike = int(child[-1].data)
            if (countToStrike % 2) == 0 :
                _writeToOutputPS2("Vehicle id {} entered {} times into the system. It just completed an order".format(Uid,str(child[-1].data)))
                print("Vehicle id {} entered {} times into the system. It just completed an order".format(Uid,str(child[-1].data)))
            
            elif(countToStrike == 0):
                _writeToOutputPS2("Vehicle id {} just reached the warehouse".format(Uid))
                print("Vehicle id {} just reached the warehouse".format(Uid))
            
            else:
                _writeToOutputPS2("Vehicle id {} entered {} times into the system. It is currently fulfilling an open order" .format(Uid, str(child[-1].data)))
                print("Vehicle id {} entered {} times into the system. It is currently fulfilling an open order" .format(Uid, str(child[-1].data)))
                    
            
        else :
            _writeToOutputPS2("------------- checkTruckRec: {} ---------------" .format(Uid))
            _writeToOutputPS2("Vehicle id {} did not come to the warehouse today".format(Uid))
            print("------------- checkTruckRec: {} ---------------" .format(Uid))
            print("Vehicle id {} did not come to the warehouse today".format(Uid))

def _printOrderStatus(rootNode,targetOrders):
    
    closeOrder = 0
    openOrder = 0
    yetToBeFullFilled=0
    
    if rootNode.children:
        for parent in  rootNode.children:
            checkoutcount = int(parent.children[-1].data)            
            
            if checkoutcount !=0:
                if(checkoutcount % 2) == 0:
                    maxDeliverCount = int(maxDeliverableByTruck)
                    orderCount=int(checkoutcount/maxDeliverCount)                    
                    closeOrder += orderCount
                else:
                    openOrder += int(checkoutcount)

    yetToBeFullFilled= int(targetOrders) - closeOrder - openOrder                 
    
    print("Open Orders : {}".format(openOrder))    
    print("Closed Orders : {} ". format(closeOrder))
    print("Yet to be fullfilled : {} " .format(yetToBeFullFilled))
    _writeToOutputPS2("Open Orders : {}".format(openOrder))
    _writeToOutputPS2("Closed Orders : {} ". format(closeOrder))
    _writeToOutputPS2("Yet to be fullfilled : {} " .format(yetToBeFullFilled))

def _highFreqTrucks(rootNode , frequency):
    print ("------------- highFreqTrucks: {} ---------------".format(frequency))
    _writeToOutputPS2("------------- highFreqTrucks: {} ---------------".format(frequency))
    found = False
    parent = 0
    UidContainer = []
    childContainer = []
    child = 0
    if rootNode.children : 
        for parent in rootNode.children:
            child = parent.children[-1].data
            parent = parent.data
            if (int(child) > int(frequency)):
                found = True
                UidContainer.append(parent)
                childContainer.append(child)

            else:
                continue
    
    if found == True : 
        print ("Vehicles that moved in/out more than {} times are:".format(frequency))
        _writeToOutputPS2("Vehicles that moved in/out more than {} times are:".format(frequency))
        #print("{}, {}".format(parent , child)) 
        for i in range(0,len(childContainer)):
           print("{}, {}".format(UidContainer[i] , childContainer[i]))
           _writeToOutputPS2("{}, {}".format(UidContainer[i] , childContainer[i]))
    else:
        _writeToOutputPS2("No such vehicle present in the system")
        print("No such vehicle present in the system")              
        
def _maxDeliveries(rootNode):
    print ("------------- maxDeliveries ---------------")
    _writeToOutputPS2("------------- maxDeliveries ---------------")
    count = 0
    container = [] 
    found = False
    for parent in rootNode.children:
        child = int (parent.children[-1].data)
        parent = parent.data
        if (child > int(maxDeliverableByTruck)):
            found = True
            count += 1
            container.append(parent)
            
        else:
            continue

    if found == True:
        print("{} Vehicle Ids did their maximum deliveries:" . format(count))
        _writeToOutputPS2("{} Vehicle Ids did their maximum deliveries:" . format(count))
        for i in range(0, len(container)):
            _writeToOutputPS2(str(container[i]))
            print(container[i])

def _availTrucks(rootNode):
    print("------------- availTrucks ---------------")
    _writeToOutputPS2("------------- availTrucks ---------------")
    uidContainer=[]
    count = 0

    for parent in rootNode.children:
        child = int (parent.children[-1].data)
        parent = parent.data
        
        if ((child < int(maxDeliverableByTruck)) & (((child % 2) !=0) | child == 0 )):
            
            uidContainer.append(parent)
            count+=1
       
    if count !=0 : 
        print("{} Vehicle Ids that are currently available to deliver supplies:". format(count))
        _writeToOutputPS2("{} Vehicle Ids that are currently available to deliver supplies:". format(count))
        for i in range (0, count):
            print (uidContainer[i])
            _writeToOutputPS2(str(uidContainer[i]))

def _updateTruckRec(rootNode,Uid):
    print("------------- updateTruckRec: {} ---------------".format(Uid))
    _writeToOutputPS2("------------- updateTruckRec: {} ---------------".format(Uid))
    recfile = open("D:\\Assignment\\DSAD\\inputPS2.txt", "a+")
    recfile.write("\n")
    recfile.write(Uid)
    recfile.close()
    print("Vehicle Id {} record updated".format(Uid))
    _writeToOutputPS2("Vehicle Id {} record updated".format(Uid))

def _writeToOutputPS2(insertingLine):
    outputFile= open("D:\\Assignment\\DSAD\\outputPS2.txt","a+")
    outputFile.write("\n")
    outputFile.write(insertingLine)
    

def readPromptsPS2():
    readPromptsPS2= open("D:\\Assignment\\DSAD\\promptsPS2.txt", 'r')  
    line= readPromptsPS2.read().splitlines()
    
    for promptLine in line:
        if promptLine.find('printTruckRec') != -1:
            st= time.time()
            print("---- {} ----".format(promptLine)) 
            _writeToOutputPS2("---- {} ----".format(promptLine))     
            root = build_product_tree()
            TruckNode._printTruckRec(root)
            _writeToOutputPS2("-----------------------------------------------") 
            print("-----------------------------------------------")
            print("time taken = ", time.time() - st)
        
        if (promptLine.find('checkTruckRec') != -1):           
            checkTruckRecordLine= promptLine        
            truckNumber = checkTruckRecordLine.split(" ")
            Uid = truckNumber[1]            
            TruckNode._checkTruckRec(root,Uid)
            _writeToOutputPS2("-----------------------------------------------") 
            print("---------------------------------------------------")
        
        if (promptLine.find('printOrderStatus') != -1):
            print("------------- {} ---------------".format(promptLine))
            _writeToOutputPS2("------------- {} ---------------".format(promptLine)) 
            printOrderStatus = promptLine
            order = printOrderStatus.split(" ")
            targetOrder = order[1]
            _printOrderStatus(root, targetOrder) 
            _writeToOutputPS2("--------------------------------------------------- ")
            print("---------------------------------------------------")

        if (promptLine.find('highFreqTrucks') != -1):
            highFreqTruck = promptLine
            reqFreq = highFreqTruck.split(" ")
            freq = reqFreq[1]
            _highFreqTrucks(root, freq)
            _writeToOutputPS2("---------------------------------------------------")
            print("---------------------------------------------------")

        if (promptLine.find('maxDeliveries') != -1):
            _maxDeliveries(root)
            _writeToOutputPS2("---------------------------------------------------")
            print("---------------------------------------------------")

        if (promptLine.find('availTrucks') != -1):
            _availTrucks(root)
            _writeToOutputPS2("---------------------------------------------------")
            print("---------------------------------------------------")
        if (promptLine.find('updateTruckRec') != -1):
            updateTruckRec= promptLine
            newRecAdd = updateTruckRec.split(" ")
            Uid= newRecAdd[-1]
            _updateTruckRec(root,Uid)



def build_product_tree():
    root = TruckNode("Truck_Record")
    readTxtFile=open('D:\\Assignment\\DSAD\\inputPS2.txt', 'r')
    global maxDeliverableByTruck
    maxDeliverableByTruck = readTxtFile.readline()
    
    containerUid=[]
    count =0
    tNode=TruckNode("Truck_Records")
    found = False
    while True:
        count += 1
        checkOutCount=0
        line=readTxtFile.readline()
        
                    
        if not line:
            break
        else:
            
            Uid =int(line)
            if len(containerUid)==0:
                containerUid.append(Uid)
                          
                newNodeUid= TruckNode(Uid)
                newNodeUid.addChild(TruckNode(checkOutCount))
                tNode.addChild(newNodeUid)

            else:
                isExist = TruckNode.isUidExist(containerUid,Uid)
                if isExist == True:
                
                    for parent in tNode.children:
                        if parent.data == Uid:
                            child = parent.children
                            counting = int(child[-1].data)+1
                            parent.addChild(TruckNode(counting))
                            break   
                else:
                    containerUid.append(Uid)                    
                    otherChild = TruckNode(Uid)
                    otherChild.addChild(TruckNode(checkOutCount))
                    tNode.addChild(otherChild)



    #TruckNode._checkTruckRec(tNode,31)
    #TruckNode._printTruckRec(tNode)
   
    #TruckNode.print_tree(tNode)
    return tNode

listContianer=[]
 
if __name__ == "__main__":
    readPromptsPS2()
    #build_product_tree()
    