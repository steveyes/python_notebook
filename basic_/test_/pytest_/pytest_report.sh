#!/usr/bin/env bash

export PYTHONPATH="/home/$(whoami)/gitrepo/python_example"

# install pytest-html
#pip install -U pytest-html


pytest --junit-xml=report.xml