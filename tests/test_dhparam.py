import pytest
from tik.urdf import _calculate_a
import numpy as np

@pytest.mark.parametrize(('u1,u2,p1,p2,expected'),[
    ([0,0,1],[0,0,1],[0,0,0],[0,0,0.13156], 0.0),
])
def test_calculate_a(u1,u2,p1,p2,expected):
    assert _calculate_a(u1,u2,p1,p2)==expected