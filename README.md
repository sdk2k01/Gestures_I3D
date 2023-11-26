# Gestures_I3D
Desktop application to control functionalities using hand-gestures.

## Dependencies

- Python 3.6 or above ( ideally python 3.10+ )
<br><i>NOTE:</i> It is recommended NOT to use python 3.12 as some packages (e.g: distutils) are deprecated which
may affect installation of other packages. Python v3.10.11 was the latest 'stable' version which tested successfully.

## Installation Steps

### 1. Create a Virtual Environment

```zsh
python3 -m venv ./venv
```

 - Alternatively, any other suitable way to create a virtual environment ( such as `virtualenv` or `conda` ) can be used as per convenience.

 ### 2. Activate the Virtual Environment

 - `zsh` or `bash`

 ```zsh
source ./venv/bin/activate
 ```

 - or, for Windows users, `pwsh`

 ```zsh
./venv/Scripts/Activate
 ```


### 3. Install all Required Packages

```zsh
python3 -m pip install requirements.txt
```

## Contributing to this Project

For contribution guidelines, check out our [contributing page](https://github.com/sdk2k01/Gestures_I3D/blob/main/CONTRIBUTING.md).
