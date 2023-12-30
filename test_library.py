import pytest

import library


def test_can_convert():
    result = library.converter(3)
    assert result


def test_can_convert_negative():
    result = library.converter(-3)
    assert result


def test_can_not_convert():
    with pytest.raises(ValueError):
        library.converter(0.03)
