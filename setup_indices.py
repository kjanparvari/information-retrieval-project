import traceback
import typing

from indexer import Indexer

DOCS_DIR: str = "./docs/"
DOC_SIZE: int = 1
stop_words = ["و"]


def is_stop_word(word: str) -> bool:
    if stop_words.__contains__(word):
        return True


def normalize(word: str) -> str:
    # removing leading and ending spaces.
    # removing commas and dots
    result: str = word.strip().replace(".", "").replace("،", "")

    # replacing ending ha
    if result[:]:
        pass
    return result


def main() -> None:
    indexer = Indexer(DOCS_DIR, DOC_SIZE)
    indexer.tmp()


if __name__ == '__main__':
    main()
