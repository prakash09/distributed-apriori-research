import subprocess
#from pssh import ParallelSSHClient
import struct
from threading import Thread
import json
import socket
import os
import time
from collections import defaultdict
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
#import profile

#import pdb
def send_msg(sock, msg):
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)
def recv_msg(sock):
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recvall(sock, msglen)
def recvall(sock, n):
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
udpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udpsock.bind(('10.0.0.21',8090))
udpsock.listen(20)

@timing
def udpreceive():
        #data, address = udpsock.recvfrom(4096)
        connection, address = udpsock.accept()
	data=recv_msg(connection)
        #print "udpdata coming from", address[0]
        data=json.loads(data)
        data=eval(data)
        print "udpdata length=", len(data), data
        return data
global_server_dictionary=dict()
@timing
def computation(node, obj,connection_no):
        serverdict={}
        allkeys=[]
        stardict=[]
        infrequent=[]
        data_from_client=[]
        n=len(node)
        for i in xrange(n):
                node[i]=defaultdict(lambda: 0, node[i])
                stardict.append({})
                #allkeys=[x for x in node[i].keys() ]
        for i in xrange(n):
            for x in node[i].keys():
                allkeys.append(x)
        #if allkeys:
        #    length=len(allkeys[0])
        #else:
        #    length=0
        allkeys=set(allkeys)
       
        for x in allkeys:
            average=0
            if(len(x)==connection_no):
                for i in xrange(n):
                        average+=node[i][x]
                temp[connection_no][x]=average/n
                if (temp[connection_no][x] >= 0.05):
                        serverdict[x]=temp[connection_no][x]
                elif(connection_no>1):
                        for i in xrange(n):
                            if(node[i][x]==0):
                                stardict[i][x]=0
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
            for x in infrequent:
                x=set(x)
                for y in serverdict.keys():
                    if (set.intersection(x, y)==x):
                        del serverdict[y]
                for i in xrange(n):
                    for z in stardict[i].keys():
                        if (set.intersection(x,z)==x):
                            del stardict[i][z]

      
        if(connection_no>1):
            temp2=defaultdict(int)
            for i in xrange(n):
                stardict[i]=json.dumps(str(stardict[i]))
                send_msg(obj[i], stardict[i])
            data_from_client=[udpreceive() for i in xrange(n)]
            for i in xrange(n):
                for x in data_from_client[i].keys():
                    if temp2[x]==0 :
                        temp2[x]=temp[connection_no][x] + (data_from_client[i][x])/n
                    else:
                        temp2[x]+=(data_from_client[i][x])/n
                    if temp2[x] >= 0.05:
                            serverdict[x]=temp2[x]
        global_server_dictionary[connection_no]=serverdict
        print "global dictionary when connection number is ", connection_no
        print global_server_dictionary
        serverdict1=json.dumps(str(serverdict))
        for i in xrange(n):
                send_msg(obj[i], serverdict1)
        return None
def connecting(i):
    subprocess.call(["ssh",i,"./exe.sh"])
    return None
@timing
def main():
    os.chdir("/home/prakash/")
    os.system("pwd")
    os.system("./exe.sh")
    subprocess.call(["cd","/home/prakash","./exe.sh"], shell=True)
    idpass=[ "mamta@10.0.0.23",  "lalit@10.0.0.22" ]
    #client=ParallelSSHClient(idpass)
    #client.run_command('./exe.sh', sudo=True)
    for i in idpass:
        th=Thread(target=connecting,args=(i,))
        th.start()
        #subprocess.call(["ssh",i,"./exe.sh"])
    return None

temp=AutoVivification()
@timing
def socketconnection():
    connection_no=0
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('10.0.0.21', 8089))
        serversocket.listen(20) # become a server socket, maximum 5 connections
    except:
        print "Connection is already open"
    count=0
    total_node=3
    node=[]
    obj=[]
    while 1:
        connection, address = serversocket.accept()
        buf1=recv_msg(connection)
        print "after RECEIVE"
        #if len(buf1) > 0:
        data_loaded = json.loads(buf1)
        print "data coming from ", address[0]
        node.append(eval(data_loaded))
        obj.append(connection)
        print eval(data_loaded)
        count=count+1
        check=0
        if count==total_node:
                for i in xrange(count):
                    try:
                        if(len(node[i].keys())>0):
                            check=1
                            break
                    except:
                            break
                if check==0:
                   # print "abc"
                    
                    break
                    #print "def"
                connection_no=connection_no+1
                computation(node[:], obj[:],connection_no)
               # profile.run('computation')
                node[:]=[]
                obj[:]=[]
                count=0
                
    #serversocket.close()
    #udpsock.close()
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
