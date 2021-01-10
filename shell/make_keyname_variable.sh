function assign() {
    local _keyname=$1
    local _value="$2"

    if [[ "$_keyname" ]]; then
        eval $_keyname="'$_value'"
    else
        echo "$_value"
    fi
}

keyname=$1
value=$2
assign "$keyname" "'$value'"
printf "%s=\"%s\"\n" "$keyname" "$value"
