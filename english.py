import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()


filename = 'english.txt'
fin = open(filename, 'rU')
finaltext = fin.read()
lowercasing = finaltext.lower()
operator = RegexpTokenizer(r'[a-z]+')
regex = operator.tokenize(lowercasing)

stemming = []

for reg in regex:
    stemming.append(stemmer.stem(reg))
#PorterStemmer

sentences = ' '.join(stemming)

print lowercasing
print regex
print sentences

