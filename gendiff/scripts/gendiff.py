##!/usr/bin/env python3

#from brain_games.cli import welcome_user

import argparse

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file second_file")

    parser.parse_args()



if __name__ == '__main__':
    main()



