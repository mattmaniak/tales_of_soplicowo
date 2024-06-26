Use the third-person camera with the Panda3D and the "Tales of Soplicowo" game
wannabe project.

![image](screenshot.png "Tales of Soplicowo screenshot")

## Descrption

A more sophisticated RoamingRalphDemo. Extracted from the discontinued
Kultakoulu Software's original RPG game project. Fully working third-person
camera with a customizable relative position. The Witcher 1's styled. Contains
also a player that can walk or run on a terrain.

## Requirements

- At least **Python 3.12**
The version used for the development. Newer versions will work. Older versions
may work but I don't guarantee anything.
- At least **Panda3D 1.10**
As above, version used for the development.

## Usage

### Prepare

https://docs.python.org/3/library/venv.html

```shell
python3 -m venv .venv &&
source .venv/bin/activate &&
python3 -m pip install -r pip_packages.txt
```

### Run

```shell
cd src &&
./main.py
```

Then move and look around using the WSAD keys and a mouse. Toggle run or walk
by hitting the Shift key. Escape button will exit the app.

## Useful resources

- **Panda3D tutorial**
(https://github.com/fireclawthefox/panda3d-tutorial)

## Coding rules

- **PEP 20 -- The Zen of Python** (https://www.python.org/dev/peps/pep-0020/)
- **PEP 8 -- Style Guide for Python Code**
(https://www.python.org/dev/peps/pep-0008/)
- **PEP 257 -- Docstring Conventions**
(https://www.python.org/dev/peps/pep-0257/)
- **Semantic Versioning**
(https://semver.org)

## Optional tools

- **the modular source code checker: pep8, pyflakes and co**
(https://pypi.org/project/flake8/)
