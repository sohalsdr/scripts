#!/usr/bin/env python

# Author:       sohalsdr
# Description:  Imports a .csv file and converts it into a markdown table.
#               It's not neat but it works.

import argparse
import sys
import os
import csv

def create_arg_parser():
    # Creates and returns the ArgumentParser object
    parser = argparse.ArgumentParser(description='Converts CSV file to a markdown table')
    parser.add_argument('inputDirectory',
                    help='Path to the input directory.')
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    filepath = parsed_args.inputDirectory
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist.")
    else:
        print(f"File {filepath} exists.")
        if not filepath.endswith('.csv'):
            print('Inputted file is not a csv file.')
        else:
            print('Table:\n')
            with open(filepath) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        print(f'| {" | ".join(row)} |')
                        print('|', end='')
                        for x in row:
                            print(' ----- |', end='')
                        print('')
                        line_count += 1
                    else:
                        print(f'| {" | ".join(row)} |')
                        line_count += 1
                print(f'\nProcessed {line_count} lines.')
