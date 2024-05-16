import pytest
from urdf2dh.matrix import (
    _RotX, _RotY, _RotZ,
    Rot, Trans, homogeneous_transformation_matrix
)
from urdf2dh.type import Mat4f
import numpy as np

ATOL = 1.e-8


@pytest.mark.parametrize(('theta', 'expected'), [
    (0, np.eye(4)),
    (2*np.pi, np.eye(4)),
])
def test_RotXYZ(theta: float, expected: float):
    assert np.allclose(_RotX(theta), expected, atol=ATOL)
    assert np.allclose(_RotY(theta), expected, atol=ATOL)
    assert np.allclose(_RotZ(theta), expected, atol=ATOL)


@pytest.mark.parametrize(('roll', 'pitch', 'yaw', 'expected'), [
    (0, 0, 0, np.eye(4)),
    (2*np.pi, 2*np.pi, 2*np.pi, np.eye(4)),
    (np.pi, np.pi, np.pi, np.eye(4))
])
def test_Rot(roll: float, pitch: float, yaw: float, expected: Mat4f):
    assert np.allclose(Rot(roll, pitch, yaw), expected, atol=ATOL)


@pytest.mark.parametrize(('x', 'y', 'z', 'expected'), [
    (0, 0, 0, np.eye(4)),
])
def test_Trans(x: float, y: float, z: float, expected: Mat4f):
    assert np.allclose(Trans(x, y, z), expected, atol=ATOL)


@pytest.mark.parametrize('a,alpha,d,theta,expected', [
    (0, 0, 0, 0, np.eye(4))
])
def test_homogeneous_transformation_matrix(
        a: float, alpha: float, d: float, theta: float,
        expected: Mat4f
):
    assert np.allclose(
        homogeneous_transformation_matrix(a, alpha, d, theta),
        expected
    )
