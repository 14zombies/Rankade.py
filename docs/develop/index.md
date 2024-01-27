# Develop

As much as possible the configuration lives in pyproject.toml.

## Installing from source
```zsh
git clone https://github.com/14zombies/Rankade.py
cd rankade.py
pip3 install '.[dev]'
```

### Available optional dependencies
> To install run `$ pip3 install '.[all]'`{l=zsh}

[dev]
: Packages for building package.

[docs]
: Packages for building documentation.

[tests] 
: Packages for running tests.

[all] 
: All of the above.


## Building docs
Docs built using Sphinx, MyST, & autodoc2, configuration for those lives in docs/conf.py.

```zsh
git clone https://github.com/14zombies/Rankade.py
cd rankade.py
pip3 install '.[docs]'
make docs
```

## Running tests
Tests built using unittest.

```zsh
git clone https://github.com/14zombies/Rankade.py
cd rankade.py
pip3 install '.[tests]'
make tests
```

## Generating Coverage Reports
```zsh
git clone https://github.com/14zombies/Rankade.py
cd rankade.py
pip3 install '.[dev]'
make coverage
```