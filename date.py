#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This program tells you if you can date a grandmother's grandchild


def main():
    # This function tells you if you can date a grandmother's grandchild

    # Input
    print("Can you date her grandchild?")
    user_rich = input("Are you rich (answer yes or no): ")
    user_good_looking = input("Are you good looking (answer yes or no): ")
    print("")

    # process
    if user_rich == "yes" or user_good_looking == "yes":
        # Output 1
        print("You can date her grandchild!")
    else:
        # Output 2
        print("Sorry, you can't date her grandchild.")


if __name__ == "__main__":
    main()
