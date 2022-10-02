from tputils.process import get_sounds_to_reprs


def test_nanpa():
    assert get_sounds_to_reprs("nanpa") == {
        "n": ["nanpa"],
        "na": ["nanpa·"],
        "nan": ["nanpa··"],
        "nanpa": ["nanpa···", "nanpa:"],
    }


def test_anpa():
    assert get_sounds_to_reprs("anpa") == {
        "a": ["anpa"],
        "an": ["anpa·"],
        "anpa": ["anpa··", "anpa:"],
    }


def test_kepeken():
    assert get_sounds_to_reprs("kepeken") == {
        "k": ["kepeken"],
        "ke": ["kepeken·"],
        "kepe": ["kepeken··"],
        "kepeke": ["kepeken···"],
        "kepeken": ["kepeken····", "kepeken:"],
    }
