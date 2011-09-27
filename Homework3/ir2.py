import re

# Debug flag: True=print intermediate data structures
DEBUG = True

# hardcoded (for simplicity) tuple of documents to index
documents = ('D1.txt','D2.txt','D3.txt')

index={}	# dictionary key: (document, term), value: frequencies/weights
for document in documents:
	for line in open( document, 'r'):
		terms = line.split()
		for term in terms:
			if term != '':		# Ignore null results from split at start/end of line
				if not index.has_key( ( document, term.lower() ) ):
					index[ ( document, term.lower() ) ] = 0
				index[ ( document, term.lower() ) ] += 1

if DEBUG:
	print '\nRaw term count:'
	for ( document, term ) in sorted( index.keys() ):
		print document, term, index[ ( document, term ) ]