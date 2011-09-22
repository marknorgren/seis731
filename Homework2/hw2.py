import math
import string
import csv
from collections import Counter
from collections import OrderedDict

d1 = open('d1.txt', 'rb')
d2 = open('d2.txt', 'rb')
d3 = open('d3.txt', 'rb')
vocab = open('vocabulary.txt', 'rb')
totalNumberOfDocs = 3
#print d1
#print d2
#print d3

d1WordList = d1.readlines().pop().rsplit()
d2WordList = d2.readlines().pop().rsplit()
d3WordList = d3.readlines().pop().rsplit()
#vocabulary = vocab.readlines().pop().rsplit()
docsContainingTerm_dict = OrderedDict()
v = vocab.readlines()
print v
vocab = []
for x in v:
    vocab.append(x.rstrip())

print 'Vocab Length: %d' % len(vocab)
print vocab

my_dict = zip(vocab, d1WordList)
print my_dict

docList = [d1WordList, d2WordList, d3WordList]

print '\n**************************************'
for d in docList:
    print d

#convert all terms to lowercase
docListLowerCase = []
for d in docList:
    docListLowerCase.append([s.lower() for s in d])
    docList = docListLowerCase

print '\n**************************************'
for d in docList:
    print d

#remove punctuation
docListNoPunctuation = []
for d in docList:
    docListNoPunctuation.append([s.translate(None, string.punctuation) for s in d])    
    docList = docListNoPunctuation

print '\n**************************************'
for d in docList:
    print d

######################################################################################
## FUNCTIONS
######################################################################################
def fillTermDict():
    global docsContainingTerm_dict
    for word in vocab:
        docsContainingTerm_dict[word] = 0
    #print docsContainingTerm_dict

def docsContainingTerm():
    global docsContainingTerm_dict
    for doc in docList:
        for word in doc:
            docsContainingTerm_dict[word] +=1
    #print docsContainingTerm_dict
    
largestTermCountInADocument = float(0)
def largestTermCountInADocument(docList):
    global largestTermCountInADocument
    maxTermCount = 0
    for x in docList:
        thisMaxTuple = Counter(x).most_common(1).pop()[1]
        if (thisMaxTuple>maxTermCount):
            maxTermCount = thisMaxTuple
    largestTermCountInADocument = float(maxTermCount)
    #print str(largestTermCountInADocument)

# term fequency
# (term count in a document/largest term count in a document)
def termFrequency(wordList, term):
    termCount = wordList.count(term)
    maxTuple = Counter(wordList).most_common(1).pop()[1]
    return (float(termCount)/float(maxTuple))

#inverse document frequency
def inverseDocumentFrequency(term):
    global docList
    global d1WordList
    global d2WordList
    global d3WordList
    global totalNumberOfDocs
    d1ContainsTerm = False
    d2ContainsTerm = False
    d3ContainsTerm = False
    numberOfDocsContainingTerm = 0
    if(docList[0].count(term) > 0):
        d1ContainsTerm = True
        numberOfDocsContainingTerm+=1
    if(docList[1].count(term) > 0):
        d2ContainsTerm = True
        numberOfDocsContainingTerm+=1
    if(docList[2].count(term) > 0):
        d3ContainsTerm = True
        numberOfDocsContainingTerm+=1
    idf = math.log((float(totalNumberOfDocs)/float(numberOfDocsContainingTerm)),2)
    return idf

def term_weight(twWordList, twTerm):
    tf = termFrequency(twWordList, twTerm)
    idf = inverseDocumentFrequency(twTerm)
    print '  tf: %f' % float(tf)
    print '  idf: %f' % float(idf)
    return round((tf * idf), 2)

def dot_product(list1, list2):
    dot_product_result = 0.0
    for index, obj in enumerate(list1):
        print str(list1[index]) + '  :  ' + str(list2[index])
        dot_product_result += (list1[index] * list2[index])
    return dot_product_result
    
######################################################################################
## INITIALIZATION
######################################################################################
largestTermCountInADocument(docList)


#open csv file
f = open('csv.txt', 'wt')
#create writer to output to csv
writer = csv.writer(f)
#header row for csv file
writer.writerow(['Doc Name'] + vocab)


query = [0,.58,1.58,0,0,0,0,0,0,0,0,0,0,.58,0,0,0,0,0,1.58]

fillTermDict()
docsContainingTerm()

for index, d in enumerate(docList):
    #going through each document (i.e. - doc1, doc2, doc3)
    print 'Document ' + str(index+1)
    my_dict = OrderedDict()
    for w in vocab:
        if w in d:
            print '  Term: ' + w
            _term_weight = term_weight(d, w)
            my_dict[w] = _term_weight
        else:
            my_dict[w] = 0
        print '    TermWeight: %f' % _term_weight
    docName = 'Doc: ' + str(index)
    writer.writerow([docName] + my_dict.values())
    #print my_dict
    #print my_dict.values()
    print 'DotProductResult: ' + str(dot_product(query, my_dict.values()))



f.close()
d1.close()
d2.close()
d3.close()