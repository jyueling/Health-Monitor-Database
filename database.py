import json


def createO2table():
    fp = open("oxygen",'a')  
    fp.close( )

def createBPtable():
    fp = open("bp",'a')  
    fp.close( )

def createPulsetable():
    fp = open("pulse",'a')  
    fp.close( )

def parseJsonfile():#(jsonfile):
    with open('data') as json_file:
        data = json.load(json_file)
    
    for jsonfile in data['data']:    
        if jsonfile['name'] == "pulse":
            storePulsedata(jsonfile['values'])
        elif jsonfile['name'] == "bp":
            storeBPdata(jsonfile['values'])
        elif jsonfile['name'] == "oxygen":
            storeO2data(jsonfile['values'])
    
def storeO2data(O2_data):
    try:
        file_object = open('oxygen', 'a')
        file_object.write(str(O2_data)+'\n')
        file_object.close()
        return "store O2 data success"
    except Exception as e:
        return "store O2 data failed: "+ e

def storeBPdata(BP_data):
    try:
        file_object = open('bp', 'a')
        file_object.write(str(BP_data[0])+' '+str(BP_data[1])+'\n')
        file_object.close()
        return "store BP data success"
    except Exception as e:
        return "store BP data failed: "+ e
        
def storePulsedata(Pulse_data):
    try:
        file_object = open('pulse', 'a')
        file_object.write(str(Pulse_data)+'\n')
        file_object.close()
        return "store Pulse data success"
    except Exception as e:
        return "store Pulse data failed: "+ e
        
def getO2data():
    try:
        with open('oxygen', 'r') as fp:
            lines = fp.readlines()
            data = lines[-1]
        return data
        print("get O2 data success")
    except Exception as e:
        print("get O2 data failed: "+e)
        
def getBPdata():
    try:
        with open('bp', 'r') as fp:
            lines = fp.readlines()
            data = lines[-1]
        return data
        print("get BP data success")
    except Exception as e:
        print("get BP data failed: " + e)
    
def getPulsedata():
    try:
        with open('pulse', 'r') as fp:
            lines = fp.readlines()
            data = lines[-1]
        return data
        print("get Pulse data success")
    except Exception as e:
        print("get Pulse data failed: "+e)

if __name__ == '__main__':
    createO2table()
    createBPtable()  
    createPulsetable()
    
    #parseJsonfile()
    print(getPulsedata())
