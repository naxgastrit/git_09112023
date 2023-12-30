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


# def test_can_drive_car():
#     result = library.can_drive_car(55)
#     assert result is True
#
#
# def test_not_can_drive_car_min():
#     with pytest.raises(ValueError):
#         library.can_drive_car(-555)
#
#
# def test_can_drive_car_max():
#     with pytest.raises(ValueError):
#         library.can_drive_car(555)
