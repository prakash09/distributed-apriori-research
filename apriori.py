"""
Description     : Simple Python implementation of the Apriori Algorithm

Usage:
    $python apriori.py -f DATASET.csv -s minSupport  -c minConfidence

    $python apriori.py -f DATASET.csv -s 0.15 -c 0.6
"""
import struct
import socket
import json
import sys
import pdb
from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser
import time
def starResove(x, largeSet, k):
    print " I am inside star resolve"
    subset= set(combinations(x,k-1))
    temp=1
    pdb.set_trace()
    for y in subset:
        if (y in largeSet[k-1]):
			if largeSet[k-1][y]< temp:
				temp=largeSet[k-1][y]
    return temp
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
def subsets(arr):
    print "I am inside subsets"
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet,k):
	print "I am inside returnItemsWithMinSupport"
        """calculates the support for items in the itemSet and returns a subset
       of the itemSet each of whose elements satisfies the minimum support"""
        _itemSet = {}
        localSet = defaultdict(int)

        for item in itemSet:
                for transaction in transactionList:
                        if item.issubset(transaction):
                                freqSet[item] += 1
                                localSet[item] += 1

        for item, count in localSet.items():
                support = float(count)/len(transactionList)
		_itemSet[item]=support
        return _itemSet


def joinSet(itemSet, length):
	print "I am inside joinSet"
        """Join a set with itself and returns the n-element itemsets"""
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator):
    print "I am inside getItemSetTransactionList"
    transactionList = list()
    itemSet = set()
    for record in data_iterator: #yield object data_iterator
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))              # Generate 1-itemSets
    return itemSet, transactionList

largeSet = dict()
def runApriori(data_iter, minSupport, minConfidence): #first line in splitted
													   #form is saved in

										  # data_iter
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    print "i am inside runApriori"
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)

    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules
    k=1
    oneCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet,k)
    largeSet[k] = oneCSet
    oneLFS=set()
    for x in oneCSet.keys():
		if(oneCSet[x]>=minSupport):
			oneLFS.add(x)
    clientsocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('10.0.0.21', 8089))
    oneCSet=json.dumps(str(oneCSet))
    send_msg(clientsocket, oneCSet)

    data=recv_msg(clientsocket)

    if data:
    	data=json.loads(data)
    	data=eval(data)
    	print data
    clientsocket.close()
    oneGFS=set()
    for x in data.keys():
		oneGFS.add(x)
    currentLSet=set.intersection(oneGFS, oneLFS)
    k = 2
    PreScan=set()#
    while True:

        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet,transactionList,minSupport,freqSet,k)
        prescan=returnItemsWithMinSupport(PreScan,transactionList,minSupport,freqSet,k)#
        k_LFS={}

        print prescan
        PreScan=currentLSet
        for x in currentCSet.keys():
            if(currentCSet[x]>=minSupport):
                k_LFS[x]=currentCSet[x]
	# add prescan with k_LFS to send it to server
	    k_LFS=dict(k_LFS.items()+prescan.items())#
        clients= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clients.connect(('10.0.0.21', 8089))
        oneCSet=json.dumps(str(k_LFS))
        send_msg(clients, oneCSet)

        data=recv_msg(clients)

    	if data:
    		data=json.loads(data)
	    	data=eval(data)
	    	print data

        for x in data.keys():
		          if x in currentCSet:
			                   data[x]=currentCSet[x]
		          else:
			                   data[x]=starResove(x,largeSet,k)
	#we need to resolve star in between these two lines
        clientsocket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data=json.dumps(str(data))
        clientsocket.sendto(str(data),('10.0.0.21',8090))
        data=recv_msg(clients)
        #data=clients.recv(4096)
        if data:
    		data=json.loads(data)
    		data=eval(data)
    		print data
        clients.close()
        k_GFS=set()
        for x in data.keys():
        	k_GFS.add(x)
        PreScan= k_GFS.difference(PreScan) #
        print "lalit"
        print PreScan
        print "Goyal"
        currentLSet = set([ x for x in k_LFS.keys()])
        currentLSet=set.intersection(k_GFS, currentLSet)

        largeSet[k] = currentCSet
        k = k + 1
        if(not currentLSet and not PreScan):
            break

    def getSupport(item):
    	    print "I am inside getSupport function"
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item))
                           for item in value])

    toRetRules = []
    for key, value in largeSet.items()[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item)/getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)),
                                           confidence))
    return toRetItems, toRetRules


def printResults(items, rules):
    print "I am inside printResults function"
    """prints the generated itemsets and the confidence rules"""
    for item, support in items:
        print "item: %s , %.3f" % (str(item), support)
    print "\n------------------------ RULES:"
    for rule, confidence in rules:
        pre, post = rule
        print "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)


def dataFromFile(fname):
	print "I am inside dataFromFile"
        """Function which reads from the file and yields a generator"""
        file_iter = open(fname, 'rU')
        for line in file_iter:
                line = line.strip().rstrip(',')                         # Remove trailing comma
                record = frozenset(line.split())
                yield record


if __name__ == "__main__":
   # pdb.set_trace()
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing csv',
                         default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minS',
                         help='minimum support value',
                         default=0.05,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minC',
                         help='minimum confidence value',
                         default=0.06,
                         type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
            inFile = sys.stdin
    elif options.input is not None:
            inFile = dataFromFile(options.input)
    else:
            print 'No dataset filename specified, system with exit\n'
            sys.exit('System will exit')

    minSupport = options.minS
    minConfidence = options.minC

    items, rules = runApriori(inFile, minSupport, minConfidence)

    printResults(items, rules)
