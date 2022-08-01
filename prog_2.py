#!/usr/bin/python3

import argparse

# http://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-i", "--input", help="input sample", action="store_true")
group.add_argument("-u", "--user", help="user sample", action="store_true")
group.add_argument("-o", "--output", help="output sample", action="store_true")
parser.add_argument('x', type=int) # positional argument x 
parser.add_argument('y', type=int) # positional argument y
parser.add_argument('--values', type=int, nargs=3)
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args() # blah


if args.input: # -i was typed
    print(f"Your input file is: {args.verbose}")
elif args.user: # -u was typed
    print(f"Your user file is: {args.user}")
elif args.output: # -o was typed
    print(f"Your user file is: {args.output}") 

elif args.subtract:
    differece = args.x - args.y
    print ('Difference:', difference)

elif args.name:
    print('Hello,', args.name)

'''
sum = sum(args.values)
print('sum:', sum)
'''
