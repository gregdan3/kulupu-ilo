from tputils.writing import CONSONANTS, VOWELS, valid_moras, valid_syllables


def test_moras():
    moras = valid_moras(musi=True)
    assert "gu" in moras


def test_syls():
    syls = valid_syllables(musi=True)
    assert "yun" in syls


def test_moras_2():
    moras = valid_moras()
    assert "wa" in moras
    assert "wu" not in moras
    assert "gu" not in moras


def test_syls_2():
    syls = valid_syllables()
    assert "wan" in syls
    assert "wun" not in syls
    assert "gun" not in syls
