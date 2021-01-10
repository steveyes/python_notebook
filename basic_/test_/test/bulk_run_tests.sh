#!/usr/bin/bash

export PYTHONPATH="/home/$(whoami)/gitrepo/python_example"

function hint() {
    echo "======================================================================"
    echo "run $1 unittest"
}

# run test for all test_*.py in the subdir
cd ..
python -m unittest discover -v -p test_*.py