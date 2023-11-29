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
    positions = np.array([1.0, 1.0, 0.0], [0.0, 0.0, 0.0])
    masses = np.array([1e-5], [1.0])

    result = NOrbit.calculate_acceleration(positions, masses)
    #assert
    print(result)

test_calculate_acceleration()

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