import pytest
import numpy as np
from urdf2dh.type import Vec3f
from typing import Tuple
from urdf2dh.dhparam import get_a, get_alpha, get_d_theta


@pytest.mark.parametrize(('inputed', 'expected'), [
    (tuple(np.array([0, 0, 1]),
           np.array([0, 0, 1]),
           np.array([0, 0, 0]),
           np.array([1, 1, 1]),
           ),
     tuple(0,
           True,
           np.array([0, 0, 0]),
           np.array([0, 0, 0]),
           )
     )
])
def test_get_a(
    inputed: Tuple[Vec3f, Vec3f, Vec3f, Vec3f],
    expected: Tuple[float, bool, Vec3f, Vec3f]
):
    assert get_a(*inputed) == expected


@pytest.mark.parametrize(('inputed', 'expected'), [
    (tuple(np.array([0, 0, 1]),
           np.array([0, 0, 1]),),
     0.0,
     )
])
def test_get_alpha(
    inputed: Tuple[Vec3f, Vec3f],
    expected: float
):
    assert get_alpha(*inputed) == expected


@pytest.mark.parametrize(('inputed', 'expected'), [
    (tuple(np.array([0, 0, 1]),
           np.array([0, 0, 1]),
           np.array([0, 0, 0]),
           np.array([1, 1, 1]),
           ),
     tuple(0,
           True,
           np.array([0, 0, 0]),
           np.array([0, 0, 0]),
           )
     )
])
def test_get_d_theta(
    inputed: Tuple[Vec3f, Vec3f, Vec3f, Vec3f],
    expected: Tuple[float, bool, Vec3f, Vec3f]
):
    assert get_d_theta(*inputed) == expected
