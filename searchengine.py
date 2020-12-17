from indexer import Dictionary, PostingList, Posting, DICT_DIST, POSTING_DIST
import os
import pickle

from tokenizer import Token, Tokenizer
from stemmer import Stemmer


class Candidate:
    _doc_id: int
    _score: int
    _covered_tokens: [(Token, [int])]  # token, positions

    def __init__(self, doc_id: int, score: int = 0):
        self._covered_tokens = []
        self._score = score
        self._doc_id = doc_id

    def getDocId(self):
        return self._doc_id

    def add(self, token: Token, positions: [int]):
        self._covered_tokens.append((token, positions))

    def getScore(self):
        return self._score

    def computeScore(self):
        length = len(self._covered_tokens)
        self._score = length

        if length >= 2:
            t1: Token
            t2: Token
            for i in range(0, length - 1):
                (t1, p1) = self._covered_tokens[i]
                (t2, p2) = self._covered_tokens[i + 1]

                if abs(t1.getPosition() - t2.getPosition()) == 1:
                    pi: int
                    pj: int
                    for pi in p1:
                        for pj in p2:
                            if abs(pi - pj) == 1:
                                self._score += 2

    def __str__(self) -> str:
        s: str = "doc: "
        s += str(self._doc_id)
        s += " -> score: "
        s += str(self._score)
        return s


class QueryResult:
    _list: [(Token, PostingList)]
    _candidates: [Candidate]  # (docId, score)

    def __init__(self):
        self._list = []
        self._candidates = []

    def addToResults(self, t: Token, pl: PostingList):
        self._list.append((t, pl))

    def buildCandidates(self):
        t: Token
        pl: PostingList
        p: Posting
        c: Candidate or None
        for (t, pl) in self._list:
            for p in pl.getPostings():
                c = self.getCandidate(p.getDocId())
                if c is None:
                    c = Candidate(p.getDocId())
                    self._candidates.append(c)
                c.add(t, p.getPositions())
        for c in self._candidates:
            c.computeScore()

    def getCandidate(self, doc_id: int) -> Candidate or None:
        c: Candidate
        for c in self._candidates:
            if c.getDocId() == doc_id:
                return c
        return None

    def printKBestCandidates(self, k=None):
        if k is None:
            k = len(self._candidates)
        from heap import MaxHeap
        c: Candidate
        # for c in self._candidates:
        #     print(c)
        h = MaxHeap(len(self._candidates))
        for c in self._candidates:
            h.insert(c)
        result_number = len(self._candidates) if len(self._candidates) < k else k
        for i in range(result_number):
            print(h.extractMax())


class SearchEngine:
    _dictionary: Dictionary
    _tokenizer: Tokenizer
    _stemmer: Stemmer
    _query_result: QueryResult

    def __init__(self):
        self._dictionary = Dictionary(load=True)
        self._tokenizer = Tokenizer()
        self._stemmer = Stemmer()
        self._query_result = QueryResult()
        print(self._dictionary)

    def _search_for_token(self, token: Token):
        pl = self._dictionary.getPostingList(token.getWord())
        print(pl)
        if pl is not None:
            self._query_result.addToResults(token, pl)

    def listen(self):
        inp = input("Enter Your Query: ")
        # inp = "هفته"
        query_tokens = self._tokenizer.tokenizeDoc(inp)
        normalized_query_tokens = self._stemmer.normalize_list(query_tokens)
        for p in normalized_query_tokens:
            self._search_for_token(p)
        self._query_result.buildCandidates()
        self._query_result.printKBestCandidates()


def main():
    se = SearchEngine()
    se.listen()


if __name__ == '__main__':
    main()
