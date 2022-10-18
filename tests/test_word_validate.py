from kulupu_ilo.validate import validate_word


def test_outside_alphabet():
    assert not validate_word("pingo")


def test_inside_alphabet_bad():
    assert not validate_word("kassi")


def test_consecutive_coda_bad():
    assert not validate_word("tennnnpo")


def test_consecutive_coda_small_bad():
    assert not validate_word("tennpo")


def test_coda():
    assert validate_word("tenpo")


def test_consecutive_nasal_n():
    assert not validate_word("ninnin")


def test_consecutive_nasal_m():
    assert not validate_word("ninmo")


def test_leading_vowel():
    assert validate_word("anpa")


def test_double_coda():
    assert validate_word("lanpan")


def test_short():
    assert validate_word("a")


def test_short_2():
    assert validate_word("li")


def test_long():  # yes really
    assert validate_word("manipulate")


def test_long_2():
    assert validate_word("kijetesantakalu")


def test_illegal_nasal():
    assert not validate_word("enmo")


def test_illegal_syl():
    assert not validate_word("wuwojiti")
