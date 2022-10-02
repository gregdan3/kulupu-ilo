from tputils.staircase import staircase
from tputils.writing import CONSONANTS, VOWELS, valid_syllables

print(valid_syllables())
SYLLABLES = list(valid_syllables())
CONSONANTS = list(CONSONANTS)
VOWELS = list(VOWELS)

FULL_STAIRS = SYLLABLES + CONSONANTS + VOWELS + [" "]


def test_none():
    assert staircase("", [], []) == None


def test_params():
    assert staircase("", []) == None


def test_empty_steps():
    assert staircase("a", []) == None


def test_empty_stairs():
    assert staircase("", ["a"]) == None


def test_equal_step_stair():
    assert staircase("a", ["a"]) == [["a"]]


def test_double_stairs():
    assert staircase("aa", ["a"]) == [["a", "a"]]


def test_two_step_cases():
    assert staircase("aa", ["a", "aa"]) == [["a", "a"], ["aa"]]


def test_name1():
    assert staircase("Kekan San".lower(), FULL_STAIRS)


def test_name2():
    assert staircase("Kapilu".lower(), FULL_STAIRS)


def test_name3():
    assert staircase("Ke Tami".lower(), FULL_STAIRS)


def test_name4():
    assert staircase("Palisewi".lower(), FULL_STAIRS)
