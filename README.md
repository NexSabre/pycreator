# pycreator
Create boilerplate application thru the command-line!

## TLDR; 
```
pip install pycreator       # to install pycreator
pycreator goes -n brrr      # where brr is the name
```

It create a command line, Python application with structure:
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