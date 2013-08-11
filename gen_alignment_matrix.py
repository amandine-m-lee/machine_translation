from collections import defaultdict
import json

"""OFFICIAL STYLE: English, Spanish"""
'''Output looks like: 
    SentenceIndex EnglishIndex ForeignIndex'''
'''Let's start with some global variables and pure functions'''


'''Initialization methods'''

    
class EMFromTest():
    
    def __init__(english_file, spanish_file, dbname):

        self.CON = sqlite3.connect(dbname)
        self.CUR = sqlite3.cursor()
        self.eng_sents = self.get_sents(english_file)
        self.spa_sents = self.get_sents(spanish_file)
        self.eng_lex = self.make_lexicon(eng_sents)
        self.spa_lex = self.make_lexicon(spa_sents)


    def get_sents(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            return[line.split() for line in lines]

    def make_lexicon(self, sentences):
        lex = set()
        for sent in sentences:
            for word in sent:
                lex.add(word)
        return lex

    def initialization_IMB1(self):
        eng_lex = list(self.eng_lex)
        spa_lex = list(self.spa_lex)
        eng_lex.sort()
        eng_lex.sort()
#Make these global variables probably 
        self.CUR.execute("CREATE TABLE t (English TEXT, Spanish TEXT, prob NUMERIC DEFAULT 0, \
                PRIMARY KEY (English, Spanish));")
        self.CUR.execute("CREATE TABLE cse (English TEXT, Spanish TEXT, counts NUMERIC DEFAULT 0, \
                PRIMARY KEY (English, Spanish));")
        self.CUR.execute("CREATE TEABLE ce (English TEXT PRIMARY KEY, coutns NUMERIC DEFAULT 0);")
        CON.commit()

        for eng in eng_lex:
            print eng
            for spa in spa_lex:
                insert_T(eng, spa, 1.0/len(eng_lex))
                insert_cse(eng, spa, 0)
                insert_cse(eng, spa, 0)

        return T

    def insert_T(self, eng, spa, prob):
        self.CUR.execute("INSERT INTO t (?, ?, ?);", (eng, spa, prob))

    def get_T(self, eng, spa):
        self.CUR.execute('SELECT prob FROM t WHERE English=? AND Spanish=?;', (eng, spa))
        result = self.CUR.fetchone()
        return result[0]

    def update_T(self, eng, spa, prob):
        self.CUR.execute('UPDATE t SET prob=? WHERE English=? AND Spanish=?;', (prob, eng, spa)) 

    def insert_cse(self, eng, spa, count):
        self.CUR.execute("INSERT INTO cse (?, ?, ?);", (eng, spa, count))
        #Commit or something?

    def get_cse(self, eng, spa):
        self.CUR.execute('SELECT count FROM cse WHERE English=? AND Spanish=?;', (eng, spa))
        result = self.CUR.fetchone()
        return result[0]

    def update_cse(self, eng, spa, count):
        self.CUR.execute('UPDATE cse SET count=? WHERE English=? AND Spanish=?;', (count, eng, spa))

    def get_ce(self, eng):
        self.CUR.execute('SELECT count FROM ce WHERE English=?;', (eng,))
        result = self.CUR.fetchone()
        return result[0]

    def insert_ce(self, eng, count):
        self.CUR.execute('INSERT INTO ce (?, ?);', (eng, count))

    def update_ce(self, eng, count):
        self.CUR.execute('UPDATE t SET count=? WHERE English=?;', (count, eng))
        
#k is the sentence pair index. i is the foreign word index. j is the english word index. Gotta search over every english word and add up the probaiblities of the foreign word being translated from that english word. 

    def delta(self, k, i, j):

        spa_word = self.spa_sents[k][i]
        eng_word = self.eng_sents[k][j]
        num = self.get_T(eng_word,spa_word)
        denom = sum([self.get_T(eng,spa_word) for eng in eng_sents[k]])

        return num/denom


#So the formula puts the t in terms of t(f|e), but it's c(e_j^(k), f_i^(k)) 
    def gen_expected_counts(self):
#These dictionaries are actually immutable
        for k in xrange(len(self.eng_sents)):
            spas = self.spa_sents
            engs = self.eng_sents
            print k
            for i in xrange(len(spas[k])):
                for j in xrange(len(engs[k])): 
                    self.update_cse(engs[k][j],spas[k][i], (self.get_cse(engs[k][j],\
                            spas[k][i]) + self.delta(k, i, j)))
                    self.update_ce(engs[k][j], (self.get_ce(engs[k][i]) + self.delta(k, i, j)))


    def iterate_t(self):
        for eword in self.eng_lex:
            print eword
            for sword in self.spa_lex:
                self.update_T(eword, sword, self.get_cse(eword, sword)/self.get_ce(eword))
       #I need to do this for ALL possible freign and english words? So I probably want to compile all of the words, and then go through both initializing parameters in a giant for loop/dict comprehension


    def iterate_EM_algo(self,niters):

        for _ in xrange(niters):
            self.gen_expected_counts()
            self.update_t()




if __name__ == '__main__':
    

    em_test = EMFromTest('corpus.en', 'corpus.es', 'em_alignments.db')
    iterate_EM_algo(1, T, eng_sents, spa_sents, eng_lex, spa_lex)

    write_T_to_file(T, 'T.json')

