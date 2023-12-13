import sys
path = "NOrbit"
sys.path.append(path)

import numpy as np
import NOrbit
import pytest


def test_kepToCart():
    planet_elements = np.array((1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-5))
    mass_star = 1.0

    result = NOrbit.kepToCart(planet_elements, mass_star)
    pos = np.array((1., 0., 0.))
    vel = np.array((0., 0.017, 0.))

    assert pytest.approx(result[0], 0.1) == pos
    assert pytest.approx(result[1], 0.1) == vel

def test_cartToKep():
    positions = np.array((1.0, 1.0, 0.0))
    velocities = np.array((0.1, 0.1, 0.0))
    mass_planet = 1e-5
    mass_star = 1.0

    result = NOrbit.cartToKep(positions, velocities, mass_star, mass_planet)
    assert pytest.approx(result, 0.1) == (0.0, 1.0, 0.0, 225.0, 0, 180.0, 1e-05)

def test_calculate_acceleration():
    positions = np.array([[ 4.24986205e-03, -2.16147702e-03, -7.22871314e-05],
                        [-9.69141616e-01, -2.45313757e-01, -7.05363499e-05],
                        [-4.45076172e+00,  2.26600558e+00,  7.57570172e-02]])
    masses = np.array([ 1.000e+00, 3.039e-06, 9.542e-04])

    result = NOrbit.calculate_acceleration(positions, masses)
    assert pytest(result) == np.array([[ -1.09315857e-08,  4.90777799e-09,  1.71316619e-10],
                                        [ 2.85191816e-04,  7.12527106e-05, -2.42462946e-10],
                                        [ 1.05479855e-05, -5.37027351e-06, -1.79538757e-07]])


'''
def test_calculate_derivatives():

    assert

def test_move_to_barycenter():

    assert

def test_rk4_n_body():

    assert

def test_orbit():

    assert
'''
