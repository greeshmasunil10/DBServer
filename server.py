# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:52:27 2020

@author: Greeshma
"""
import socketserver
data={}
class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        request = self.request[0].strip().decode(encoding="utf-8")
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(request)
        raw= request.split(',');
        if (raw[0]=="find"):
            response=findCustomer(raw[1]).encode()
        if (raw[0]=="add"):
            response=addCustomer(request).encode()
        if (raw[0]=="delete"):
            response=deleteCustomer(raw[1]).encode()
        if (raw[0]=="updateage"):
            response=updateValue("age",raw[1],raw[2]).encode()
        if (raw[0]=="updateaddress"):
            response=updateValue("address",raw[1],raw[2]).encode()
        if (raw[0]=="updatephone"):
            response=updateValue("phone",raw[1],raw[2]).encode()
        if (raw[0]=="print"):
            response=printReport().encode()
        print("loaded",data.keys())    
        socket.sendto(response, self.client_address)

def startServer():
    print("Starting server...")
    loadData()
    if __name__ == "__main__":
        HOST, PORT = "localhost", 9999
        with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
            server.serve_forever()

def loadData():
    file1 = open("data.txt","r+")  
    for line in file1.readlines() :
        raw= line.split('|');
        data[raw[0]]={'age':raw[1],'address':raw[2],'phone':raw[3]}
    file1.close()   
    
def findCustomer(name):
    if (name not in data):
        return("customer not found")
    record=data[name]
    res=""
    res+=name+","
    for k,v in record.items():
        res+=v+","
    print("response:",res)
    return(res)

def addCustomer(line):  
    raw= line.split(',');
    name= raw[1]
    print(name)
    if (name in data):
        print(("customer already exists") )
        return("customer already exists")      
    data[name]={'age':raw[2],'address':raw[3],'phone':raw[4]}
    return("Customer "+name+" has been added")

def deleteCustomer(name):
    if (name not in data):
        return("customer not found")
    del data[name]
    return("Customer "+name+" has been deleted")

def updateValue(func,name,value):
    if (name not in data):
        return("customer not found")
    record=data[name]
    if(func=="age"):
         record['age']=value  
    if(func=="address"):
        record['address']=value  
    if(func=="phone"):
        record['phone']=value  
    return(func+" "+value+" has been updated")

def printReport():
    temp= sorted (data)
    res=""
    for k,v in data.items():
        res+=k+","
        for k1, v1 in v.items():
            res+=k1+","+v1+","
    print(res)
    return res
    
    
startServer()
loadData()
