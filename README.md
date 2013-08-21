machine_translation
===================
An implementation of IBM1 model of translation in Python. **WORK IN PROGRESS**

The training data given is a set of paralell sentences in English and Spanish from Europarliament transcripts. The goal is to compute *t*(spanish | english), the 
probability that a spanish word is translated from an English word, for every word used in the corpuses. 
This data will then be used to generate "alignments" for the development data. An alignment records which English word in a given 
sentence a Spanish word was translated from. For example, given the two sentences:

"Coding is fun"

"La codificación es divertido"

"Coding" would correspond to "codificación". Given that this is sentence number 1 in the development data, the alignment should
look like:

SentenceNumber EnglishIndex SpanishIndex

1 1 2

1 2 3

1 3 4

####My python files:
1. clean_corpus.py - The pariliament transcripts are supposed to be all lower case, with punctuation treated as separate words. The English corpus came with some errors, i.e. "mistake." instead of "mistake . ", which I found and fixes with a few regexes. 
2. gen_alignment_matrix.py - This is the script that compiles our probabilities t(spanish | english). Depending on the branch you look at, it has been implemented a couple of different ways, trying to find the sweet spot in the compromise between memory usage and speed. Unfortunately, *t* and the expected counts *cse* are matrices of size 10,000 English words by 10,000 Spanishwords, which in this model are all intiialized to a non-zero float value and then adjusted individually. This means something on the order of 400 MB for each matrix, let alone all the overhead of python. 
Some solutions:

  a. Do it all in memory anyway. It works but nothing else will run on your compute. (branch: master)
  
  b. Convert those matrices to sqlite databases. Also works, put pretty damn slow. (branch: database)
  
  c. Store each English word's dictionary of Spanish word (key) and translationship probabliilty (value) in a file of a corresponding name. (branch: collecitonoffiles)
3. apply-to-dev.py. Yet to come, this will take *t* and generate alignments.
