# tests/test_tuples.py

import exercises


def test_create_tuple():
    assert exercises.create_tuple() == (10, 20, 30, 40, 50)


def test_access_elements():
    t = ("banana", "apple", "date", "cherry")
    new_tuple = exercises.access_elements(t)
    assert new_tuple == ("apple", "date")


def test_check_membership():
    numbers = (10, 20, 25, 30, 35)
    assert exercises.check_membership(numbers) is True


def test_concat_and_repeat():
    t1 = (1, 2, 3)
    t2 = ("a", "b")
    concat, repeated = exercises.concat_and_repeat(t1, t2)
    assert concat == (1, 2, 3, "a", "b")
    assert repeated == (1, 2, 3, 1, 2, 3, 1, 2, 3)


def test_count_and_index():
    t = (5, 10, 15, 10, 20, 10, 25)
    count_10, index_15 = exercises.count_and_index(t)
    assert count_10 == 3
    assert index_15 == 2


def test_unpack_person():
    person = ("Alice", 25, "Engineer")
    job, age, name = exercises.unpack_person(person)
    assert job == "Engineer"
    assert age == 25
    assert name == "Alice"


def test_swap_variables():
    x, y = exercises.swap_variables(15, 100)
    assert x == 100
    assert y == 15


def test_max_and_min():
    numbers = (4, 7, 1, 19, 3, -1)
    max_val, min_val = exercises.max_and_min(numbers)
    assert max_val == 19
    assert min_val == -1


def test_return_as_str():
    likes = ("I", "like", "to", "eat", "applea", "and", "bananas.")
    assert exercises.return_as_str(likes) == "I like to eat apples and bananas."


def test_common_elements():
    t1 = (1, 2, 3, 4, 5, 13, 15, 20)
    t2 = (3, 4, 5, 6, 7, 13, 18, 29)
    assert exercises.common_elements(t1, t2) == (3, 4, 5, 13)

