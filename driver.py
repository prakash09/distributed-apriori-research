import subprocess
from threading import Thread
import json
import socket
import os
import time
from collections import defaultdict
def main():
    os.chdir("/home/prakash/")
    os.system("pwd")
    os.system("./exe.sh")
    subprocess.call(["cd","/home/prakash","./exe.sh"], shell=True)
    idpass=[ "lalit@10.0.0.22"  ]
    for i in idpass:
        
        subprocess.call(["ssh",i,"./exe.sh"])
def socketconnection():
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('10.0.0.21', 8089))
        serversocket.listen(5) # become a server socket, maximum 5 connections
    except:
        print "Connection is already open"
    count=1
    while count<3:
        connection, address = serversocket.accept()
        buf = connection.recv(4096)
        if len(buf) > 0:
                data_loaded = json.loads(buf)
                print connection
                if address[0]=='10.0.0.21':
                        node1=data_loaded
			obj1=connection
                        node1=eval(node1)
                        print node1
                        #for x in node1.keys():
                         #   print "Key:", x, "-->", node1[x]
                if address[0]=='10.0.0.22':
                        node2=data_loaded
			obj2=connection
                        node2= eval(node2)
                        print node2
                #print data_loaded
               # data_loaded=list(data_loaded)
                        #for x in node2.keys():
                         #       print "key:",x, "-->",node2[x]
        count=count+1
    serverdict={}
    node1=defaultdict(lambda: 0.0, node1)
    #node2=defaultdict(lambda: 0.0, node2)
    allkeys=[]
    for x in node1.keys():
        allkeys.append(x)
    #for x in node2.keys():
     #   allkeys.append(x)
    allkeys=set(allkeys)


    for x in allkeys:
        #temp=(node1[x] + node2[x])/2
        temp=node1[x]
        if (temp > 0.05):
                serverdict[x]=temp
    serverfinaldata=json.dumps(str(serverdict))
    print address[1]
    
    obj1.send(serverfinaldata)
    obj2.send(serverfinaldata)


    for x in serverdict.keys():
        print "Key:",x,"-->", serverdict[x]
    print len(set(node1))
    #print len(set(node2))
    print len(set(serverdict.keys()))
    #print len(set(node1.keys()) & set(node2.keys()))    

if __name__=="__main__":
    t=Thread(target=socketconnection)
    t1=Thread(target=main)
    t.start()
    time.sleep(1)
    t1.start()
