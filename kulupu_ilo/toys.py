#!/usr/bin/env python3
import json
from typing import Dict, List, Optional

from kulupu_ilo.tokenize import mora_split
from kulupu_ilo.validate import VOWELS, valid_syllables, validate_word
from kulupu_ilo.words import nimi_Linku


def rm_str_prefix(str, prefix):
    return str[len(prefix) :]


def all_possible_words(n: int):
    words = []
    syllables = valid_syllables(consecutive=False)
    con_syls = valid_syllables(consecutive=True)
    for syl1 in syllables:
        for syl2 in con_syls:
            could_word = syl1 + syl2
            if validate_word(could_word):
                words.append(could_word)

            # for syl3 in syllables:
            #     for syl4 in syllables:
            #         could_word = syl1 + syl2 + syl3 + syl4
            #         if validate_word(could_word):
            #             words.append(could_word)
    # pprint(words)


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


def staircase(
    stairs: str,
    steps: List[str],
    past: Optional[List[str]] = None,
    paths: Optional[List[List[str]]] = None,
) -> Optional[List[List[str]]]:
    """Given a 'staircase' string, return all possible paths through that
    string given a list of possible steps. Returns None if not possible.
    The complexity here is **bad**. This is depth first."""
    if past is None:
        past = []
    if paths is None:
        paths = []
    if not steps:
        return
    if not stairs:
        if past:
            paths.append(past)
        return

    for step in steps:
        if stairs.startswith(step):
            staircase(rm_str_prefix(stairs, step), steps, past + [step], paths)
    return paths


def repr_staircase(
    stairs: str,
    steps: Dict[str, List[str]],
    past: Optional[List[str]] = None,
    paths: Optional[List[List[str]]] = None,
) -> Optional[List[List[str]]]:
    """Given a 'staircase' string, return all possible paths through that
    string given a list of possible steps. Returns None if not possible.
    The complexity here is **bad**. This is depth first."""
    if past is None:
        past = []
    if paths is None:
        paths = []
    if not steps:
        return
    if not stairs:
        if past:
            paths.append(past)
        return

    for step in steps:
        if stairs.startswith(step):
            for substep in steps[step]:
                repr_staircase(
                    rm_str_prefix(stairs, step), steps, past + [substep], paths
                )
    return paths


def generate_steps(words: List[str], one_letter_one_path: bool = True):
    urr_dict = {}
    for word in words:
        reprs = get_sounds_to_reprs(word)
        for sound, repr in reprs.items():
            if sound in urr_dict:
                urr_dict[sound].extend(repr)
            else:
                urr_dict[sound] = repr
            if one_letter_one_path and len(sound) == 1:
                urr_dict[sound] = urr_dict[sound][:1]
    urr_dict[" "] = [" "]
    return urr_dict


def main(argv):
    words = [
        word
        for word, content in nimi_Linku().items()
        if content["usage_category"] in {"core", "widespread", "common", "uncommon"}
    ]

    steps = generate_steps(words, one_letter_one_path=True)
    print("STEPS = ", sep="", end="")
    print(json.dumps(steps, ensure_ascii=False))

    steps = generate_steps(words, one_letter_one_path=False)
    print("BIGSTEPS = ", sep="", end="")
    print(json.dumps(steps, ensure_ascii=False))


if __name__ == "__main__":
    main(None)
