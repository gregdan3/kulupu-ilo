import json
from typing import Dict, Iterable, List, Union

from tputils.download import get_data
from tputils.writing import VOWELS

# sound: representation


def safe_index(word: str, index: int):
    return word[index : index + 1]


def get_sounds_to_reprs(word: str) -> dict[str, List]:
    s_t_r = dict()
    s_t_r[word[0]], s_t_r[word] = [], []
    s_t_r[word[0]].append(word)
    s_t_r[word].append(word + ":")
    if len(word) == 1:
        return s_t_r

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
    urr_dict = {}

    data = get_data()["data"]
    for word in data.keys():
        reprs = get_sounds_to_reprs(word)
        print(reprs)

        for sound, repr in reprs.items():
            if sound in urr_dict:
                urr_dict[sound].extend(repr)
            else:
                urr_dict[sound] = repr
    print(urr_dict)


if __name__ == "__main__":
    main()
