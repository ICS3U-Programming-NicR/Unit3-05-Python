#!/usr/bin/env python3

# Created by: Nicolas Riscalas
# Created on: March 29 2022
# Find the number equivalent to a month


import sys


def weekday_name():
    month_num = input("Enter the number equivalent to a month ")
    match month_num:
        case "1":
            print("The equivalent month is January")
        case "2":
            print("The equivalent month is Febuary")
        case "3":
            print("The equivalent month is March")
        case "4":
            print("The equivalent month is April")
        case "5":
            print("The equivalent month is May")
        case "6":
            print("The equivalent month is June")
        case "7":
            print("The equivalent month is July")
        case "8":
            print("The equivalent month is August")
        case "9":
            print("The equivalent month is September")
        case "10":
            print("The equivalent month is October")
        case "11":
            print("The equivalent month is November")
        case "12":
            print("The equivalent month is December")
        case _:
            print("Invalid. Month number should be
                  + "an integer between and including 1 and 12")
    try_again = str(input("Would you like to try again? \n"))
    if (try_again == "Y"
        or try_again == "y"
        or try_again == "yes"
            or try_again == "YES"):
        main()
    elif try_again == "N"
    or try_again == "n"
    or try_again == "no"
    or try_again == "NO":
        sys.exit()


def main():
    # this function checks if there is over 30 students

    # input
    weekday_name()


if __name__ == "__main__":
    main()
