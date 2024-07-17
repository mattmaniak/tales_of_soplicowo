# Tales of Soplicowo

Use the third-person camera with the Panda3D and the "Tales of Soplicowo" game wannabe project.

![image](main_screenshot.png "Tales of Soplicowo main screenshot")

## Descrption

A more sophisticated RoamingRalphDemo. Extracted from the discontinued Kultakoulu Software's original RPG game project. Fully working third-person camera with a customizable relative position. The Witcher 1's styled. Contains also a player that can walk or run on a terrain.

## Requirements

- At least **Python 3.12**. The version used for the development. Newer versions will work. Older versions may work but I don't guarantee anything.
- At least **Panda3D 1.10**. As above, it is the minimum version used for the development.

## Usage

**Warning!** There is an issue with a mouse cursor on macOS. A cursor appears outside the game window making an input and the camera uncontrollable. 

### Prepare

Use [venv](https://docs.python.org/3/library/venv.html) to enter a virtual environment.

```shell
python3 -m venv .venv &&
source .venv/bin/activate &&
python3 -m pip install -r python_deps.txt
```

### Run

```shell
cd src/main.py
```


Move the character and look around using the WSAD keys and a mouse. Toggle run or walk by hitting the Shift key. Escape button will exit the app.

## Useful resources

- [Panda3D tutorial](https://github.com/fireclawthefox/panda3d-tutorial).

### [AtiByte's](https://www.youtube.com/@atibyte) YouTube tutorial playlists for Panda3D

- [Panda3D GLSL shaders](https://www.youtube.com/playlist?list=PL1P11yPQAo7p7rwLfMYvcxdzRBLwue7O2).
- [Panda3D game prototypes](https://www.youtube.com/playlist?list=PL1P11yPQAo7rMvtIxF1kedMQOacdXxr-e).
- [Panda3D model loading](https://www.youtube.com/playlist?list=PL1P11yPQAo7r198TGKomijJpwZGWO3EUg).
- [Panda3D tutorials](https://www.youtube.com/playlist?list=PL1P11yPQAo7oEAGuPcqMnn9ZWHLWP3-Lc).

## Coding rules

- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).
- [PEP 20 -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/).
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/).
- [Semantic Versioning](https://semver.org).

## Optional tools

- [flake8](https://pypi.org/project/flake8/) for static code analysis.
