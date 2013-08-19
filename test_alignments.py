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
        assert out[1] == ['bananas', 'apples']
        assert len(out[1]) == 2

    def test_make_lexicon(self):
        fake_sentences = [['i', 'have', 'a', 'kiwi', '.'],
                          ['his', 'name', 'name', 'is', 'steve', '.'],
                          ['hacker', 'school', 'has', 'lots', 'of','people', ',', 'and', 'i', 'am', 'one', 'of', 'them','.']]
        fake_lex = {'i', 'have', 'a', 'kiwi','.','his','name','is','steve','hacker','school',
                    'has','lots','of','people','and','am','one','them',','}

        assert make_lexicon(fake_sentences) == fake_lex

    def test_initialization(self, T):
        comp = T['a']['h']
        for item1 in T.keys():
            for item2 in T[item1].keys():
                assert comp == T[item1][item2]
    
    @pytest.fixture
    def TCEETC(self):
        self.lex1 = {'a','b', 'c', 'd', 'e', 'f'}
        self.lex2 = {'g','h','i','j','k','l','m','n','o'}
        T = initialization_IMB1(lex1, lex2)
        return T

    def test_delta(self,T):
        sents1 =['f','a','b','c','d','e']
        sents2 =['h','h','h','g','k','k']

        assert delta(0, 0, 0, T, sents1, sents2) == 1.0/9
       
   # def test_count_generator(self, T)
