from tokenizer import Tokenizer
from stemmer import Stemmer
from docloader import DocLoader


class Indexer:
    def __init__(self, docsDir, docsSize):
        self.docLoader = DocLoader(docsDir, docsSize)
        self.tokenizer = Tokenizer()
        self.stemmer = Stemmer()

    def tmp(self):
        print(self.docLoader.getDoc(1))
