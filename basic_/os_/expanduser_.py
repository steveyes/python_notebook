import os
from basic_.search_.is_line_in_file import is_line_in_file

file_path_bashrc = os.path.expanduser('~/.bashrc')
print(file_path_bashrc)

if is_line_in_file('# **** DEV_TOOL_CHAIN_TAG', file_path_bashrc):
    print('paths are already added, check %s for further infomation' % file_path_bashrc)
else:
    with open(file_path_bashrc, 'a') as f:
        f.write('''
# **** dev tool chain begins
# **** DEV_TOOL_CHAIN_TAG
# add /devel to paths
export LC_ALL=en_US.UTF-8
export LD_LIBRARY_PATH=/devel/lib:/devel/lib64
export LIBRARY_PATH=/devel/lib:/devel/lib64
export CDPATH=.:/devel/:$CDPATH
export PATH=./:/devel/bin:/usr/bin:/sbin:$PATH
export CC=`which gcc`
export CXX=`which g++`
export CMAKE_C_COMPILER=`which gcc`
export CMAKE_CXX_COMPILER=`which g++`
export CPPFLAGS="-I/devel/include"
export LDFLAGS="-L/devel/lib"
# **** dev tool chain ends
''')
