from kulupu_ilo.tokenize import syllable_split


def test_nanpa():
    assert syllable_split("nanpa") == ["nan", "pa"]


def test_suli():
    assert syllable_split("suli") == ["su", "li"]


def test_li():
    assert syllable_split("li") == ["li"]


def test_anpa():
    assert syllable_split("anpa") == ["an", "pa"]


def test_misikeke():
    assert syllable_split("misikeke") == ["mi", "si", "ke", "ke"]


def test_kijetesantakalu():
    assert syllable_split("kijetesantakalu") == [
        "ki",
        "je",
        "te",
        "san",
        "ta",
        "ka",
        "lu",
    ]


def test_kekansan():
    assert syllable_split("kekansan") == ["ke", "kan", "san"]
