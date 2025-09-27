#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description='A simple CLI application to greet users.')
    
    parser.add_argument(
        '-n', '--name',
        type=str,
        default='World',
        help='The name to greet.'
    )
    
    parser.add_argument(
        '-g', '--greeting',
        type=str,
        default='Hello',
        help='The greeting message.'
    )
    
    args = parser.parse_args()

    message = f"{args.greeting}, {args.name}!"
    print(message)

if __name__ == "__main__":
    main()
