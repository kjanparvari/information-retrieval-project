import traceback
import typing

DOCS_DIR: str = "./docs/"
DOC_SIZE: int = 1
stop_words = ["و"]


class Stemmer:
    pass


class Tokenizer:

    def tokenize(self, file: typing.TextIO) -> None:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                print(normalize(word))


class Indexer:
    pass


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
    try:
        for i in range(1, DOC_SIZE + 1):
            with open(DOCS_DIR + "1.txt", "r", encoding='utf-8', buffering=True) as file:
                tokenize(file)
    except (FileExistsError, FileNotFoundError) as e:
        print(traceback.format_exc())


if __name__ == '__main__':
    main()
