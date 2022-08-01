#!/usr/bin/python3

import argparse

# http://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
group.add_argument("-i", "--input", help="input sample", action="store_true")
group.add_argument("-u", "--user", help="user sample", action="store_true")
group.add_argument("-o", "--output", help="output sample", action="store_true")
group.add_argument('--values', type=int, nargs=3)
args = parser.parse_args() # blah


if args.input: # -i was typed
    print(f"Your input file is: {args.verbose}")
elif args.user: # -u was typed
    print(f"Your user file is: {args.user}")
elif args.output: # -o was typed
    print(f"Your user file is: {args.output}")

else:
    print("Error! Please try Again")

sum = sum(args.values)
print('sum:', sum)

