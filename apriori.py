"""
Description     : Simple Python implementation of the Apriori Algorithm

Usage:
    $python apriori.py -f DATASET.csv -s minSupport  -c minConfidence

    $python apriori.py -f DATASET.csv -s 0.15 -c 0.6
"""
import socket
import json
import sys
#import pdb
from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser
import time

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
		if k==1 :
			_itemSet[item]=support
		else:
                	if support >= minSupport:
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
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules
    k=1
    oneCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet,k)
    oneLFS=set()
    for x in oneCSet.keys():
		if(oneCSet[x]>=minSupport):
			oneLFS.add(x)
    clientsocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('10.0.0.21', 8089))

    oneCSet=json.dumps(str(oneCSet))
    clientsocket.sendall(str(oneCSet))
    data=clientsocket.recv(10000)
    data=json.loads(data)
    data=eval(data)

    clientsocket.close()
    oneGFS=set()
    for x in data.keys():
		oneGFS.add(x)
    currentLSet=set.intersection(oneGFS, oneLFS)
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet,
                                                transactionList,
                                                minSupport,
                                                freqSet,k)
        clientsocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('10.0.0.21', 8089))

        oneCSet=json.dumps(str(currentCSet))
        clientsocket.sendall(str(oneCSet))
            #time.sleep(2)
        data=clientsocket.recv(10000)
        data=json.loads(data)
        data=eval(data)

        clientsocket.close()
        k_GFS=set()
        for x in data.keys():
        	k_GFS.add(x)


        currentLSet = set([ x for x in currentCSet.keys()])
        currentLSet=set.intersection(k_GFS, currentLSet)
        k = k + 1

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
