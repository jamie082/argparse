#!/usr/bin/python3

import argparse

# http://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
group.add_argument("-i", "--input", action="store_true")
group.add_argument("-u", "--user", action="store_true")
group.add_argument("-o", "--output", action="store_true")
args = parser.parse_args()
answer = args.x**args.y

'''
if args.input:
    print(f"Input file is: {args.input}")
    '''

if args.quiet:
    print(answer)
elif args.user:
    print(f"User file is: {args.user}")
elif args.output:
    print(f"Output file is: {args.output}")
