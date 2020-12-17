import traceback
import typing

from indexer import Indexer

DOCS_DIR: str = "./docs/"
DOC_SIZE: int = 1


def main() -> None:
    indexer = Indexer(DOCS_DIR, DOC_SIZE)


if __name__ == '__main__':
    main()
