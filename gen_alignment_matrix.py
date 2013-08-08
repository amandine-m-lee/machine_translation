from collections import defaultdict

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
        for spa in spa_lex:
            print eng, spa
            T[eng][spa] =1.0/len(eng_lex)

    return T
#k is the sentence pair index. i is the foreign word index. j is the english word index. Gotta search over every english word and add up the probaiblities of the foreign word being translated from that english word. 

def delta(k, i, j, T, engs, spas):
    spa_word = spas[k][i]
    eng_word = engs[k][j]
    num = T[eng_word][spa_word]
    denom = sum(T[eng_word].values())
    return num/denom


#So the formula puts the t in terms of t(f|e), but it's c(e_j^(k), f_i^(k)) 
def gen_expected_counts(C_SE, C_E, T, eng_sents, spa_sents):
#These dictionaries are actually immutable
    for k in xrange(len(eng_sents)):
        for wi in spa_sents[k]:
            for wj in eng_sents[k]: 
                C_SE[wj][wi] = C_SE[wj] + delta(k, i, j, T, eng_sents, spa_sents)
                C_E[wj] = C_E[wj] + delta(k, i, j, T, eng_sents, spa_sents)


def update_t(eng_lex, spa_lex, T):
    for eword in eng_lex:
        for sword in spa_lex:
            T[eword][sword] = c_s_given_e(eword, sword)/c_e(eword)
   #I need to do this for ALL possible foreign and english words? So I probably want to compile all of the words, and then go through both initializing parameters in a giant for loop/dict comprehension


def iterate_EM_algo(niters, T, eng_sents, spa_sents, eng_lex, spa_lex):

    C_E = defaultdict(float)
    C_SE = defaultdict(float)


    for i in xrange(niters):
        gen_expected_counts(C_SE, C_E, T, eng_sents, spa_sents)
        update_t(eng_lex, spa_lex, T)

'''Looks like we should put the dev analysis and printing in a different file or class'''

#Probably we want a way to figure out how many iterations is enough. 

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

