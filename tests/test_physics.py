import pytest

from src.physics import time_of_flight, max_height, range_projectile
from src.validation import validate_velocity
from src.validation import validate_velocity, validate_angle
from simulations.projectile import generate_trajectory

def test_time_of_flight():
    result = time_of_flight(20, 45)
    assert result == pytest.approx(2.88, abs=0.01)


def test_max_height():
    result = max_height(20, 45)
    assert result == pytest.approx(10.19, abs=0.01)


def test_range_projectile():
    result = range_projectile(20, 45)
    assert result == pytest.approx(40.77, abs=0.01)

def test_validate_negative_velocity():
    with pytest.raises(ValueError):
        validate_velocity(-20)


def test_validate_velocity():
    assert validate_velocity(20) is True

def test_validate_negative_velocity():
    with pytest.raises(ValueError):
        validate_velocity(-20)


def test_validate_non_numeric_velocity():
    with pytest.raises(TypeError):
        validate_velocity("20")

def test_validate_angle():
    assert validate_angle(45) is True


def test_validate_invalid_angle():
    with pytest.raises(ValueError):
        validate_angle(120)


def test_validate_non_numeric_angle():
    with pytest.raises(TypeError):
        validate_angle("45")

def test_generate_trajectory():
    t, x, y = generate_trajectory(20, 45)

    assert len(t) == 100
    assert len(x) == 100
    assert len(y) == 100

    assert t[0] == pytest.approx(0)
    assert x[0] == pytest.approx(0)
    assert y[0] == pytest.approx(0)

    assert y[-1] == pytest.approx(0, abs=0.01)        