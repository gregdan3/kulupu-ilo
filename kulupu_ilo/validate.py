import re

VOWELS = {"a", "e", "i", "o", "u"}
CONSONANTS = {"j", "k", "l", "m", "n", "p", "s", "t", "w"}
ALPHABET = CONSONANTS | VOWELS
FORBIDDEN = {"wu", "wo", "ji", "ti"}
MUSI_CONSONANTS = {"y", "g"}
SPACING = 5

WORD_RE = r"^(?:(?:^[aeiou]|[klmnps][aeiou]|[jt][aeou]|[w][aei])(?:n(?![mn]))?)+$"
WORD_RE = re.compile(WORD_RE)
SYL_RE = r"TODO"
SYL_RE = re.compile(SYL_RE)


def _valid_syls_or_moras(
    consecutive: bool, do_syls: bool, musi: bool = False
) -> set[str]:
    s_or_m = set()
    local_cons = CONSONANTS | MUSI_CONSONANTS if musi else CONSONANTS
    for vow in VOWELS:
        for con in local_cons:
            syllable = con + vow
            if syllable not in FORBIDDEN:
                s_or_m.add(syllable)
                s_or_m.add(syllable + "n") if do_syls else None

        if not consecutive:
            s_or_m.add(vow)
            s_or_m.add(vow + "n") if do_syls else None

    if not do_syls:
        s_or_m.add("n")
    return s_or_m


def valid_syllables(consecutive: bool = False, musi: bool = False):
    return _valid_syls_or_moras(consecutive=consecutive, do_syls=True, musi=musi)


def valid_moras(consecutive: bool = False, musi: bool = False):
    return _valid_syls_or_moras(consecutive=consecutive, do_syls=False, musi=musi)


def invalid_syllables():
    return FORBIDDEN | {syl + "n" for syl in FORBIDDEN}


def invalid_mora():
    return FORBIDDEN


def validate_word(word: str):
    return re.fullmatch(WORD_RE, word) is not None


def validate_syl(word: str):
    raise NotImplementedError
