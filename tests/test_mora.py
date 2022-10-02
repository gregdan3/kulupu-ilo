from tputils.process import mora_split


def test_nanpa():
    assert mora_split("nanpa") == ["na", "n", "pa"]


def test_suli():
    assert mora_split("suli") == ["su", "li"]


def test_li():
    assert mora_split("li") == ["li"]


def test_anpa():
    assert mora_split("anpa") == ["a", "n", "pa"]


def test_misikeke():
    assert mora_split("misikeke") == ["mi", "si", "ke", "ke"]


def test_kijetesantakalu():
    assert mora_split("kijetesantakalu") == [
        "ki",
        "je",
        "te",
        "sa",
        "n",
        "ta",
        "ka",
        "lu",
    ]


def test_kekansan():
    assert mora_split("kekansan") == ["ke", "ka", "n", "sa", "n"]
