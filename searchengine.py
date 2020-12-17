from indexer import Dictionary, PostingList, Posting, DICT_DIST, POSTING_DIST
import os
import pickle

from tokenizer import Token, Tokenizer
from stemmer import Stemmer


class SearchEngine:
    _dictionary: Dictionary
    _tokenizer: Tokenizer
    _stemmer: Stemmer

    def __init__(self):
        self._dictionary = Dictionary(load=True)
        self._tokenizer = Tokenizer()
        self._stemmer = Stemmer()
        print(self._dictionary)

    def _search_for_token(self, token: Token):
        pl = self._dictionary.getPostingList(token.getWord())
        print("before")
        print(pl)
        print("after")

    def listen(self):
        # inp = input("Enter Your Query: ")
        inp = "تراکتور"
        for p in self._tokenizer.tokenizeDoc(inp):
            print(p)
            self._search_for_token(p)


def main():
    se = SearchEngine()
    se.listen()


if __name__ == '__main__':
    main()
