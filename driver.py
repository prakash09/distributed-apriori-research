import subprocess
import struct
from threading import Thread
import json
import socket
import os
import time
from collections import defaultdict
import pdb
import sys
def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)
def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)
def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = ''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data
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
        #print "udp is receiving data from", address[0]
        data=eval(data)
        return data
global_server_dictionary=dict()
def computation(node, obj,connection_no):
        serverdict={}
        allkeys=[]
        n=len(node)
        for i in xrange(n):
                node[i]=defaultdict(lambda: 0, node[i])
        for i in xrange(n):
                for x in node[i].keys():
                        allkeys.append(x)
                
        #node2=defaultdict(lambda: 0, node2)
        #allkeys=[]
        #for x in node1.keys():
         #   allkeys.append(x)
        #for x in node2.keys():
         #  allkeys.append(x)
        if allkeys:
            length=len(allkeys[0])
        else:
            length=0
        allkeys=set(allkeys)
        print "length of all keys", len(allkeys),"\n", allkeys
        stardict=[]
        #stardict2={}
        infrequent=[]
        data_from_client=[]
        for i in xrange(n):
            stardict.append({})
        for x in allkeys:
            average=0
            if(len(x)==connection_no):
                for i in xrange(n):
                        average+=node[i][x]
                temp[connection_no][x]=average/n
                if (temp[connection_no][x] > 0.05):
                        serverdict[x]=temp[connection_no][x]
                elif(length!=1):
                        for i in xrange(n):
                            if(node[i][x]==0):
                                stardict[i][x]=0
                                
                ''''elif(node1[x]==0 and length!=1 for ):
                    stardict1[x]=0
                elif(node2[x]==0 and length!=1):
                    stardict2[x]=0'''
            else:
                    average=0
                    for i in xrange(n):
                        average+=node[i][x]
                    temp[connection_no-1][x]=temp[connection_no-1][x]+average/n
                    if (temp[connection_no-1][x]<0.05):
                        del global_server_dictionary[connection_no-1][x]
                  #      print "self deletion", x
                        infrequent.append(x)
        if connection_no>2:
            #pdb.set_trace()
            for x in infrequent:
                x=set(x)
                for y in serverdict.keys():
                    if (set.intersection(x, y)==x):
                   #     print "serverdict", y
                        del serverdict[y]
            #pdb.set_trace()
            for i in xrange(n):
                for x in infrequent:
                    x=set(x)
                    for y in stardict[i].keys():
                        if (set.intersection(x, y)==x):
                           # print "stardict", y
                            del stardict[i][y]
        ''' pdb.set_trace()
            for x in infrequent:
                x=set(x)
                for y in stardict2.keys():
                    if (set.intersection(x, y)==x):
                        print "stardict2", y
                        del stardict2[y] '''
        if(length!=1):
            for i in xrange(n):
                stardict[i]=json.dumps(str(stardict[i]))
                send_msg(obj[i], stardict[i])
            #stardict2=json.dumps(str(stardict2))
            #send_msg(obj2, stardict2)
            #tcpsend(obj1,stardict1)
            #tcpsend(obj2, stardict2)
            for i in xrange(n):
                data_from_client.append(udpreceive())
            #print "data from prakash", data_from_client1
            #data_from_client2=udpreceive()
            #print "data from lalit sir", data_from_client2
            for i in xrange(n):
                for x in data_from_client[i].keys():
                        temp2=temp[connection_no][x]+(data_from_client[i][x])/2
                        if temp2 > 0.05:
                                serverdict[x]=temp2
            '''for x in data_from_client2.keys():
                temp2=temp[connection_no][x]+(data_from_client2[x])/2
                if(temp2 > 0.05):
                    serverdict[x]=temp2'''
        #udpsock.sendto(str("hello world"), ('10.0.0.22',5850))
        global_server_dictionary[connection_no]=serverdict
        print "global dictionary when connection number is ", connection_no
        print global_server_dictionary
        serverdict1=json.dumps(str(serverdict))
        #pdb.set_trace()
        for i in xrange(n):
                send_msg(obj[i], serverdict1)
        return None
     
'''def tcpsend(obj,sdata):
        sdata=json.dumps(str(sdata))
        print "sending data to",obj
        obj.sendall(sdata)
        return
'''
def main():
    os.chdir("/home/prakash/")
    os.system("pwd")
    os.system("./exe.sh")
    subprocess.call(["cd","/home/prakash","./exe.sh"], shell=True)
    idpass=[ "lalit@10.0.0.22"  ]
    for i in idpass:
        subprocess.call(["ssh",i,"./exe.sh"])
    return None
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
    total_node=2 #int(raw_input("Enter the total number of computers"))
    node=[]
    obj=[]
    
    while 1:
       
        connection, address = serversocket.accept()
        buf1=recv_msg(connection)
        #buf1 = connection.recv(4096)
        print "after RECEIVE"
        if len(buf1) > 0:
                data_loaded = json.loads(buf1)
                #if address[0]=='10.0.0.21':
                print "data coming from ", address[0]
                node.append(eval(data_loaded))
                obj.append(connection)
                print eval(data_loaded)
                #node1=eval(node1)
                #print "I am object", node1
                #print len(node1)
                #for x in node1.keys():
                #   print "Key:", x, "-->", node1[x]
            #if address[0]=='10.0.0.22':
             #           print "data coming from ", address[0]
              #          node2=data_loaded
              #          obj2=connection
               #         node2= eval(node2)
                        #print "I am object2", node2
                        #print len(node2)
                #print data_loaded
            # data_loaded=list(data_loaded)
                        #for x in node2.keys():
                        #       print "key:",x, "-->",node2[x]
        count=count+1
        check=0
        if count==total_node:
                for i in xrange(count):
                    if(len(node[i].keys())>0):
                        check=1
                

                connection_no=connection_no+1
                computation(node[:], obj[:],connection_no)
                node[:]=[]
                obj[:]=[]
                count=0
                if check==0: 
                    break
    print "total time in execution =", time.time()-start_time
    return None
start_time=0
if __name__=="__main__":
    start_time=time.time()
    t=Thread(target=socketconnection)
    t1=Thread(target=main)
    t.start()
    time.sleep(1)
    t1.start()
