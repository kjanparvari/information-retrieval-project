import errno
import os
import pickle
import typing
import json
from tokenizer import Tokenizer, Token
from stemmer import Stemmer
from docloader import DocLoader

DICT_DIST = "./dist/"
POSTING_DIST = "./dist/postings-lists/"


class Posting:
    _docId: int
    _positions: [int]

    def __init__(self, doc_id):
        self._docId = doc_id
        self._positions = []

    def addPosition(self, position: int):
        if not self._positions.__contains__(position):
            self._positions.append(position)

    def getDocId(self):
        return self._docId

    def __str__(self):
        s: str = ""
        s += "doc: " + str(self._docId) + " | "
        for p in self._positions:
            s += str(p) + " "
        return s


class PostingList:
    _id: int
    _term: str
    _list: [Posting]

    def __init__(self, term: str, pl_id: int):
        self._list = []
        self._term = term
        self._id = pl_id

    def addToken(self, token: Token, doc_id: int):
        p: Posting
        for p in self._list:
            if p.getDocId() == doc_id:
                p.addPosition(token.getPosition())
                self._save()
                return
        p = Posting(doc_id)
        p.addPosition(token.getPosition())
        self._list.append(p)
        self._save()

    def getFrequency(self) -> int:
        return len(self._list)

    def getTerm(self):
        return self._term

    def __str__(self):
        s: str = ""
        s += "term: " + self._term + " -> "
        for p in self._list:
            s += str(p)
        return s

    def _save(self):
        pl_addr: str = POSTING_DIST + str(self._id) + ".pl"
        if not os.path.exists(os.path.dirname(pl_addr)):
            try:
                os.makedirs(os.path.dirname(pl_addr))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        try:
            with open(pl_addr, 'wb') as pl_file:
                pl = pickle.dump(self, pl_file)
                pl_file.close()
        except (FileNotFoundError, FileExistsError) as e:
            print("error")


class Dictionary:
    _dict: {str, int}

    def __init__(self):
        self._dict = {}

    def addToken(self, token: Token, doc_id: int):
        term = token.getWord()
        pl: PostingList
        x = self._getPostingList(term)
        if x is None:
            pl_id: int = len(self._dict)
            self._dict[term] = pl_id
            pl = PostingList(term, pl_id)
            self._save()

        else:
            pl = x
        pl.addToken(token, doc_id)

    def _getPostingList(self, term: str) -> typing.Union[PostingList, None]:
        pl_id: int = self._getPostingListId(term)
        pl: PostingList
        pl_addr: str = POSTING_DIST + str(pl_id) + ".pl"
        if os.path.exists(pl_addr):
            with open(pl_addr, 'rb') as pl_file:
                pl = pickle.load(pl_file)
                pl_file.close()
            return pl
        else:
            return None

    def _getPostingListId(self, term: str) -> int:
        return self._dict.get(term) if self._dict.__contains__(term) else -1

    def _load(self):
        dic_addr: str = DICT_DIST + 'dictionary.json'
        if not os.path.exists(os.path.dirname(dic_addr)):
            try:
                os.makedirs(os.path.dirname(dic_addr))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        try:
            with open(dic_addr, 'r') as inputFile:
                self._dict = json.load(inputFile)
        except (FileNotFoundError, FileExistsError) as e:
            print("error")

    def _save(self):
        dic_addr: str = DICT_DIST + 'dictionary.json'
        if not os.path.exists(os.path.dirname(dic_addr)):
            try:
                os.makedirs(os.path.dirname(dic_addr))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        try:
            with open(dic_addr, 'w') as outFile:
                json.dump(self._dict, outFile)
        except (FileNotFoundError, FileExistsError) as e:
            print("error")

    def __str__(self):
        return str(self._dict)

    def test(self):
        self._load()
        # print(self)
        a = self._getPostingList("را")
        print(a)


class Indexer:
    def __init__(self, docs_dir, docs_size):
        self.docLoader = DocLoader(docs_dir, docs_size)
        self.tokenizer = Tokenizer()
        self.stemmer = Stemmer()
        self.dictionary = Dictionary()

        self.dictionary.test()

        # for i in range(1, docs_size + 1):
        #     doc = self.docLoader.getDoc(i)
        #     tokens = self.tokenizer.tokenizeDoc(doc)
        #     # print("tokens: ")
        #     # for token in tokens:
        #     #     print(token)
        #     normalized_words = self.stemmer.normalize_list(tokens)
        #     # print("normalized_words: ")
        #     # for token in normalized_words:
        #     #     print(token)
        #     for i in range(1, len(tokens)):
        #         self.dictionary.addToken(tokens[i], i)
