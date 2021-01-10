#!/usr/bin/env bash

## readme
# suppose you have bin file helloworld and hellopython and even more bin files to package to this bash file, merged as one large bash file which later could be used to install all the bin files to the $dst_file.
# 1. tar -jcvf package.tar.xz helloworld hellopython
# 2. cat $0 package.tar.xz > install.sh
# 3. bash install.sh

# base vars
dst_dir=~/checkout/
line_no=$(sed -n '0, /^# bin file\[s\] start below/ p' $0 | wc -l)
temp_file=$(mktemp)
temp_dir=$(mktemp -d)

# retrieve the bin file which start from the end+1 of this bash file.
tail +$((line_no + 1)) $0 >${temp_file}

# untar and unzip the file
tar xf ${temp_file} -C ${temp_dir}

# install the files to the $dst_file
for file in ${temp_dir}/*; do
    cp ${temp_dir}/$file ${dst_dir}
done

exit 0

# bin file[s] start below
