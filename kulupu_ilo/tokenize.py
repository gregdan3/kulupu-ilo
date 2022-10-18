from typing import List

import nltk

from kulupu_ilo.validate import VOWELS

Sent = str
Word = str
TokenizedWords = List[str]


def safe_index(word: str, index: int):
    return word[index : index + 1]


def tp_sent_tokenize(doc: str) -> List[Sent]:
    return nltk.sent_tokenize(doc)


def tp_word_tokenize(sent: str) -> List[Word]:
    return nltk.word_tokenize(sent)


# for a very loose definition of "tokenize"
def mora_split(word: str) -> List[str]:
    moras = []
    i = 0
    end = len(word)
    while i < end:
        con, vow = word[i], safe_index(word, i + 1)
        if (con in VOWELS) or (con == "n" and vow not in VOWELS):
            moras.append(con)
            i += 1
            continue
        moras.append(con + vow)
        i += 2

    return moras


# for a very loose definition of "tokenize"
def syllable_split(word: str) -> List[str]:
    syls = []
    i = 0
    end = len(word)
    while i < end:
        con, vow = word[i], safe_index(word, i + 1)
        if i == 0:
            if con in VOWELS:
                if vow == "n":
                    syls.append(con + vow)  # Vn
                    i += 2
                    continue
                syls.append(con)  # V
                i += 1
                continue
        n = safe_index(word, i + 2)
        if n == "n":
            syls.append(con + vow + n)  # CVn
            i += 3
            continue
        syls.append(con + vow)  # Vn
        i += 2

    return syls
