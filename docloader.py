import traceback


class DocLoader:
    def __init__(self, dir: str, size: int):
        self.dir = dir
        self.size = size

    def getDoc(self, docNumber: int):
        try:
            with open(self.dir + f"{docNumber}.txt", "r", encoding='utf-8', buffering=True) as file:
                return file.read()
        except (FileExistsError, FileNotFoundError) as e:
            print(traceback.format_exc())
