import subprocess
import struct
from threading import Thread
import json
import socket
import os
import time
from collections import defaultdict
import pdb
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
udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsock.bind(('10.0.0.21',8090))
'''def udpreceive():
        data, address = udpsock.recvfrom(4096)
        data=json.loads(data)
        print "udp is receiving data from", address[0]
        data=eval(data)
        return data'''
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


        allkeys=set(allkeys)
        print "length of all keys", len(allkeys),"\n", allkeys


        for x in allkeys:
            average=0
            if(len(x)==connection_no):
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
        serversocket.listen(20)
    except:
        print "Connection is already open"
    count=0
    total_node=int(raw_input("Enter the total number of computers"))
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
        if count==total_node:
                connection_no=connection_no+1
                computation(node[:], obj[:],connection_no)
                node[:]=[]
                obj[:]=[]
                count=0
if __name__=="__main__":
    t=Thread(target=socketconnection)
    t1=Thread(target=main)
    t.start()
    time.sleep(1)
    t1.start()
