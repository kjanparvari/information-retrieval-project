import traceback


class DocLoader:
    def __init__(self, directory: str, size: int):
        self.dir = directory
        self.size = size

    def getDoc(self, doc_number: int):
        try:
            with open(self.dir + f"{doc_number}.txt", "r", encoding='utf-8', buffering=True) as file:
                return file.read()
        except (FileExistsError, FileNotFoundError) as e:
            print(traceback.format_exc())
