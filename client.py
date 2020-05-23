# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:00:17 2020

@author: Greeshma
"""
import socket
import sys

HOST, PORT = "localhost", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def request(data):
    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")
#    print("Sent:     {}".format(data))
#    print("Received: {}".format(received)) 
    print("\n Response form Server:")
    if(choice =="1"):
        printRecord(received)
    if(choice =="2"):
        print(received)
    if(choice =="3"):
        print(received)
    if(choice =="4"):
        print(received)
    if(choice =="5"):
        print(received)
    if(choice =="6"):
        print(received)
    if(choice =="7"):
        print(received)
    if(choice =="8"):
        print(received)
        
def entername():
    while True:
        name=input("Enter name:")
        if(name!=""):
            break
        else:
            print("Please enter again!")
    return name   
def enterage():
    while True:
        age=input("Enter age:")
        try:
            int(age)
            break
        except ValueError:
                print("Please enter a number!")
    return age  
def printRecord(received):
    if(received=="Customer not found!"):
        print(received)
        return(0)
    raw= received.split(',');
    print("Name:",raw[0])
    print("Age:",raw[1])
    print("Address:",raw[2])
    print("Phone:",raw[3])
while(1):    
    choice=input("""Python DB Menu
    1. Find customer
    2. Add customer
    3. Delete customer
    4. Update customer age
    5. Update customer address
    6. Update customer phone
    7. Print report
    8. Exit
    Select:""")
    if(choice=="1"):
        name=entername()
        request("find,"+name)
    if(choice=="2"):
        name= entername()
        age=enterage()
        add=input("Enter address:")
        ph=input("Enter phone:")
        if(ph==""):
            ph="\n"
        request("add,"+name+","+age+","+add+","+ph+",")
    if(choice=="3"):
        name=entername()
        request("delete,"+name)
    if(choice=="4"):
        name=entername()
        age=enterage()
        request("updateage,"+name+","+age+",")
    if(choice=="5"):
        name=entername()
        add=input("Enter address:")
        request("updateaddress,"+name+","+add+",")
    if(choice=="6"):
        name=entername()
        ph=input("Enter phone:")
        if(ph==""):
            ph="\n"
        request("updatephone,"+name+","+ph+",")
    if(choice=="7"):
        request("print"+",")    
    if(choice=="8"):
        print("Good bye!")
        break  

     