import typing


## Importing modules necessarily take some time, but how much?

''' Measuring import time using perf
echo "import typing" > import_typing.py
echo "" > empty_file.py
sudo perf stat -r 1000 python3 import_typing.py
sudo perf stat -r 1000 python3 empty_file.py
'''

''' Measuring import time using timeit
python3 -m timeit "import typing"
python3 -m timeit -n 1 -r 1 "import typing"
'''

''' Measuring import time using option: importtime
python3 -X importtime import_typing.py
'''