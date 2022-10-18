from kulupu_ilo.toys import get_sounds_to_reprs


def test_nanpa():
    assert get_sounds_to_reprs("nanpa") == {
        "n": ["nanpa"],
        "na": ["nanpa·"],
        "nan": ["nanpa··"],
        "nanpa": ["nanpa:", "nanpa···"],
    }


def test_anpa():
    assert get_sounds_to_reprs("anpa") == {
        "a": ["anpa"],
        "an": ["anpa·"],
        "anpa": ["anpa:", "anpa··"],
    }


def test_kepeken():
    assert get_sounds_to_reprs("kepeken") == {
        "k": ["kepeken"],
        "ke": ["kepeken·"],
        "kepe": ["kepeken··"],
        "kepeke": ["kepeken···"],
        "kepeken": ["kepeken:", "kepeken····"],
    }


def test_ike():
    assert get_sounds_to_reprs("ike") == {"i": ["ike"], "ike": ["ike:", "ike·"]}


def test_li():
    assert get_sounds_to_reprs("li") == {"l": ["li"], "li": ["li:", "li·"]}


def test_n():
    assert get_sounds_to_reprs("n") == {"n": ["n", "n:"]}


def test_e():
    assert get_sounds_to_reprs("e") == {"e": ["e", "e:"]}
