#!/usr/bin/python3

import argparse

# http://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('--values', type=int, nargs=3)
parser.add_argument('--name', type=str, required=True)
group.add_argument('--add', action='store_true')
group.add_argument('--subtract', action='store_true')
parser.add_argument('x', type=int, help="positional argument x") # positional argument x
parser.add_argument('y', type=int, help="positional argument y") # positional argument y
args = parser.parse_args() # blah

if args.add:
    total = args.x + args.y
    print ('Difference:', total)

elif args.subtract:
    difference = args.x - args.y
    print ('Difference:', difference)

elif args.name:
    print('Hello,', args.name)

'''
sum = sum(args.values)
print('sum:', sum)
'''
