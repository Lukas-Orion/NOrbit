import sys
path = "/home/informatik2020/NOrbit/NOrbit"
sys.path.append(path)

import numpy as np
from NOrbit import kepToCart

def test_kepToCart():
    planet_elements = [np.array((1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))]
    M_star = 1.0
    pos = kepToCart(planet_elements[0], M_star)[0]
    vel = kepToCart(planet_elements[0], M_star)[1]
    #result = np.array([pos, vel])
    result = np.round(vel[1], 4)
    #assert result == np.array([[1.0, 0.0, 0.0], [0.0 , 0.0172021, 0.0]])
    assert result == 0.0172