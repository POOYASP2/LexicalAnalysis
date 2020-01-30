req = str(input("Please Enter a String The Last Char is $ \n"))
req =req.replace(" ", "")
req = list(req)
token = []

def digit(req):
    counter = 0
    summ = 0 
    sreq = []
    while counter < len(req):
        if(req[counter].isdigit() == True):
            for j in range(counter , len(req)):
                if(req[j].isdigit() == True):
                    summ = summ * 10
                    summ = summ + int(req[j])                    
                else:
                    sreq.append(summ)
                    counter = j - 1 
                    summ = 0
                    break
        else:
            sreq.append(req[counter])
        counter = counter + 1 
    return sreq
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
        token.append(["*", "*"])
        return 1
    elif(req[0]=="+"):
        token.append(["+", "+"])
        return 1
    elif(req[0]==">"):
        token.append([">", ">"])
        return 1
    elif(req[0]=="<"):
        token.append(["<", "<"])
        return 1
    elif(req[0]=="="):
        token.append(["=", "="])
        return 1
    elif(req[0]=="$"):
        token.append(["$", "$"])
        return 1
    else:
        token.append(["Variable",req[0]])
        return 1

def lexicalAnalysis(req):
    for i in range(dfa(req)):
        req.pop(0)
    if(len(req)==0):
        print("\n is okie")
    else:
        lexicalAnalysis(req)

lexicalAnalysis(digit(req))
# Work with File ...
f = open("table.txt" , "w+")
f.write(str(token))
f.close()
