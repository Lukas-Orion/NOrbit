[![codecov](https://codecov.io/gh/Lukas-Orion/NOrbit/graph/badge.svg?token=ZR0LVVUXDU)](https://codecov.io/gh/Lukas-Orion/NOrbit)
# NOrbit
N-body integrator

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
