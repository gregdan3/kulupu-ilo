import json
import urllib.request
from typing import Dict, Iterable, List, Union

from tputils.writing import VOWELS

JASIMA = "https://raw.githubusercontent.com/lipu-linku/jasima/master/data.json"

# sound: representation


def download(url: str) -> bytes:
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req).read()
    return resp


def safe_index(word: str, index: int):
    return word[index : index + 1]


def get_sounds_to_reprs(word: str) -> dict[str, List]:
    s_t_r = dict()
    s_t_r[word[0]] = [word]
    moras = mora_split(word)
    current = ""
    offset = 1
    for i in range(len(moras)):
        current += moras[i]
        if moras[i] in VOWELS:
            offset = 0
            continue
        if current not in s_t_r:
            s_t_r[current] = []

        s_t_r[current].append(word + "·" * (i + offset))
        if current == word:
            s_t_r[current].append(word + ":")
    return s_t_r


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


def main():
    # word_data = json.loads(download(JASIMA).decode("UTF-8"))["data"]
    mora_split("kekansan")


if __name__ == "__main__":
    main()
