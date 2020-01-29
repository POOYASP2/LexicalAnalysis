req = str(input("Please Enter Reg The Last Char is $ \n"))
req =req.replace(" ", "")
req = list(req)
token = []
sreq = []
summ = 0
counter = 0 
def digit():
    global counter  
    global summ
    while counter < len(req):
        if(req[counter].isdigit() == True):
            for j in range(counter , len(req)):
                if(req[j].isdigit() == True):
                    summ = summ * 10
                    summ = summ + int(req[j])                    
                else:
                    sreq.append(summ)
                    counter = j - 1 
                    break
        else:
            sreq.append(req[counter])
        counter = counter + 1 
digit()
def dfa(req):
    if(isinstance(req[0],int)):
        token.append(["Numbers", req[0]])
        return 1
    elif(req[0]=="i" and req[1]=="f"):
        token.append(["if","if"])
        return 2
    elif(req[0]=="w" and req[1]=="h" and req[2]=="i" and req[3]=="l" and req[4]=="e"):
        token.append(["while","while"])
        return 5
    elif(req[0]=="e" and req[1]=="l" and req[2]=="s" and req[3]=="e"):
        token.append(["else","else"])
        return 4
    elif(req[0]=="t" and req[1]=="h" and req[2]=="e" and req[3]=="n"):
        token.append(["then","then"])
        return 4
    elif(req[0]=="*"):
        token.append(["Operators", "*"])
        return 1
    elif(req[0]=="+"):
        token.append(["Operators", "+"])
        return 1
    elif(req[0]==">"):
        token.append(["Operators", ">"])
        return 1
    elif(req[0]=="<"):
        token.append(["Operators", "<"])
        return 1
    elif(req[0]=="="):
        token.append(["Operators", "="])
        return 1
    elif(req[0]=="$"):
        token.append(["Operators", "$"])
        return 1
    else:
        token.append(["identifier",req[0]])
        return 1

def lexicalAnalysis(req):
    for i in range(dfa(req)):
        req.pop(0)
    if(len(req)==0):
        print("\n is okie")
    else:
        lexicalAnalysis(req)
print(sreq)
lexicalAnalysis(sreq)
print(token)
# Work with File ...
f = open("table.txt" , "w+")
f.write(str(token))
f.close()
