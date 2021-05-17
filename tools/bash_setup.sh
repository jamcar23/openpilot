#!/bin/bash -e

# install pyenv
if ! command -v "pyenv" > /dev/null 2>&1; then
  curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
fi

# install python
pyenv install -s 3.8.5
pyenv global 3.8.5
pyenv rehash
eval "$(pyenv init -)"

# **** in python env ****

# upgrade pip
pip install --upgrade pip==20.2.4

# install pipenv
pip install pipenv==2020.8.13

# pipenv setup (in openpilot dir)
pipenv install --dev --system --deploy
