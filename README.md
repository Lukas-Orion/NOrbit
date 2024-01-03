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
Ask Prash about google docstring return functions 

add a if __name__ == __main__ \
typing for checking the input type (pydantic) \
Pull requests! 

### Update PyPi 
 - Delete all files in the dist folder
 - Update the version number
 - python -m build
 - python -m twine upload -p "<your_password>" dist/*

### Edit and test Example Notebook 
 - import functions directly from NOrbit (without redefining it)
 - maybe add solar system bodies as preset? (so you can just type eg. NOrbit.earth or NOrbit.bodies / objects)

Edit the README 
### Check Assessment Criteria
