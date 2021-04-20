#!/usr/bin/python3

import os
import argparse

def main():
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument('--input', '-i',
                            dest='input_path',
                            help='Input file location',
                            required=True)

    parser.add_argument('--output', '-o',
                            dest='output_path',
                            help='Output file location',
                            required=True)

    args = parser.parse_args()
    search(args.input_path, args.output_path)

def search(input_path, output_path):
    print(input_path)
    print(output_path)


if __name__ == '__main__':
    main()
