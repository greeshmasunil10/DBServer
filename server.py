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
        raw= data.split('|');
        if (len(raw)==1):
            response=findCustomer(raw[0]).encode()
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
        
def findCustomer(name):
    if (name not in data):
        return("customer not found")
    record=data[name]
    print("oooooooooooooooo.",record)
    res=""
    res+=name+","
    for k,v in record.items():
        res+=v+","
    return(res)

#def AddCustomer():         
        
    
startServer()
loadData()
findCustomer()