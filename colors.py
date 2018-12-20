""" Module for applying colors on the print display."""


def print_red(prt):
    print(f"\033[91m {prt}\033[00m")  # Format start color code, text, end color code. '\x1b[0m' resets to default.


def print_green(prt):
    print(f"\033[92m {prt}\033[00m")


def print_yellow(prt):
    print(f"\033[93m {prt}\033[00m")


def print_light_purple(prt):
    print(f"\033[94m {prt}\033[00m")


def print_purple(prt):
    print(f"\033[95m {prt}\033[00m")


def print_cyan(prt):
    print(f"\033[96m {prt}\033[00m")


def print_light_gray(prt):
    print(f"\033[97m {prt}\033[00m")


def print_black(prt):
    print(f"\033[98m {prt}\033[00m")


def print_custom(prt):
    print(f"\33[101m {prt}\x1b[0m")
