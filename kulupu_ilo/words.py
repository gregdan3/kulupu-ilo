#!/usr/bin/env python
import argparse
import json
import os
import urllib.request
from typing import Dict, List, Literal

FILEDIR = "downloads"

SONJA_FILES = ["nimi_pu.txt", "nimi_pi_pu_ala.txt", "nimi_ku.txt"]
SONJA_FILES_J = [FILEDIR + os.sep + name for name in SONJA_FILES]
SONJA_SOURCES = ["pu", "ku", "ku", "other"]
SONJA_UPSTREAM = ""

LINKU_FILES = ["data.json"]
LINKU_FILES_J = [FILEDIR + os.sep + name for name in LINKU_FILES]
LINKU_UPSTREAM = "https://raw.githubusercontent.com/lipu-linku/jasima/master/"

# join filename from _FILES to _UPSTREAM to get download source

JAN_MUTE_ALA = "# jan mute ala li kepeken nimi ni pi pu ala:\n"


def download(url: str) -> bytes:
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req).read()
    return resp


def download_nimi_Sonja():
    return [download(SONJA_UPSTREAM + fname) for fname in SONJA_FILES]


def download_nimi_Linku():
    return [download(LINKU_UPSTREAM + fname) for fname in LINKU_FILES]


def _process_word(word: str) -> dict:
    # edge case: multi-word definitions (yupekosi), quotes in definition (pu)
    splits = word.split(" ")
    defin = " ".join(splits[:-1])
    score = splits[-1]
    return {"def": defin, "score": int(score)}


def _process_definitions(defs: str) -> list:
    return [_process_word(defin.strip()) for defin in defs.split(",")]


def _process_line(line: str, source: str) -> dict:
    # edge case: files download in DOS format, spare whitespace, []
    if not line or line[0] == "#" or line == os.linesep:
        return {}
    word, *defs = line.split(":")
    defs = ":".join(defs).strip().replace("[", "").replace("]", "").replace('"', "")
    return {word: {"meanings": _process_definitions(defs), "source": source}}


def nimi_filter(
    nimi: dict,
    minscore: int = 0,
    minsize: int = 0,
    maxsize: int = 0,
    override: list = [],
):
    """
    don't use this unironically
    it isn't very representative of toki pona

    intended for use with tputils.words.nimi_Sonja

    1. directly assign override words into nimi_sin
    2. remove words having fewer definitions than minsize
        - before score removal for fairness
    3. remove definitions scoring lower than minscore
    4. remove definitions after keeping maxsize many
        - for words with altogether too many definitions for brevity
    5. assign remainder to nimi_sin
    """
    nimi_sin = {}
    for key in nimi:
        defs_of_nimi = nimi[key]["meanings"]
        nlen = len(defs_of_nimi)

        if override and key in override:
            nimi_sin[key] = nimi[key]
            continue

        if minsize and nlen < minsize:
            continue

        defs_of_nimi = [w for w in defs_of_nimi if w["score"] >= minscore]

        if maxsize and nlen > maxsize:
            # assumption: nimi_lipu is score sorted
            defs_of_nimi = defs_of_nimi[:maxsize]

        if defs_of_nimi:
            nimi_sin[key] = nimi[key]
            nimi_sin[key]["meanings"] = defs_of_nimi

    return nimi_sin


def nimi_Sonja(
    book_categories: List[Literal["pu"] | Literal["ku"] | Literal["other"]] = [
        "pu",
        "ku",
        "other",
    ],
    # minscore: int = 0,
    # minsize: int = 0,
    # maxsize: int = 0,
    # override: List[str] = [],
) -> Dict:
    nimi = {}
    source = SONJA_SOURCES[0]
    for i, file in enumerate(SONJA_FILES_J):
        source = SONJA_SOURCES[i]
        f = open(file, "r")

        for line in f:
            if file == SONJA_FILES_J[1]:  # nimi pi pu ala
                if line == JAN_MUTE_ALA:
                    source = SONJA_SOURCES[-1]  # special case!
            nimi.update(_process_line(line, source))
        f.close()

    # loje and pu are the only nimi pu with one definition in `nimi_pu.txt`
    # nimi = nimi_filter(
    #     nimi,
    #     minscore=minscore,
    #     minsize=minsize,
    #     maxsize=maxsize,
    #     override=override,
    # )
    return nimi


def nimi_Linku():
    linku_data = open(LINKU_FILES_J[0], "r").read()
    linku_data = json.loads(linku_data)
    linku_data = linku_data["data"]
    return linku_data


def main(argv):
    pass


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "--minscore",
        "-s",
        dest="minscore",
        default=0,
        choices=range(0, 101),
        type=int,
        help="Remove words with lower than min-score frequency score",
        metavar="[0-100]",
    )
    PARSER.add_argument(
        "--minsize",
        "-n",
        dest="minsize",
        default=0,
        type=int,
        help="Remove words with fewer than min-size definitions",
        metavar="MIN",
    )
    PARSER.add_argument(
        "--maxsize",
        "-m",
        dest="maxsize",
        default=0,
        type=int,
        help="Reduce the number of definitions of a word to max-size",
        metavar="MAX",
    )
    PARSER.add_argument(
        "--override",
        "-o",
        dest="override",
        default=[],
        type=list,
        help="Ignore filtering behavior for given word(s)",
        metavar="OVERRIDE",
        nargs="*",
    )

    ARGV = PARSER.parse_args()

    main(ARGV)
