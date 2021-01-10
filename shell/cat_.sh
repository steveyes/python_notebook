function usage() {
    echo '--------------------Usage--------------------'
    cat <<- EOF
Usage:
    bash $0 [options] [ARGUMENT]
Examples:
    # groups and users
    bash $0
    # specific group: quant, and it's users
    bash $0 quant
    #######################################
    # to-do
    #
    # specific group: quant, and it's users
    # to-do
    bash $0 -g quant
    # specific user:
    # to-do
    bash $0 -u sixieops
    #######################################
EOF
    echo '--------------------Usage--------------------'
}


usage