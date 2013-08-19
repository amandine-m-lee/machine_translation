import re

apos = re.compile(r"\'(\S)+")
period = re.compile(r"([A-Za-z0-9\-]){3,10}\.$")

corp = open('corpus.en')
lines = corp.readlines()
corp.close()

out = open('corpus_cleaned.en', 'w')

for l in lines:
    words = l.split()
    for i in xrange(len(words)):
        w = words[i]
        match_apos = apos.match(w)
        match_period = period.match(w)
        if match_apos and len(w) > 2:
            print w
            words[i] = "' " + w[1:]
        if match_period:
            print w
            words[i] = w[:-1] + ' .'
    out.write(' '.join(words) + '\n')
