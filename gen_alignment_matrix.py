from collections import defaultdict
import json

"""OFFICIAL STYLE: English, Spanish"""
'''Output looks like: 
    SentenceIndex EnglishIndex ForeignIndex'''
'''Let's start with some global variables and pure functions'''


'''Initialization methods'''
def get_sents(filename):
    with open(filename) as f:
        lines = f.readlines()
        return[line.split() for line in lines]

def make_lexicon(sentences):
    lex = set()
    for sent in sentences:
        for word in sent:
            lex.add(word)
    return lex

def initialization_IMB1(eng_lex, spa_lex):
    T = defaultdict(dict)
    eng_lex = list(eng_lex)
    spa_lex = list(spa_lex)
    eng_lex.sort()
    eng_lex.sort()
    for eng in eng_lex:
        print eng
        for spa in spa_lex:
            T[eng][spa] =1.0/len(eng_lex)

    return T
#k is the sentence pair index. i is the foreign word index. j is the english word index. Gotta search over every english word and add up the probaiblities of the foreign word being translated from that english word. 

def delta(k, i, j, T, engs, spas):

    spa_word = spas[k][i]
    eng_word = engs[k][j]
    num = T[eng_word][spa_word]
    denom = sum([T[eng][spa_word] in engs[k]])

    return num/denom


#So the formula puts the t in terms of t(f|e), but it's c(e_j^(k), f_i^(k)) 
def gen_expected_counts(C_SE, C_E, T, engs, spas):
#These dictionaries are actually immutable
    for k in xrange(len(engs)):
        print k
        for i in xrange(len(spas[k])):
            for j in xrange(len(engs[k])): 
                C_SE[engs[k][j]][spas[k][i]] = C_SE[engs[k][j]][spas[k][i]] +\
                        delta(k, i, j, T, eng_sents, spa_sents)
                C_E[engs[k][j]] = C_E[spas[k][i]] + delta(k, i, j, T, eng_sents, spa_sents)


def update_t(C_SE, C_E, eng_lex, spa_lex, T):
    for eword in eng_lex:
        print eword
        for sword in spa_lex:
            T[eword][sword] = C_SE(eword, sword)/C_E(eword)
   #I need to do this for ALL possible foreign and english words? So I probably want to compile all of the words, and then go through both initializing parameters in a giant for loop/dict comprehension


def iterate_EM_algo(niters, T, eng_sents, spa_sents, eng_lex, spa_lex):

    C_E = defaultdict(dict)
    C_SE = defaultdict(dict)

    for eword in eng_lex:
        print "c_e", eng_lex
        for sword in spa_lex:
            C_E[eword][sword] = 0
            C_SE[eword][sword] = 0


    for _ in xrange(niters):
        gen_expected_counts(C_SE, C_E, T, eng_sents, spa_sents)
        update_t(eng_lex, spa_lex, T)

def write_T_to_file(T, filename):
    with open(filename) as f:
        json.dumps(T, f)


'''Looks like we should put the dev analysis and printing in a different file or class'''

#Probability of generating a foreign word f (dest_word) from and english word e (source_word).
#Possibilities for constructions: tuples of (spa_word, eng_word):probability. or spa_word:{engword:prob}

'''So the things I need are a t, which keeps track of the probabilities of translating one word 
into another. Should this be a sparse matrix? Or is he referring to the alignment matrices? Maybe
let's just do another default dict for T'''

if __name__ == '__main__':
    
    english_file = 'corpus.en'
    spanish_file = 'corpus.es'
    eng_sents = get_sents(english_file)
    spa_sents = get_sents(spanish_file)
    eng_lex = make_lexicon(eng_sents)
    spa_lex = make_lexicon(spa_sents)

    T = initialization_IMB1(eng_lex, spa_lex)

    iterate_EM_algo(1, T, eng_sents, spa_sents, eng_lex, spa_lex)

    write_T_to_file(T, 'T.json')

