# Toshies

Toshies is a Python library with modules and scripts to create a random Pandas dataframe. 

### Installation

Change directory to where you would like to clone the repository, for example to your `dev` directory.

```bash
$ cd ~/dev/
$ git clone git@github.com:sabinescheffer/toshies.git
```

Create a virtual environment inside the root of the repository and activate it.

```bash
$ cd toshies
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Make sure to install the repo requirements.

```bash
$ pip install -r requirements.txt
```

### Setup

Now run setup.py to install modules from repository.
```bash
$ python setup.py develop
```
Finally, create a `data` folder so that data outputs from scripts can be stored locally.
```bash
$ mkdir data
```
