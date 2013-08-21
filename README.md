machine_translation
===================
An implementation of IBM1 model of translation in Python. 

The training data given is a set of paralell sentences in English and Spanish from the Europarliament. THe goal is to compute t(spanish | english), the 
probability that a spanish word is translated from an English word, for every word used in the corpuses. 
This data will then be used to generate "alignments" for the development data. An alignment records which English word in a given 
sentence a Spanish word was translated from. For example, given the two sentences:

"Coding is fun"

"La codificación es divertido"

"Coding" would correspond to "codificación'. Given that this is sentence number 1 in the development data, the alignment should
look like:

SentenceNumber EnglishIndex SpanishIndex
1 1 2
1 2 3
1 3 4

####What the files do:

