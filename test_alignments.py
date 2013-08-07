import pytest
from gen_alignment_matrix import *
'''What are the end goals here? Specifically for IBM 1
1. To initialize with all of the T values being the same. 
2. To compile a final T matrix after 5 iterations. Save in a file. OR CLASS??
3. Run on dev data and write spanish word corresponding to the highest t value for each english word as in the sample output
'''

def test_get_sents():
#Probably should do this with fake files because the given files could change at anytime.

    with file('ex.txt', 'w') as f:
        for i in xrange(100 ):
            f.write('bananas apples\n')

    out = get_sents('ex.txt')

    assert len(out) == 100
    assert out[1] == 'bananas apples\n'
    assert out[1].split()[1] == 'apples'
    assert len(out[1].split()) == 2

def test_make_lexicon():
    assert len(make_lexicon(get_sents('corpus.en'))) > 5401


'''def test_initialization():
#Will this take for fucking ever?
    eng_lex, spa_lex, T = initialization_IMB1()
    print len(eng_lex)
    print len(spa_lex)
    comp = T.values()[1]
    print comp
    #for item in T.keys:
        #assert comp == T[item]'''
 
