import math
import string
from collections import Counter

d1 = open('d1.txt', 'rb')
d2 = open('d2.txt', 'rb')
d3 = open('d3.txt', 'rb')
totalNumberOfDocs = 3
#print d1
#print d2
#print d3

d1WordList = d1.readlines().pop().rsplit()
d2WordList = d2.readlines().pop().rsplit()
d3WordList = d3.readlines().pop().rsplit()
docList = [d1WordList, d2WordList, d3WordList]
#convert all terms to lowercase
docListLowerCase = []
for d in docList:
    docListLowerCase.append([s.lower() for s in d])
    
docList = docListLowerCase
print docList[0]
print docList[1]
print docList[2]
# docList[0] = [x.lower() for x in docList[0]]
# docList[1] = [x.lower() for x in docList[1]]
# docList[2] = [x.lower() for x in docList[2]]
# print docList[0]
# print docList[1]
# print docList[2]


largestTermCountInADocument = float(0)
def largestTermCountInADocument(docList):
    global largestTermCountInADocument
    maxTermCount = 0
    for x in docList:
        thisMaxTuple = Counter(x).most_common(1).pop()[1]
        if (thisMaxTuple>maxTermCount):
            maxTermCount = thisMaxTuple
    largestTermCountInADocument = float(maxTermCount)
    print str(largestTermCountInADocument)
    
# term fequency
# (term count in a document/largest term count in a document)
def termFrequency(wordList, term):
    print '  termFreq'
    #global largestTermCountInADocument
    termCount = wordList.count(term)
    #print 'frequency in list: ' + str(termCount)
    maxTuple = Counter(wordList).most_common(1).pop()[1]
    print '    term Count: %d' % termCount
    print '    largest term count: ' + str(maxTuple)
    #print '    largestTermCount: %d' % largestTermCountInADocument
    #largestTermCount = max.pop()[1]
    #print 'termFreq'
    #print largestTermCountInADocument
    #return (float(termCount)/float(largestTermCountInADocument))
    return (float(termCount)/float(maxTuple))
    #print '\n'
    
#inverse document frequency
def inverseDocumentFrequency(term):
    global docList
    global d1WordList
    global d2WordList
    global d3WordList
    global totalNumberOfDocs
    #print 'numberOfDocs: %d' % totalNumberOfDocs
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
    #print d1ContainsTerm
    #print d2ContainsTerm 
    #print d3ContainsTerm
    print '  inveresDocumentFreq'
    print '    TotalNumberOfDocs %d' % totalNumberOfDocs
    print '    TotalDocsContainingTerm: %d' % numberOfDocsContainingTerm
    idf = math.log((float(totalNumberOfDocs)/float(numberOfDocsContainingTerm)),2)
    return idf
    #log(3, 2)

def termWeight(twWordList, twTerm):
    tf = termFrequency(twWordList, twTerm)
    idf = inverseDocumentFrequency(twTerm)
    print '      tf: %f' % float(tf)
    print '      idf: %f' % float(idf)
    return tf * idf
    




#print str(termFrequency(d1WordList, 'quick'))
#print str(termFrequency(d1WordList, 'brown'))
#inverseDocumentFrequency('quick')

#init
largestTermCountInADocument(docList)

#print 'TermWeight: %f' % termWeight(d1WordList, 'the')
#print '\n'
#print 'quick'
#print '  TermWeight: %f' % termWeight(d1WordList, 'quick')
#print '  TermWeight: %f' % termWeight(d2WordList, 'quick')
#print '  TermWeight: %f' % termWeight(d3WordList, 'quick')

print 'd1'
print '  the'
print '    TermWeight: %f' % termWeight(docList[0], 'the')
# print '  quick'
# print '    TermWeight: %f' % termWeight(d1WordList, 'quick')
# print '  brown'
# print '    TermWeight: %f' % termWeight(d1WordList, 'brown')
# print '  waltz'
# print '    TermWeight: %f' % termWeight(d1WordList, 'waltz')
# 
# print 'd2'
# print '  waltz'
# print '    TermWeight: %f' % termWeight(d2WordList, 'waltz')
# print '  nymph'
# print '    TermWeight: %f' % termWeight(d2WordList, 'nymph')
# print '  for'
# print '    TermWeight: %f' % termWeight(d2WordList, 'for')
# 
# print '  vex'
# print '    TermWeight: %f' % termWeight(d2WordList, 'vex')

d1.close()
d2.close()
d3.close()