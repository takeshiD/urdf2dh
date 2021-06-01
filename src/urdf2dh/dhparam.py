import numpy as np
from typing import Tuple
from nptyping import NDArray

EPSILON = 10e-8
# Sequence
# n-joints
# 1. compute ai, xi (i=0, ..., n-1)
# 2. compute alpha_i (i=0, ..., n-1)
# 3. compute d and theta

class DH:
    def __init__(self, n):
        self.dhparams = [
            namedtuple("dh", "a", "alpha", "d", "theta", "origin") for _ in range(n)
        ]            
    def 

def get_dh_parameter(z, p):
    n = len(z)
    dh = 
    a = np.zeros(n-1)
    cn = np.zeros(n-1,3))
    for i in range(n-1):
        _a, _parallel, _cp1, _cp2 = get_a(z[i], z[i+1], p[i], p[i+1]
        a[i] = _a
        cn[i] = _cp1
    alpha
    d = np.zeros(n-1)


    for i in range(n-1):
    
    return dh

def get_a(z1:NDArray[3,float], z2:NDArray[3,float], p1:NDArray[3,float],p2:NDArray[3,float]) -> Tuple[float,NDArray[3,float],NDArray[3,float]]:
    """NDArray[3
    Parameters
    --------
    z1 : array_like(3)
        direction vector of z1 axis on cartecian coordinate
    z2 : array_like(3)
        direction vector of z2 axis on cartecian coordinate
    p1 : array_like(3)
        point through z1 axis line on cartecian coordinate
    p2 : array_like(3)
        point through z2 axis line on cartecian coordinate

    Returns
    --------
    a : float
        The length of straight lines perpendicular 
        from the z1 axis to the z2 axis.
    parallel : bool
        z1 and z2 are parallel or not parallel.
    cp1: numpy.array(3,)
    cp2: numpy.array(3,)

    Raises
    --------

    """
    z1 = np.array(z1)
    z2 = np.array(z2)
    p1 = np.array(p1)
    p2 = np.array(p2)
    if any([x.shape!=(3,) for x in [z1,z2,p1,p2]]):
        raise ValueError("imcomaptible dimensions. dimension must be 3")
    if any([np.linalg.norm(x)==0 for x in [z1,z2]]):
        raise ValueError("direction vector(u1 or u2) is zero. must be non-zero")

    # normalize
    z1 = z1/np.linalg.norm(z1)
    z2 = z2/np.linalg.norm(z2)

    cosz = np.dot(z1,z2)
    if cosz<=EPSILON:
        cosz = 0.0
    det = 1-cosz**2
    if det<=EPSILON:
        det = 0.0
    b = np.array([np.dot(p2-p1, z1), np.dot(p2-p1, z2)])
    if det!=0.0:
        # z1,z2 are not parallel, skew or intersection
        Ainv = (1.0/det)*np.array([
            [-np.dot(z2,z2), np.dot(z1,z2)],
            [-np.dot(z1,z2), np.dot(z1,z1)]
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
    return a, parallel, cp1, cp2
    
def get_alpha(z1:NDArray[3,float], z2:NDArray[3,float]) -> float:
    z1 = np.array(z1)
    z2 = np.array(z2)
    if any([x.shape!=(3,) for x in [z1,z2]]):
        raise ValueError("imcomaptible dimensions. dimension must be 3")
    if any([np.linalg.norm(x)==0 for x in [z1,z2]]):
        raise ValueError("direction vector(u1 or u2) is zero. must be non-zero")

    # normalize
    z1 = z1/np.linalg.norm(z1)
    z2 = z2/np.linalg.norm(z2)

    alpha = np.acos(np.dot(z1, z2))
    return alpha

def get_d_theta(z1:NDArray[3,float], x1:NDArray[3,float], p1:NDArray[3,float], o1:NDArray[3,float], x2:NDArray[3,float]) -> Tuple[float,NDArray[3,float],NDArray[3,float]]:
    z1 = np.array(z1)
    x1 = np.array(x1)
    p1 = np.array(p1)
    o1 = np.array(o1)
    if any([x.shape!=(3,) for x in [z1,x1,p1,o1,x2]]):
        raise ValueError("imcomaptible dimensions. dimension must be 3")
