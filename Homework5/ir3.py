#############################################################################################################
### Mark Norgren
### SEIS731 Fall 2011
### Homework 5
#############################################################################################################
import re, math

# Debug flag: True=print intermediate data structures
DEBUG = False
DEBUG_LEVEL_2 = False

# hardcoded (for simplicity) tuple of documents to index
documents = ('D1.txt','D2.txt','D3.txt')

index={}    # dictionary key: (document, term), value: frequencies/weights
maxterm={}  # dictionary key: document, value: maximum number of time any term appears
docfreq={}  # dictionary key: term, value: number of documents term appears in
queryWeights={}
vocab=[]
vocabSet = set()


def add_weights_to_query():
    global queryWeights
    for ( term ) in sorted( queryWeights.keys() ):
        #idf=log base 2[(totalNumberofDocs)/(numberOfDocumentsContainingTerm)]
        if (docfreq.has_key(term)): 
            termfreq = float(docfreq[term])
        else:
            termfreq = 0.5
        inverse_document_frequency = math.log( (float(len(documents)) / termfreq),2)
        if DEBUG_LEVEL_2:
            print 'IDF====total#ofDocs:%d, term:%s, docfreq:%s, inverseDocumentFreq:%f' % \
                (len(documents), term, index[ ( document, term ) ],inverse_document_frequency)
        queryWeights[term] = round(inverse_document_frequency,2)


def add_Term_Weights(the_index):
    for ( document, term ) in sorted( index.keys() ):
        #tf=(termCountInADocument/largestTermCountInADocument)
        largest_term_count_in_a_document = maxterm[max(maxterm, key=maxterm.get)]
        term_frequency = float( float(index[ ( document, term ) ]) / float(largest_term_count_in_a_document) ) 
        if DEBUG_LEVEL_2:
            print 'TF====doc:%s, term:%s, docfreq:%s, largestTermCountInADoc:%d, termFreq:%f' % \
            (document, term, index[ ( document, term ) ],largest_term_count_in_a_document, term_frequency)
    
        #idf=log base 2[(totalNumberofDocs)/(numberOfDocumentsContainingTerm)]
        inverse_document_frequency = math.log( float(len(documents)) / float(docfreq[term]), 2 )
        if DEBUG_LEVEL_2:
            print 'IDF====total#ofDocs:%d, term:%s, docfreq:%s, inverseDocumentFreq:%f' % \
            (len(documents), term, index[ ( document, term ) ],inverse_document_frequency)

        term_weight = round((term_frequency * inverse_document_frequency), 2)
        if DEBUG_LEVEL_2:
            print 'term:%s ---- TERM_WEIGHT=%f' % \
            (term, term_weight)
            print '\n'
        the_index[document,term] = term_weight
        
def docFreqCount():
    global vocabSet
    numberOfDocsContainingTerm = 0
    for doc in documents:
        for term in vocabSet:
            if( index.has_key( (doc, term) ) ):
                if not docfreq.has_key( term.lower() ):
                    docfreq[term.lower()] = 1
                else:
                    docfreq[term.lower()] += 1


for document in documents:
    if not maxterm.has_key( ( document) ):
        maxterm[ document ] = 0
    for line in open( document, 'r'):
        terms = re.split('\W+', line)
        for term in terms:
            if term != '':      # Ignore null results from split at start/end of line
                vocab.append(term.lower())
                if not index.has_key( ( document, term.lower() ) ):
                    index[ ( document, term.lower() ) ] = 0
                index[ ( document, term.lower() ) ] += 1
                # check if this is the highest maxterm found in document
                if ( index[ ( document, term.lower() ) ] > maxterm[ document ]):
                    maxterm[ document ] = index[ ( document, term.lower() ) ]

#create a vocabSet which removes duplicates
#used to count term frequecncies in docs                    
vocabSet = set(vocab)
docFreqCount()
                    
if DEBUG:
    print '\nRaw term count:'
    for ( document, term ) in sorted( index.keys() ):
        print document, term, index[ ( document, term ) ]
                    
                    
add_Term_Weights(index)

if DEBUG:
    print '\nMaxterm Dict:'
    for ( doc ) in sorted( maxterm ):
        print doc, maxterm[ (doc) ]
    print '\nDocFreq:'
    for ( term ) in sorted( docfreq ):
        print term, docfreq[ ( term ) ]
    print max(maxterm)
    #get maxterm in all docs
    print maxterm[max(maxterm, key=maxterm.get)]
    print '\nTerm Weights:\n'
    for ( document, term ) in sorted( index.keys() ):
        print document, term, index[ ( document, term ) ]


while True:
    querystring = raw_input( '\nEnter query (q to quit): ' ) 
    queryWeights = {}
    if querystring == 'q':
        #print '\nGoodbye!\n'
        break
    terms = re.split('\W+', querystring)
    #print terms
    for term in terms:
        if term != '':      # Ignore null results from split at start/end of line
            if not queryWeights.has_key( ( term.lower() ) ):
                queryWeights[ ( term.lower() ) ] = 0
    #print queryWeights
    add_weights_to_query()
    #print queryWeights

    queryDocSimilarity={} # dictionary key: document value:similarity
    dotProduct = 0.0
    docLength = 0.0
    queryLength = 0.0
    for document in documents:
        queryDocLength = 0
        dotProduct = 0.0
        docLength = 0.0
        queryLength = 0.0
        for aTerm in vocabSet:
            if index.has_key( (document,aTerm) ):
                docLength += pow(index[document,aTerm],2)
        #print 'DocLength: ' + str(docLength)
        for term in queryWeights:
            if index.has_key( (document,term) ):
                product = index[document,term] * queryWeights[term]
                
            else:
                product = 0
            queryLength += pow(queryWeights[term],2)
            dotProduct += product
        #print 'Query Length: ' + str(queryLength)     
        queryDocLength =( math.sqrt(queryLength) * math.sqrt(docLength) )
        #print document + ': ' + str(queryDocLength)
        queryDocSimilarity[document] = round( (dotProduct / queryDocLength ),2 )
    
    from operator import itemgetter    
    items = queryDocSimilarity.items()
    items.sort( key = itemgetter(1), reverse=True )
    for (document, ranking) in items:
        print document, "%.2f" % ranking
'''
    print queryDocSimilarity
    for ( document ) in sorted( queryDocSimilarity.keys() ):
        print document, queryDocSimilarity[ document ] 
'''
    


