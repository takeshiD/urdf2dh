import numpy as np
from nptyping import NDArray

def _RotZ(roll: float) -> NDArray[(4,4), float]:
    c = np.cos(roll)
    s = np.sin(roll)
    return np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
        ])

def _RotY(pitch: float) -> NDArray[(4,4), float]:
    c = np.cos(pitch)
    s = np.sin(pitch)
    return np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1]
        ])
def _RotX(yaw: float) -> NDArray[(4,4), float]:
    c = np.cos(yaw)
    s = np.sin(yaw)
    return np.array([
        [1, 0,  0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0,  0, 1]
        ])

def Rot(roll:float, pitch:float, yaw:float) -> NDArray[(4,4), float]:
    tmp = np.dot(_RotZ(roll), _RotY(pitch))
    return np.dot(tmp, _RotX(yaw))

def Trans(x:float,y:float,z:float)->NDArray[(4,4), float]:
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

def homogeneous_transformation_matrix(a:float, alpha:float, d:float, theta:float)->NDArray[(4,4),float]:
    """Compute homogeneous transformation matrix based on Modified DH comvention.
    In this function, homogeneous transformation matrix is computed bellow following
    T^{i-1}_{i} = Trans(a,0,0)*RotX(alpha)*Trans(0,0,d)*RotZ(theta)

    Parameters
    --------
    a : float
        The length of straight lines perpendicular 
        from the z_{i-1} axis to the z_{i} axis.
    alpha : float
        The angle between the z_{i-1} axis and the z_{i} axis.
    d : float
        The length between i-1 coordinate origin O_{i-1} and i coordinate origin O_{i}
        when translate direction z axis.
    theta : float
        The angle at which x_{i-1} axis and x_{i} axis match 
        when rotated around z_{i-1} axis

    Returns
    --------
    numpy.ndarray(4,4) : homogeneous transformation matrix

    Raises:
    --------
    ValueError
    """
    ta = Trans(a, 0, 0)
    rx = _RotX(alpha)
    td = Trans(0, 0, d)
    rz = _RotZ(theta)

    ret = np.eye(4)
    ret = np.dot(ret, ta)
    ret = np.dot(ret, rx)
    ret = np.dot(ret, td)
    ret = np.dot(ret, rz)
    return ret