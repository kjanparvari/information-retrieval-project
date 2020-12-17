import traceback
import typing
import re

from indexer import Indexer

DOCS_DIR: str = "./docs/"
DOC_SIZE: int = 10


def main() -> None:
    indexer = Indexer(DOCS_DIR, DOC_SIZE)


if __name__ == '__main__':
    main()
