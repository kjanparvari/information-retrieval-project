import typing

from tokenizer import Token


class Stemmer:
    _stop_words: [str]

    def __init__(self):
        with open("./stopwords/stopwords.txt", encoding="utf-8") as file:
            self._stop_words = file.read().split()

    def normalize_list(self, tokens_list: [Token]) -> list:
        result: list = []
        token: Token
        for i in range(1, len(tokens_list)):
            token = tokens_list[i]
            nw = self._normalize_word(token.getWord())
            if nw != "":
                result.append(Token(nw, token.getPosition()))
                del token
        del tokens_list
        return result

    def _normalize_word(self, word: str) -> str:
        result: str = word
        if self._stop_words.__contains__(word):  # checking stop words
            return ""
        result = self.correct_invalid_chars(result)
        if result == "":
            return ""
        return result

    @staticmethod
    def correct_invalid_chars(word: str):
        new_string: [str] = []
        ln: int = 0
        for char in word:
            if char == 'ي':
                new_string.append('ی')
                ln += 1
            elif char in ['ة', 'ۀ']:
                new_string.append('ه')
                ln += 1
            elif char in ['‌', '‏']:
                new_string.append(' ')
                ln += 1
            elif char == 'ك':
                new_string.append('ک')
                ln += 1
            elif char == 'ؤ':
                new_string.append('و')
                ln += 1
            elif char in ['إ', 'أ']:
                new_string.append('ا')
                ln += 1
            elif char in ['\u064B',  # تنوین فتحه
                          '\u064C',  # تنوین ضمه
                          '\u064D',  # تنوین کسره
                          '\u064E',  # فتحه
                          '\u064F',  # ضمه
                          '\u0650',  # کسره
                          '\u0651',  #
                          '\u0652']:  # سکون
                ln += 1
                pass
            else:
                new_string.append(char)

                ln += 1

        return ''.join(new_string)
