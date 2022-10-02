VOWELS = {"a", "e", "i", "o", "u"}
CONSONANTS = {"j", "k", "l", "m", "n", "p", "s", "t", "w"}
FORBIDDEN = {"wu", "wo", "ji", "ti"}
MUSI_CONSONANTS = {"y", "g"}
SPACING = 5


def _valid_syls_or_moras(musi: bool, syl: bool) -> set[str]:
    s_or_m = set()
    L_CONSONANTS = CONSONANTS | MUSI_CONSONANTS if musi else CONSONANTS
    for consonant in L_CONSONANTS:
        for vowel in VOWELS:
            syllable = consonant + vowel
            if syllable not in FORBIDDEN:
                s_or_m.add(syllable)
                if syl:
                    s_or_m.add(syllable + "n")
    s_or_m |= VOWELS
    if not syl:
        s_or_m.add("n")
    return s_or_m


def valid_syllables(musi: bool = False):
    return _valid_syls_or_moras(musi=musi, syl=True)


def valid_moras(musi: bool = False):
    return _valid_syls_or_moras(musi=musi, syl=False)


def invalid_syllables():
    return FORBIDDEN | {syl + "n" for syl in FORBIDDEN}


def chart_syllables():
    for vowel in VOWELS:
        for consonant in CONSONANTS:
            syllable = consonant + vowel
            if syllable[:2] in FORBIDDEN:
                # illegal part can only occur in first two chars
                print(" " * SPACING, end="")
                continue

            print(("{:<%s}" % SPACING).format(syllable), end="")
            # this is the crunchiest workaround
        print()


def main():
    chart_syllables()


if __name__ == "__main__":
    main()
