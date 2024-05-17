import numpy as np
from typing import Tuple
from .type import Mat4f, Vec3f

EPSILON = 10e-8
# Sequence
# n-joints
# 1. compute ai, xi (i=0, ..., n-1)
# 2. compute alpha_i (i=0, ..., n-1)
# 3. compute d and theta


# class DH: def __init__(self, n):
#         self.dhparams = [
#             namedtuple("dh", "a", "alpha", "d", "theta", "origin") for _ in range(n)
#         ]


# def get_dh_parameter(z, p):
#     n = len(z)
#     # dh =
#     a = np.zeros(n-1)
#     cn = np.zeros(n-1, 3)
#     for i in range(n-1):
#         _a, _parallel, _cp1, _cp2 = get_a(z[i], z[i+1], p[i], p[i+1])
#     a[i] = _a
#     cn[i] = _cp1
#     # alpha
#     d = np.zeros(n-1)
#     # for i in range(n-1):

#     return dh


def get_a(
    z1: Vec3f, z2: Vec3f,
    p1: Vec3f, p2: Vec3f
) -> Tuple[float, Vec3f, Vec3f]:
    """Calculate shortest length `a` and intersections between joint and joint.

    Parameters
    --------
    z1 : array_like(3)
        direction vector of z1 axis on cartecian coordinate
    z2 : array_like(3)
        direction vector of z2 axis on cartecian coordinate
    p1 : array_like(3)
        a point through z1 axis line on cartecian coordinate
    p2 : array_like(3)
        a point through z2 axis line on cartecian coordinate

    Returns
    --------
    a : float
        The length of straight lines perpendicular
        from the z1 axis to the z2 axis.
    parallel : bool
        z1 and z2 are parallel or not parallel.
    cp1: numpy.array(3)
    cp2: numpy.array(3)
        Intersections of the perpendicular line from the shortest
        distance between the line l1 and l2.
        cp1 is intersection on l1, cp2 is intersection on l2.
        Note: l1 is line formed by z1 and p1, l2 is line formed by z2 and p2.

    Raises
    --------

    Examples
    --------

    """
    z1 = np.array(z1)
    z2 = np.array(z2)
    p1 = np.array(p1)
    p2 = np.array(p2)
    if any([x.shape != (3,) for x in [z1, z2, p1, p2]]):
        raise ValueError("imcomaptible dimensions. dimension must be 3")
    if any([np.linalg.norm(x) == 0 for x in [z1, z2]]):
        raise ValueError(
            "direction vector(u1 or u2) is zero. must be non-zero")

    # normalize
    z1 = z1/np.linalg.norm(z1)
    z2 = z2/np.linalg.norm(z2)

    cosz = np.dot(z1, z2)
    if cosz <= EPSILON:
        cosz = 0.0
    det = 1-cosz**2
    if det <= EPSILON:
        det = 0.0
    b = np.array([np.dot(p2-p1, z1), np.dot(p2-p1, z2)])
    if det != 0.0:
        # z1,z2 are not parallel, skew or intersection
        Ainv = (1.0/det)*np.array([
            [-np.dot(z2, z2), np.dot(z1, z2)],
            [-np.dot(z1, z2), np.dot(z1, z1)]
        ])

        s = np.dot(Ainv, b)
        parallel = False
    else:
        # z1,z2 are parallel
        s = np.array([b[0], 0.0])
        parallel = True

    cp1 = p1+s[0]*z1
    cp2 = p2+s[1]*z2
    a = np.linalg.norm(cp1-cp2)
    return (a, parallel, cp1, cp2)


def get_alpha(z1: Vec3f, z2: Vec3f) -> float:
    z1 = np.array(z1)
    z2 = np.array(z2)
    if any([x.shape != (3,) for x in [z1, z2]]):
        raise ValueError("imcomaptible dimensions. dimension must be 3")
    if any([np.linalg.norm(x) == 0 for x in [z1, z2]]):
        raise ValueError(
            "direction vector(u1 or u2) is zero. must be non-zero")

    # normalize
    z1 = z1/np.linalg.norm(z1)
    z2 = z2/np.linalg.norm(z2)

    alpha = np.acos(np.dot(z1, z2))
    return alpha


def get_d_theta(z1: Vec3f, x1: Vec3f, p1: Vec3f, o1: Vec3f, x2: Vec3f) -> Tuple[float, Vec3f, Vec3f]:
    z1 = np.array(z1)
    x1 = np.array(x1)
    p1 = np.array(p1)
    o1 = np.array(o1)
    if any([x.shape != (3,) for x in [z1, x1, p1, o1, x2]]):
        raise ValueError("imcomaptible dimensions. dimension must be 3")
