#!/usr/bin/env bash



# cli
pydoc3 sys

# gui window
python3 -m pydoc -b -p 8000


# py cli
echo "help('sys')" | python | less

# py cli
python3 -c "import sys; help(sys)"
echo "import sys; print(sys.__doc__); " | python | less
echo "modules sys" | python3 -c "help()"
