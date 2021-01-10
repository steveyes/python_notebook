#!/usr/bin/bash

export PYTHONPATH="/home/$(whoami)/gitrepo/python_example"

# install coverage
# pip install -U coverage

# collect data
coverage run test_app.py &>/dev/null
echo "----------------------------------------------------------------------"

# run report
coverage report -m