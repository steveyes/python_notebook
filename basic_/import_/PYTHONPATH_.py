"""sys.path
A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH,
plus an installation-dependent default.

As initialized upon program startup, the first item of this list, path[0], is the directory containing the script
that was used to invoke the Python interpreter. If the script directory is not available (e.g.
if the interpreter is invoked interactively or if the script is read from standard input),
path[0] is the empty string, which directs Python to search modules in the current directory first.
Notice that the script directory is inserted before the entries inserted as a result of PYTHONPATH.

A program is free to modify this list for its own purposes. Only strings and bytes should be added to sys.path;
all other data types are ignored during import.

"""

import subprocess
from os import sys, path
from textwrap import dedent
import tempfile

PROJECT_NAME = 'python_example'


def get_pathname_backwardly(path_name, file_name):
    _path, _ = path.split(path_name)
    if _path.endswith(file_name):
        return _path
    else:
        return get_pathname_backwardly(_path, file_name)


def set_env_in_app():
    _current_file_path: str = path.abspath(__file__)
    project_path = get_pathname_backwardly(_current_file_path, PROJECT_NAME)
    sys.path.append(project_path)
    print(sys.path)


def set_env_from_shell():
    """sample
    use in production do not permitted"""

    cmd_stmt = dedent("""\
    #!/usr/bin/env bash
    
    # before PYTHONPATH
    python -c 'import sys; print(sys.path);'
    
    PROJECT_NAME='python_example'
    _current_file_path=$(realpath $0)
    
    # after PYTHONPATH
    project_path=${_current_file_path%$PROJECT_NAME*}${PROJECT_NAME}
    PYTHONPATH=$project_path python -c 'import sys; print(sys.path);'
    """)

    tmp_fd, tmp_fn = tempfile.mkstemp(suffix='.sh', text=True, dir='.')
    with open(tmp_fn, 'w+') as _f:
        _f.write(cmd_stmt)
        subprocess.call([tmp_fn, ])


if __name__ == '__main__' and __package__ is None:
    # set_env_in_app()
    set_env_from_shell()
