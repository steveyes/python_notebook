#!/usr/bin/env bash
#

# COLOR_OFF="\033[0m"

COLOR_BLACK="\033[0;30m"
COLOR_RED="\033[0;31m"
COLOR_GREEN="\033[0;32m"
COLOR_ORANGE="\033[0;33m"
COLOR_BLUE="\033[0;34m"
COLOR_PURPLE="\033[0;35m"
COLOR_CYAN="\033[0;36m"
COLOR_LIGHT_GRAY="\033[0;37m"

COLOR_DARK_GRAY="\033[1;30m"
COLOR_LIGHT_RED="\033[1;31m"
COLOR_LIGHT_GREEN="\033[1;32m"
COLOR_LIGHT_YELLOW="\033[1;33m"
COLOR_LIGHT_BLUE="\033[1;34m"
COLOR_LIGHT_PURPLE="\033[1;35m"
COLOR_LIGHT_CYAN="\033[1;36m"
COLOR_WHITE="\033[1;37m"

function colorize() {
    local COLOR_OFF="\033[0m"
    local color=$1
    local strings=$2
    printf "%b%s%b\n" "${color}${strings}${COLOR_OFF}"
}

function color_red() {
    colorize $COLOR_LIGHT_RED "$1"
}

function color_blue() {
    colorize $COLOR_BLUE "$1"
}

function color_white() {
    colorize $COLOR_WHITE "$1"
}

function color_black() {
    colorize $COLOR_BLACK "$1"
}

color_red "red"
color_blue "blue"
color_white "white"
color_black "black"
