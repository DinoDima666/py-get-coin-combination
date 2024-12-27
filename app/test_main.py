from app.main import get_coin_combination

def test_no_coin() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_min_value() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_only_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_return_penny_and_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_penny_nickel_and_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_only_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]

def test_lage() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]
