import pytest
from app.stats import mean, max_value, min_value


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_max():
    assert max_value([1, 5, 3]) == 5


def test_min():
    assert min_value([1, 5, 3]) == 1


def test_empty_list():
    with pytest.raises(ValueError):
        mean([])