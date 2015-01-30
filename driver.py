import subprocess
import struct
from threading import Thread
import json
import socket
import os
import time
from collections import defaultdict
import pdb
c_c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_c.bind(('10.0.0.21', 8080))
c_c.listen(20)

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
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
global_server_dictionary=dict()
@timing
def c2c(obj1):
   
    return None




    
def computation(node, obj,connection_no):
        serverdict={}
        allkeys=[]
        n=len(node)
        for i in xrange(n):
                node[i]=defaultdict(lambda: 0, node[i])
        for i in xrange(n):
                for x in node[i].keys():
                        allkeys.append(x)
        allkeys=set(allkeys)
        print "length of all keys", len(allkeys),"\n", allkeys
        for x in allkeys:
            average=0
           # if(len(x)==connection_no):
            for i in xrange(n):
                    average+=node[i][x]
            temp[connection_no][x]=average/n
            if (temp[connection_no][x] > 0.05):
                    serverdict[x]=temp[connection_no][x]
        global_server_dictionary[connection_no]=serverdict
        print "global dictionary when connection number is ", connection_no
        print global_server_dictionary
        serverdict1=json.dumps(str(serverdict))
        for i in xrange(n):
                send_msg(obj[i], serverdict1)
        obj1=[]
        data=[]
        for i in xrange(3):

            connection, address = c_c.accept()
            print "data is coming from ", address[0]
            buf=recv_msg(connection)
            obj1.append(connection)
            data.append(buf)

    
        for i in xrange(3):
            for j in xrange(3):
                send_msg(obj1[i],data[j])
        return None
def connecting(i):
    subprocess.call(["ssh", i, "./exe.sh"])
@timing
def main():
    os.chdir("/home/prakash/")
    os.system("pwd")
    os.system("./exe.sh")
    subprocess.call(["cd","/home/prakash","./exe.sh"], shell=True)
    idpass=[ "lalit@10.0.0.22" , "mamta@10.0.0.23" ]
    for i in idpass:
        tx=Thread(target=connecting, args=(i,))
        tx.start()
        #subprocess.call(["ssh",i,"./exe.sh"])
temp=AutoVivification()
@timing
def socketconnection():
    connection_no=0
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('10.0.0.21', 8089))
        serversocket.listen(20)
    except:
        print "Connection is already open"
    count=0
    total_node=3 #int(raw_input("Enter the total number of computers"))
    node=[]
    obj=[]
    while 1:
        connection, address = serversocket.accept()
        buf1=recv_msg(connection)
        print "after RECEIVE"
        if len(buf1) > 0:
                data_loaded = json.loads(buf1)
                print "data coming from ", address[0]
                node.append(eval(data_loaded))
                obj.append(connection)
                print eval(data_loaded)
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
    print "the total runtime=", time.time()-start_time
    return None
start_time=0
if __name__=="__main__":
    start_time=time.time()
    t=Thread(target=socketconnection)
    t1=Thread(target=main)
    t.start()
    time.sleep(1)
    t1.start()
