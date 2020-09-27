# pycreator
Create boilerplate application thru the command-line!

## TLDR; 
```
pip install pycreator       # to install pycreator
pycreator goes brrr         # where brr is the name
```

## Usage

### create
This command allow to create a Python boilerplate application with the structure as showed below.
Available commands for `create`:
```
-n, --name      -- application name (required)
-l, --location  -- location to create a new package. If none it will create at working directory
```

Structure of example application named `brrr`
```
brrr
│   LICENSE.md
│   README.md
│   VERSION
│
└───src
    └───brrr
        │   setup.py
        │   __init__.py
        │
        ├───actions
        │   │   action.py
        │   │   action_dispatcher.py
        │   │   version.py
        │   │   __init__.py
        │   │
        │   └───example_action
        │           example_action.py
        │           __init__.py
        │
        ├───core
        │       __init__.py
        │
        ├───framework
        │       messages.py
        │       __init__.py
        │
        └───main
                main.py
                __init__.py
```

## Build
Boilerplate app comes with preconfigured `setup.py` file which allow to create a `.whl` package.
To build a package, go to `src` dir a type in the terminal:
```
pip install setuptools wheel
python setup.py sdist bdist_wheel
```
After operation in the newly created dir `dist/` you should find a `*.tar.gz` & `*.whl` packages.
