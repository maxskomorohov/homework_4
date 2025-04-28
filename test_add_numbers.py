import pytest

def add_numbers(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (-2, 3, 1),
    (0, 0, 0)
], ids=[
    "add 2 positive numbers",
    "add 2 negative numbers",
    "add negative and positive numbers",
    "add zeroes"
])
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected


if __name__ == "__main__":
    test_add_numbers()
