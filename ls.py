# list directories
from argparse import ArgumentParser
import os

parser = ArgumentParser()

parser.add_argument('path', default='.', nargs='?')

args = parser.parse_args()
# print(args)

print(*os.listdir(args.path), sep='\n')

