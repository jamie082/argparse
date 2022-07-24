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
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
elif args.input:
    print(f"{args.input}")
elif args.output:
    print(f"{args.output}")
elif args.user:
    print(f"{args.user}")
elif args.output:
    print(f"{args.output}")

else:
    print(f"{args.x}^{args.y} == {answer}")
