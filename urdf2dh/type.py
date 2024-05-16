from nptyping import NDArray, Float, Shape
from typing import TypeAlias

Mat4f: TypeAlias = NDArray[Shape["4, 4"], Float]
Vec3f: TypeAlias = NDArray[Shape["3"], Float]
