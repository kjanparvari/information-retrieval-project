class Tokenizer:
    def __init__(self):
        pass

    def tokenizeDoc(self, file: typing.TextIO) -> None:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                print(normalize(word))