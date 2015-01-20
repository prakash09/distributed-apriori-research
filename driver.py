import subprocess
from threading import Thread
import json
import socket
import os
import time
from collections import defaultdict
class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsock.bind(('10.0.0.21',8090))
def udpreceive():
        data, address = udpsock.recvfrom(4096)
        data=json.loads(data)
        print "udp is receiving data from", address[0]
        data=eval(data)
        return data
def computation(node1, obj1, node2, obj2,connection_no):
        serverdict={}
        node1=defaultdict(lambda: 0, node1)
        node2=defaultdict(lambda: 0, node2)
        allkeys=[]
        for x in node1.keys():
            allkeys.append(x)
        for x in node2.keys():
           allkeys.append(x)
        length=len(allkeys[1])
        allkeys=set(allkeys)

        stardict1={}
        stardict2={}
        for x in allkeys:
                temp[connection_no][x]=(node1[x] + node2[x])/2
                if (temp[connection_no][x] > 0.05):
                        serverdict[x]=temp[connection_no][x]

                elif(node1[x]==0 and length!=1):
                    stardict1[x]=0
                elif(node2[x]==0 and length!=1):
                    stardict2[x]=0

        if(length!=1):
            tcpsend(obj1,stardict1)
            tcpsend(obj2, stardict2)
            data_from_client1=udpreceive()
            print "data from prakash", data_from_client1
            data_from_client2=udpreceive()
            print "data from lalit sir", data_from_client2
            for x in data_from_client1.keys():
                temp[connection_no][x]=temp[connection_no][x]+(data_from_client1[x])/2
                if temp[connection_no][x] > 0.05:
                        serverdict[x]=temp[connection_no][x]
            for x in data_from_client2.keys():
                temp[connection_no][x]=temp[connection_no][x]+(data_from_client2[x])/2
		if(temp[connection_no][x] > 0.05):
		        serverdict[x]=temp[connection_no][x]

        #udpsock.sendto(str("hello world"), ('10.0.0.22',5850))
        tcpsend(obj1, serverdict)
        tcpsend(obj2, serverdict)
        #obj1.send(serverfinaldata)
        #obj2.send(serverfinaldata)


        for x in serverdict.keys():
            print "Key:",x,"-->", serverdict[x]
        print len(set(node1))
        #print len(set(node2))
        print len(set(serverdict.keys()))
        #print len(set(node1.keys()) & set(node2.keys()))
def tcpsend(obj,sdata):
        sdata=json.dumps(str(sdata))
        print "sending data to",obj 
        obj.sendall(sdata)
        return

def main():
    os.chdir("/home/prakash/")
    os.system("pwd")
    os.system("./exe.sh")
    subprocess.call(["cd","/home/prakash","./exe.sh"], shell=True)
    idpass=[ "lalit@10.0.0.22"  ]
    for i in idpass:

        subprocess.call(["ssh",i,"./exe.sh"])
temp=AutoVivification()
def socketconnection():
    connection_no=0
    try:
       
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('10.0.0.21', 8089))
        serversocket.listen(20) # become a server socket, maximum 5 connections
    except:
        print "Connection is already open"
    count=0
    while 1:
        connection, address = serversocket.accept()
        buf1 = connection.recv(4096)
        print "after RECEIVE"
        

        if len(buf1) > 0:
                data_loaded = json.loads(buf1)
                if address[0]=='10.0.0.21':
                        print "data coming from ", address[0]
                        node1=data_loaded
                        obj1=connection
                        node1=eval(node1)
                        print "I am object", node1
                        #for x in node1.keys():
                        #   print "Key:", x, "-->", node1[x]
                if address[0]=='10.0.0.22':
                        print "data coming from ", address[0]
                        node2=data_loaded
                        obj2=connection
                        node2= eval(node2)
                        print "I am object2", node2
                #print data_loaded
            # data_loaded=list(data_loaded)
                        #for x in node2.keys():
                        #       print "key:",x, "-->",node2[x]
        count=count+1
        if count==2:
                connection_no=connection_no+1
                computation(node1, obj1, node2, obj2,connection_no)
                count=0

if __name__=="__main__":
    t=Thread(target=socketconnection)
    t1=Thread(target=main)
    t.start()
    time.sleep(1)
    t1.start()
