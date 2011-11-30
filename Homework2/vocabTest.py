vocab = open('vocabulary.txt', 'rb')

v = vocab.readlines()
print v
#vocab = []
vx = []
for x in v:
    vx.append(x.rstrip())
    
print 'Vocab Length: %d' % len(vx)
print vx

vocab.close()