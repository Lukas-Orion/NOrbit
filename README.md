[![codecov](https://codecov.io/gh/Lukas-Orion/NOrbit/graph/badge.svg?token=ZR0LVVUXDU)](https://codecov.io/gh/Lukas-Orion/NOrbit)
# NOrbit
NOrbit is a Python package designed for simulating the N-body problem using a Runge-Kutta 4th order integration scheme. The code provides functions for converting between Keplerian and Cartesian coordinates, calculating accelerations, calculating derivatives, and simulating the orbits of objects in an N-body system.

## Installation
Clone the repository and install the required dependencies using the following commands:
```sh
git clone https://github.com/your_username/your_repository.git
cd your_repository
pip install
```

## Usage

Here's an example of how to use the NOrbit package:
```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from src.NOrbit import NOrbit, Object
```

```python
planets_solar_system = Object.planets_solar_system # list of orbital elements and masses of solar system planets
ss_names = Object.planets_solar_system_names # names of solar system planets

m_sun = 1.0 # mass of sun in solar masses

solar_system = NOrbit(object_elements = planets_solar_system, m_primary = m_sun) # base model of solar system
```

```python
dt = 1/100 # time-step of integration
n_orbits = 1000 # number of orbits of first planet (Merkury) around Sun

solar_system_positions = solar_system.orbit(dt = dt, n_orbits = n_orbits)[0] # orbital position calculations for planets and Sun

fig = plt.figure(figsize = (10, 10))
ax = plt.axes(projection = "3d")

# position of Sun
ax.plot3D(solar_system_positions[:, 0, 0], solar_system_positions[:, 0, 1], solar_system_positions[:, 0, 2], "*", color = "yellow", label = "Sun")

for i in range(len(planets_solar_system)):
    # orbital position evolution of planets
    ax.plot3D(solar_system_positions[:, i + 1, 0], solar_system_positions[:, i + 1, 1], solar_system_positions[:, i + 1, 2], label = f"{ss_names[i]}")

ax.set_title(f"Orbit of Planets around Sun with dt = {dt}", fontsize = 15)
ax.set_xlabel("x [AU]", fontsize = 15)
ax.set_ylabel("y [AU]", fontsize = 15)
ax.set_zlabel("z [AU]", fontsize = 15)
ax.set_zlim3d(-30, 30) # z-axis scaled
ax.legend(loc = "center left", bbox_to_anchor = (1, 0.5))
plt.show()
```

## Objects
    Object.mercury
    Object.venus
    Object.earth
    Object.mars
    Object.jupiter
    Object.saturn
    Object.uranus
    Object.neptune
### Grouped Objects
    Object.planets_solar_system
    Object.planets_solar_system_names
    
    Object.planets_inner_solar_system
    Object.planets_inner_solar_system_names
    Object.planets_outer_solar_system
    Object.planets_outer_solar_system_names

## Basics
### before working
git fetch\
git pull origin
### after working
git add . \
git commit -m 'Commit Message' \
git push
### overwriting local changes
git fetch --all \
git branch backup \
git reset --hard origin
### Pull request
git checkout -b new-branch \
*make changes* \
git add . \
git commit -m 'Commit Message' \
git push origin new-branch \
*create pull request* \
*merge pull request*
### Change Branch
git checkout branch-name

## To-Do
check if works directly from PyPi

### Update PyPi 
 - Delete all files in the dist folder
 - Update the version number
 - python -m build
 - python -m twine upload -p "<your_password>" dist/*

### Edit and test Example Notebook 
 - maybe add solar system bodies as preset? (so you can just type eg. NOrbit.earth or NOrbit.bodies / objects)

Edit the README 
### Check Assessment Criteria
