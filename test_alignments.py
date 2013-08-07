import pytest
from gen_alignment_matrix import *
'''What are the end goals here? Specifically for IBM 1
1. To initialize with all of the T values being the same. 
2. To compile a final T matrix after 5 iterations. Save in a file. OR CLASS??
3. Run on dev data and write spanish word corresponding to the highest t value for each english word as in the sample output
'''

class TestEM():

    def test_get_sents(self):
#Probably should do this with fake files because the given files could change at anytime.

        with file('ex.txt', 'w') as f:
            for i in xrange(100 ):
                f.write('bananas apples\n')

        out = get_sents('ex.txt')

        assert len(out) == 100
        assert out[1] == 'bananas apples\n'
        assert out[1].split()[1] == 'apples'
        assert len(out[1].split()) == 2

    def test_make_lexicon(self):
        fake_sentences = ['i have a kiwi .',
                          'his name name is steve .',
                          'hacker school has lots of people , and i am one of them .']
        fake_lex = {'i', 'have', 'a', 'kiwi','.','his','name','is','steve','hacker','school',
                    'has','lots','of','people','and','am','one','them',','}

        assert make_lexicon(fake_sentences) == fake_lex

    def test_initialization(self):
#Will this take for fucking ever?
        lex1 = {'a','b', 'c', 'd', 'e', 'f'}
        lex2 = {'g','h','i','j','k','l','m','n','o'}
        T = initialization_IMB1(lex1, lex2)
        comp = T.values()[0]
        for item in T.keys():
            assert comp == T[item]
        assert len(T) == 54
     
