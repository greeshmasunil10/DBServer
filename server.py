# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:52:27 2020

@author: Greeshma
"""
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip().decode(encoding="utf-8")
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        raw= data.split(',');
        if (raw[0]=="find"):
            response=findCustomer(raw[1]).encode()
        if (raw[0]=="add"):
            response=addCustomer(data).encode()
        socket.sendto(response, self.client_address)

def startServer():
    print("Starting server...")
    loadData()
    if __name__ == "__main__":
        HOST, PORT = "localhost", 9999
        with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
            server.serve_forever()
data={}
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
    f1=open('data.txt', 'a')
    f1.write("\n"+name+"|" +raw[2]+"|"+raw[3]+"|"+raw[4])
    f1.close()
    loadData()
    return("Customer "+name+" has been added")
    
startServer()
loadData()
