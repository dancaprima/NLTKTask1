import nltk
from nltk.tokenize import RegexpTokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()


filename = 'dataprocessing.txt'
fin = open(filename, 'rU')
finaltext = fin.read()
lowercasing = finaltext.lower()
operator = RegexpTokenizer(r'[a-z]+')
regex = operator.tokenize(lowercasing)

#Sastrawi
sentences = ' '.join(regex)
stemming = stemmer.stem(sentences)



print lowercasing
print regex
print stemming
print stemming1
