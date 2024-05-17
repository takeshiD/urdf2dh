import pytest
import numpy as np
from urdf2dh.type import Vec3f
from urdf2dh.dhparam import get_a
from typing import Tuple

ATOL = 1.e-8


@pytest.mark.parametrize(('inputed', 'expected'), [
    ((np.array([0, 0, 1]),  # paralleled z1 and z2
      np.array([0, 0, 1]),
      np.array([0, 0, 0]),
      np.array([0, 1, 0]),),
     (1.0, True, np.array([0, 0, 0]), np.array([0, 1, 0]),)),
    ((np.array([0, 0, 1]),  # paralleled z1 and z2
      np.array([0, 0, 1]),
      np.array([0, 0, np.sqrt(5)]),
      np.array([0, 1, -np.sqrt(99)]),),
     (1.0, True, np.array([0, 0, 0]), np.array([0, 1, 0]),))
])
def test_get_a(
    inputed: Tuple[Vec3f, Vec3f, Vec3f, Vec3f],
    expected: Tuple[float, bool, Vec3f, Vec3f]
):
    actuals = get_a(*inputed)
    assert np.allclose(actuals[0], expected[0], atol=ATOL)
    assert actuals[1] == expected[1]
    assert np.allclose(actuals[2], expected[2], atol=ATOL)
    assert np.allclose(actuals[3], expected[3], atol=ATOL)


# @pytest.mark.parametrize(('inputed', 'expected'), [
#     (tuple(np.array([0, 0, 1]),
#            np.array([0, 0, 1]),),
#      0.0,
#      )
# ])
# def test_get_alpha(
#     inputed: Tuple[Vec3f, Vec3f],
#     expected: float
# ):
#     assert get_alpha(*inputed) == expected


# @pytest.mark.parametrize(('inputed', 'expected'), [
#     (tuple(np.array([0, 0, 1]),
#            np.array([0, 0, 1]),
#            np.array([0, 0, 0]),
#            np.array([1, 1, 1]),
#            ),
#      tuple(0,
#            True,
#            np.array([0, 0, 0]),
#            np.array([0, 0, 0]),
#            )
#      )
# ])
# def test_get_d_theta(
#     inputed: Tuple[Vec3f, Vec3f, Vec3f, Vec3f],
#     expected: Tuple[float, bool, Vec3f, Vec3f]
# ):
#     assert get_d_theta(*inputed) == expected
