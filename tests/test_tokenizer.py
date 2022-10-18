import pytest

from tputils.tokenize import tp_sent_tokenize, tp_word_tokenize


def test_document():
    doc = "nimi mi li jan Wiku. sina wile seme? mi wile pona tawa jan mute mute a!"
    compare = [
        "nimi mi li jan Wiku.",
        "sina wile seme?",
        "mi wile pona tawa jan mute mute a!",
    ]
    result = tp_sent_tokenize(doc)
    assert compare == result


def test_sentence():
    sent = "nimi mi li jan Wiku."
    compare = ["nimi", "mi", "li", "jan", "Wiku", "."]
    result = tp_word_tokenize(sent)
    assert compare == result


def test_sentence_name():
    pytest.skip("name joining not implemented")
    sent = "nimi mi li jan Kekan San."
    compare = ["nimi", "mi", "li", "jan", "Kekan San", "."]
    result = tp_word_tokenize(sent)
    assert compare == result
