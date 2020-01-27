req = str(input("Please Enter Reg The Last Char is $ \n"))
req =req.replace(" ", "")
req = list(req)
token = []
def chara(req):
    if(req[0]=="i" and req[1]=="f" and req[2]=="-" and req[3]=="e" and req[4]=="l" and req[5]=="s" and req[6]=="e"):
        token.append(["Keywords","if-else"])
        return 7
    elif(req[0]=="i" and req[1]=="f"):
        token.append(["Keywords","if"])
        return 2
    elif(req[0]=="w" and req[1]=="h" and req[2]=="i" and req[3]=="l" and req[4]=="e"):
        token.append(["Keywords","while"])
        return 5
    elif(req[0]=="e" and req[1]=="l" and req[2]=="s" and req[3]=="e"):
        token.append(["Keywords","else"])
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
    for i in range(chara(req)):
        req.pop(0)
    if(len(req)==0):
        print("\n is okie")
    else:
        lexicalAnalysis(req)

lexicalAnalysis(req)

# Work with File ...
f = open("table.txt" , "w+")
f.write(str(token))
f.close()


